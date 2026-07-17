#!/usr/bin/env python3
"""Strict stdlib validator for the native v5-domain-1 handoff contract."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any


SNAPSHOT_ID = "2026-07-12-v5-native"
VALIDATOR_VERSION = "v5-domain-validator-1"
PINNED_SCHEMA_SHA256 = "7ec5c158e9a1e90b2bd25663dbd899c6ba9320f4e1a90896271793bdbd2816af"
PINNED_MANIFEST_SHA256 = "5f97080d18cd7a2691fc09ab2482ec689864e8be54179bfa997718083e29c4d6"
SCRIPT = Path(__file__).resolve()
V5_ROOT = SCRIPT.parent.parent
SERIES_ROOT = V5_ROOT.parent.parent
DEFAULT_PRODUCER_ROOT = SERIES_ROOT / "subskills/snapshots" / SNAPSHOT_ID
DEFAULT_MANIFEST = DEFAULT_PRODUCER_ROOT / "manifest.sha256"
DEFAULT_SCHEMA = V5_ROOT / "references/v5-domain-1.schema.json"

FORBIDDEN_AUTHORITY_KEYS = {
    "permit", "agent_creation", "commit_mode", "resume_authority",
    "effect_authorization", "canonical_state_mutation",
}
AUTHORITY_ASSERTION = re.compile(
    r"\b(?:permit\s+(?:is\s+)?granted|effect\s+(?:is\s+)?authorized|"
    r"resume\s+(?:the\s+)?pause|commit[_ -]?mode\s*[:=]|"
    r"canonical\s+state\s+mutat(?:e|ion)|(?:I|we|domain|subskill)\s+"
    r"(?:hereby\s+)?(?:authorize|approve|grant|resume|commit|mutate))\b",
    re.IGNORECASE,
)
PASSIVE_AUTHORITY_ASSERTION = re.compile(
    r"(?:\b(?:packet|domain|subskill|authorization|approval|permit|protected effect)\b.*"
    r"\b(?:grants?|granted|approves?|approved|authorizes?|authorized|permitted)\b|"
    r"\bpause\b.*\b(?:may|can|is)\b.*\bresum(?:e|ed)\b|"
    r"\bcanonical state\b.*\b(?:may|can|is)\b.*\bmutat(?:e|ed)\b)", re.IGNORECASE,
)


class ContractError(ValueError):
    """A deterministic packet-contract rejection."""


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ContractError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _reject_constant(value: str) -> None:
    raise ContractError(f"nonstandard JSON constant: {value}")


def _reject_surrogates(value: Any, location: str = "$") -> None:
    if isinstance(value, str):
        if any(0xD800 <= ord(char) <= 0xDFFF for char in value):
            raise ContractError(f"invalid Unicode surrogate at {location}")
    elif isinstance(value, dict):
        for key, nested in value.items():
            _reject_surrogates(key, f"{location}.<key>")
            _reject_surrogates(nested, f"{location}.{key}")
    elif isinstance(value, list):
        for index, nested in enumerate(value):
            _reject_surrogates(nested, f"{location}[{index}]")


def parse_json_bytes(payload: bytes) -> Any:
    """Parse strict UTF-8 JSON, rejecting duplicate keys and NaN/Infinity."""
    try:
        source = payload.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ContractError("input is not UTF-8") from exc
    if source.startswith("\ufeff"):
        raise ContractError("UTF-8 BOM is not accepted")
    try:
        value = json.loads(source, object_pairs_hook=_reject_duplicate_keys,
                           parse_constant=_reject_constant)
    except ContractError:
        raise
    except json.JSONDecodeError as exc:
        raise ContractError(f"malformed JSON at line {exc.lineno} column {exc.colno}") from exc
    _reject_surrogates(value)
    return value


def load_schema(path: Path = DEFAULT_SCHEMA) -> dict[str, Any]:
    payload = path.read_bytes()
    if sha256_bytes(payload) != PINNED_SCHEMA_SHA256:
        raise ContractError("schema bytes do not match the pinned published schema")
    schema = parse_json_bytes(payload)
    if not isinstance(schema, dict):
        raise ContractError("schema root must be an object")
    return schema


def _resolve_ref(root: dict[str, Any], reference: str) -> dict[str, Any]:
    if not reference.startswith("#/"):
        raise ContractError(f"unsupported schema reference: {reference}")
    current: Any = root
    for component in reference[2:].split("/"):
        component = component.replace("~1", "/").replace("~0", "~")
        if not isinstance(current, dict) or component not in current:
            raise ContractError(f"broken schema reference: {reference}")
        current = current[component]
    if not isinstance(current, dict):
        raise ContractError(f"schema reference is not an object: {reference}")
    return current


def _json_type_matches(value: Any, expected: str) -> bool:
    return {
        "object": isinstance(value, dict), "array": isinstance(value, list),
        "string": isinstance(value, str),
        "number": isinstance(value, (int, float)) and not isinstance(value, bool),
        "integer": isinstance(value, int) and not isinstance(value, bool),
        "boolean": isinstance(value, bool), "null": value is None,
    }.get(expected, False)


def validate_schema_instance(value: Any, schema: dict[str, Any], *,
                             root: dict[str, Any] | None = None,
                             location: str = "$") -> None:
    """Enforce the JSON-Schema subset used by the checked-in contract."""
    root = schema if root is None else root
    if "$ref" in schema:
        validate_schema_instance(value, _resolve_ref(root, schema["$ref"]),
                                 root=root, location=location)
        return
    if "anyOf" in schema:
        for alternative in schema["anyOf"]:
            try:
                validate_schema_instance(value, alternative, root=root, location=location)
                return
            except ContractError:
                pass
        raise ContractError(f"{location} matches no allowed schema alternative")
    if "const" in schema and value != schema["const"]:
        raise ContractError(f"{location} must equal {schema['const']!r}")
    if "enum" in schema and value not in schema["enum"]:
        raise ContractError(f"{location} has an unsupported value")
    expected = schema.get("type")
    if expected is not None and not _json_type_matches(value, expected):
        raise ContractError(f"{location} must be {expected}")
    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0):
            raise ContractError(f"{location} is too short")
        if "pattern" in schema and re.fullmatch(schema["pattern"], value) is None:
            raise ContractError(f"{location} does not match the required pattern")
    elif isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            raise ContractError(f"{location} has too few items")
        if "items" in schema:
            for index, item in enumerate(value):
                validate_schema_instance(item, schema["items"], root=root,
                                         location=f"{location}[{index}]")
    elif isinstance(value, dict):
        missing = set(schema.get("required", [])) - set(value)
        if missing:
            raise ContractError(f"{location} is missing fields: {', '.join(sorted(missing))}")
        properties = schema.get("properties", {})
        additional = schema.get("additionalProperties", True)
        for key, item in value.items():
            if key in properties:
                child_schema = properties[key]
            elif additional is False:
                raise ContractError(f"{location} has unknown field: {key}")
            elif isinstance(additional, dict):
                child_schema = additional
            else:
                child_schema = None
            if child_schema is not None:
                validate_schema_instance(item, child_schema, root=root,
                                         location=f"{location}.{key}")
        if "propertyNames" in schema:
            for key in value:
                validate_schema_instance(key, schema["propertyNames"], root=root,
                                         location=f"{location}.<key>")


def canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True,
                      separators=(",", ":")).encode("utf-8")


def parse_manifest(path: Path) -> dict[str, str]:
    payload = path.read_bytes()
    if sha256_bytes(payload) != PINNED_MANIFEST_SHA256:
        raise ContractError("manifest bytes do not match the pinned native snapshot manifest")
    entries: dict[str, str] = {}
    try:
        lines = payload.decode("utf-8").splitlines()
    except UnicodeDecodeError as exc:
        raise ContractError("manifest is not UTF-8") from exc
    for number, line in enumerate(lines, 1):
        match = re.fullmatch(r"([0-9a-f]{64})  (\./[^\s]+)", line)
        if match is None:
            raise ContractError(f"malformed manifest line {number}")
        digest, relative = match.groups()
        if relative in entries:
            raise ContractError(f"duplicate manifest path: {relative}")
        entries[relative] = digest
    return entries


def package_fingerprint(producer: Path) -> str:
    skill_hash = sha256_bytes((producer / "SKILL.md").read_bytes())
    yaml_hash = sha256_bytes((producer / "agents/openai.yaml").read_bytes())
    identity = f"SKILL.md {skill_hash}\nagents/openai.yaml {yaml_hash}\n".encode("utf-8")
    return sha256_bytes(identity)


def verify_producer(identity: dict[str, Any], *, producer_root: Path = DEFAULT_PRODUCER_ROOT,
                    manifest_path: Path = DEFAULT_MANIFEST,
                    expected_producer: str | None = None,
                    expected_fingerprint: str | None = None) -> Path:
    name = identity["subskill_name"]
    if expected_producer is not None and name != expected_producer:
        raise ContractError("producer does not match the expected producer")
    if "/" in name or name in {"", ".", ".."}:
        raise ContractError("unsafe producer name")
    producer = producer_root / name
    if not producer.is_dir():
        raise ContractError("producer package is missing")
    files = sorted(path.relative_to(producer).as_posix()
                   for path in producer.rglob("*") if path.is_file())
    if files != ["SKILL.md", "agents/openai.yaml"]:
        raise ContractError("producer package must contain exactly SKILL.md and agents/openai.yaml")
    manifest = parse_manifest(manifest_path)
    for relative in files:
        expected = manifest.get(f"./{name}/{relative}")
        if expected is None or sha256_bytes((producer / relative).read_bytes()) != expected:
            raise ContractError(f"producer file is absent from or mismatches manifest: {relative}")
    observed = package_fingerprint(producer)
    if identity["subskill_fingerprint"] != observed:
        raise ContractError("producer fingerprint mismatch")
    if expected_fingerprint is not None and observed != expected_fingerprint:
        raise ContractError("producer does not match the expected fingerprint")
    return producer


def _all_mapping_keys(value: Any):
    if isinstance(value, dict):
        for key, nested in value.items():
            yield key
            yield from _all_mapping_keys(nested)
    elif isinstance(value, list):
        for nested in value:
            yield from _all_mapping_keys(nested)


def _all_strings(value: Any):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for nested in value.values():
            yield from _all_strings(nested)
    elif isinstance(value, list):
        for nested in value:
            yield from _all_strings(nested)


def _positive_strings(values: list[str]) -> bool:
    return bool(values) and all(value.strip() and value == value.strip() for value in values)


def _validate_semantics(packet: dict[str, Any]) -> None:
    if FORBIDDEN_AUTHORITY_KEYS & set(_all_mapping_keys(packet)):
        raise ContractError("domain packet claims parent authority")
    if any(AUTHORITY_ASSERTION.search(value) or PASSIVE_AUTHORITY_ASSERTION.search(value)
           for value in _all_strings(packet)):
        raise ContractError("domain packet asserts parent authority in text")
    for key in ("primary_domain", "route_reason", "marginal_delta"):
        value = packet["routing"][key]
        if not value.strip() or value != value.strip():
            raise ContractError(f"routing field {key} must be canonical and nonblank")
    for item in packet["human_input_deltas"]:
        if item.get("applicability") == "not_applicable":
            if not item["fact"].strip() or not _positive_strings(item["evidence_refs"]):
                raise ContractError("not-applicable human input needs positive evidence")
            continue
        affected, blocked = item["decisions_actions_gates_affected"], item["blocked_commitments"]
        if (not item["fact"].strip() or not item["authorized_owner"].strip()
                or not _positive_strings(affected) or not _positive_strings(blocked)
                or not _positive_strings(item["reopen_trigger"])
                or not set(affected).issubset(blocked)):
            raise ContractError("unresolved human input must map positive blocked commitments")
    for gate in packet["domain_gates"]:
        for key in ("gate_id", "action_stage"):
            if not gate[key].strip() or gate[key] != gate[key].strip():
                raise ContractError(f"gate field {key} must be canonical and nonblank")
        applicability, decision = gate["applicability"], gate["decision"]
        if not _positive_strings(gate["applicability_evidence_refs"]):
            raise ContractError("gate applicability needs positive evidence")
        if applicability == "not_applicable":
            if decision != "not_applicable" or any(
                    gate[key] for key in ("open_gap_ids", "blocked_commitments", "required_change")):
                raise ContractError("not-applicable gate has inconsistent decision or unresolved state")
        elif applicability == "unresolved":
            if (decision != "open" or not _positive_strings(gate["open_gap_ids"])
                    or not _positive_strings(gate["blocked_commitments"])
                    or gate["action_stage"] not in gate["blocked_commitments"]):
                raise ContractError("unresolved applicability requires an open mapped block")
        elif decision == "not_applicable" or not _positive_strings(gate["evidence_required"]):
            raise ContractError("applicable gate needs an evidence contract and applicable decision")
        if decision == "pass" and (not _positive_strings(gate["evidence_refs"])
                or gate["open_gap_ids"] or gate["blocked_commitments"] or gate["required_change"]):
            raise ContractError("pass gate contains missing proof or unresolved state")
        if decision in {"open", "blocked"} and (not _positive_strings(gate["open_gap_ids"])
                or not _positive_strings(gate["blocked_commitments"])
                or gate["action_stage"] not in gate["blocked_commitments"]):
            raise ContractError("open gate must map its gaps and blocked commitments")
        if not _positive_strings(gate["reopen_or_invalidation_trigger"]):
            raise ContractError("gate needs a positive reopen or invalidation trigger")
    work = packet["work_model_delta"]
    work_substance = any(work[key].strip() for key in (
        "semantic_units_and_cardinality", "governing_source_or_dataflow",
        "loops_fanout_access_pattern", "lower_bounds",
    )) or any(value.strip() for key in (
        "calibration_slices_and_oracles", "progress_resource_integrity_signals"
    ) for value in work[key])
    if not work_substance and not _positive_strings(work["domain_NA_evidence"]):
        raise ContractError("empty work-model delta lacks positive N/A evidence")
    for group in ("action_delta", "anomaly_delta", "change_impact_delta"):
        delta = packet[group]
        substantive = [key for key in delta if key != "domain_NA_evidence"]
        if not any(value.strip() for key in substantive for value in delta[key]) \
                and not _positive_strings(delta["domain_NA_evidence"]):
            raise ContractError(f"empty {group} lacks positive N/A evidence")


def validate_packet(packet: Any, *, producer_root: Path = DEFAULT_PRODUCER_ROOT,
                    manifest_path: Path = DEFAULT_MANIFEST,
                    schema_path: Path = DEFAULT_SCHEMA,
                    expected_producer: str | None = None,
                    expected_fingerprint: str | None = None) -> dict[str, Any]:
    try:
        canonical_json_bytes(packet)
    except (TypeError, ValueError, UnicodeEncodeError) as exc:
        raise ContractError("packet contains a non-JSON value or nonstandard constant") from exc
    validate_schema_instance(packet, load_schema(schema_path))
    assert isinstance(packet, dict)
    verify_producer(packet["producer"], producer_root=producer_root,
                    manifest_path=manifest_path, expected_producer=expected_producer,
                    expected_fingerprint=expected_fingerprint)
    _validate_semantics(packet)
    return packet


def validate_routing_join(packets: list[dict[str, Any]]) -> None:
    if not packets:
        raise ContractError("routing bundle must not be empty")
    primaries = [packet for packet in packets if packet["routing"]["role"] == "primary"]
    if len(primaries) != 1:
        raise ContractError("routing join requires exactly one primary")
    primary = primaries[0]["producer"]["subskill_name"]
    if any(packet["routing"]["primary_domain"] != primary for packet in packets):
        raise ContractError("routing join disagrees on primary domain")
    producers = [packet["producer"]["subskill_name"] for packet in packets]
    if len(producers) != len(set(producers)):
        raise ContractError("routing join has a duplicate producer")


def validate_bundle(bundle: Any, *, producer_root: Path = DEFAULT_PRODUCER_ROOT,
                    manifest_path: Path = DEFAULT_MANIFEST,
                    schema_path: Path = DEFAULT_SCHEMA) -> list[dict[str, Any]]:
    if not isinstance(bundle, dict) or set(bundle) != {"packets"} \
            or not isinstance(bundle["packets"], list):
        raise ContractError("bundle must be exactly an object with a packets array")
    packets = [validate_packet(packet, producer_root=producer_root,
                               manifest_path=manifest_path, schema_path=schema_path)
               for packet in bundle["packets"]]
    validate_routing_join(packets)
    return packets


def validation_receipt(packets: list[dict[str, Any]], *, mode: str,
                       rendered_input_bytes: bytes,
                       schema_path: Path = DEFAULT_SCHEMA,
                       manifest_path: Path = DEFAULT_MANIFEST) -> dict[str, Any]:
    # Recheck at receipt time so a path override cannot drift after packet validation.
    load_schema(schema_path)
    parse_manifest(manifest_path)
    receipt = {
        "mode": mode, "packet_count": len(packets),
        "canonical_packet_sha256": [
            sha256_bytes(canonical_json_bytes(packet)) for packet in packets
        ],
        "producers": [packet["producer"]["subskill_name"] for packet in packets],
        "producer_package_fingerprints": [
            {
                "producer": packet["producer"]["subskill_name"],
                "subskill_fingerprint": packet["producer"]["subskill_fingerprint"],
            }
            for packet in packets
        ],
        "rendered_input_bytes_sha256": sha256_bytes(rendered_input_bytes),
        "routing_join": "accepted" if mode == "bundle" else "not_requested",
        "schema_sha256": PINNED_SCHEMA_SHA256,
        "snapshot_manifest_sha256": PINNED_MANIFEST_SHA256,
        "status": "accepted",
        "validator_script_sha256": sha256_bytes(SCRIPT.read_bytes()),
        "validator_version": VALIDATOR_VERSION,
    }
    if mode == "bundle":
        receipt["bundle_input_bytes_sha256"] = sha256_bytes(rendered_input_bytes)
    return receipt


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", default="-", help="JSON file, or - for stdin")
    parser.add_argument("--bundle", action="store_true",
                        help="validate a {packets: [...]} routing join")
    parser.add_argument("--producer-root", type=Path, default=DEFAULT_PRODUCER_ROOT)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--producer", help="expected producer name for a single packet")
    parser.add_argument("--fingerprint", help="expected package fingerprint for a single packet")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        if args.bundle and (args.producer is not None or args.fingerprint is not None):
            raise ContractError("--producer and --fingerprint apply only to a single packet")
        payload = sys.stdin.buffer.read() if args.input == "-" else Path(args.input).read_bytes()
        value = parse_json_bytes(payload)
        if args.bundle:
            packets = validate_bundle(value, producer_root=args.producer_root,
                                      manifest_path=args.manifest, schema_path=args.schema)
            receipt = validation_receipt(
                packets, mode="bundle", rendered_input_bytes=payload,
                schema_path=args.schema, manifest_path=args.manifest,
            )
        else:
            packet = validate_packet(value, producer_root=args.producer_root,
                                     manifest_path=args.manifest, schema_path=args.schema,
                                     expected_producer=args.producer,
                                     expected_fingerprint=args.fingerprint)
            receipt = validation_receipt(
                [packet], mode="single", rendered_input_bytes=payload,
                schema_path=args.schema, manifest_path=args.manifest,
            )
        sys.stdout.buffer.write(canonical_json_bytes(receipt) + b"\n")
        return 0
    except (ContractError, OSError) as exc:
        sys.stderr.buffer.write(canonical_json_bytes(
            {"error": str(exc), "status": "rejected"}) + b"\n")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
