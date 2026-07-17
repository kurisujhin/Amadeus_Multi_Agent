---
name: workflow-design-security-privacy
description: Use with multi-agent-workflow-designer when designing workflows for security, privacy, auth, access control, secrets, PII, sensitive data, data retention, permissions, threat modeling, abuse prevention, fraud, compliance evidence, audit logging, incident response, or high-risk data flows. Emphasize assets, trust boundaries, adversaries, data minimization, consent, auditability, detection, response, and recovery.
---

# Workflow Design: Security/Privacy

This domain subskill supplies security, privacy, abuse, and sensitive-data deltas to `multi-agent-workflow-designer`. It does not replace the parent workflow.

## Trigger

Use as the primary domain when security/privacy validity is the dominant risk in auth, permissions, secrets, PII, retention/deletion, consent, export, fraud/abuse, threats, audit, incidents, or sensitive data flows. Use as a borrowed lens when another domain touches identity, payment, enforcement, regulated data, or adversarial behavior. Security vocabulary alone does not decide primary routing; an auth migration can remain reliability-primary.

## Parent Contract

- The parent owns real-subagent creation, runtime DAG and budgets, canonical ledgers, execution feedback, observer/reviewer separation, permits, protected-action dispatch, mutation ownership, insight validation, synthesis, and reporting.
- Review perspectives below are competencies, never real or virtual agents. The parent maps them to real runtime owners.
- Each gate record needs `gate_id`, `action_stage`, `proof_phase=entry|result`, `applicability=applicable|not_applicable|unresolved`, and `applicability_evidence_refs`. Only `applicable` gates receive `decision=pass|fail|escalate`, with evidence and blocked commitments; `not_applicable` needs positive scope evidence and a reopen trigger, while `unresolved` blocks. A direction-changing open gap cannot pass provisionally.
- High-impact claims require authoritative source, `observed_at`, effective version/date/environment/jurisdiction, applicability, conflicts, and invalidation trigger. Model memory cannot close legal interpretation or residual-risk acceptance.
- Never copy raw secrets, PII, prompts, private records, or exploit material into ledgers. Store redacted metadata, hashes, counts, and access-controlled stable references.
- Unknown environment, data class/subject, jurisdiction, purpose/authority, consent promise, processor, critical client, test authorization, deletion semantics, incident ownership, risk acceptance, schedule, or scope blocks dependent testing, mutation, launch, and claims.

## Domain Ledger Additions

- Assets/owners/data classes/objectives, actors/adversaries, entry points, trust boundaries, threat paths, controls, abuse cases, and residual-risk owners.
- Data subject/source/purpose/allowed use/necessity/authority or consent, transformations/derived data, stores/regions/processors, access/sharing, backups/logs/caches, retention/deletion propagation, and rights hooks.
- Principal/resource/action, required/granted privilege, authn/authz, token/session scope/expiry/revocation, break-glass, separation of duties, secret references/rotation, denied paths, audit, compatibility, and rollback.
- Test authorization/environment/data class, safety limits/stops/oracles; detection, evidence preservation, containment, communications, recovery/restore validation, and exercise.
- Obligations, jurisdiction/effective version, controls/evidence integrity, exceptions, rights request authentication/fulfillment/downstream propagation/appeal, and accountable owners.

## Domain Gates

| Gate | Pass condition | Required proof |
| --- | --- | --- |
| `SP-G1` AssetThreat | High-impact assets, boundaries, adversaries, threat/abuse paths, controls, residual risk, and accountable owners are linked. | `AssetThreatProof` with assets/objectives, actors, entry points, boundary identity/protocol/control refs, threat capability/path/preconditions/impact, abuse cases, out-of-scope, and residual-risk owners. |
| `SP-G2` DataLifecycle | Every personal/sensitive-data lifecycle stage is necessary, authorized, purpose-bound, bounded, and testable, including derived data and backups. | `DataLifecycleProof` with subjects, source/purpose/use/necessity/authority/notice, transformations, stores/locations/processors, roles/sharing, retention triggers, backups/caches/logs, deletion propagation, rights hooks, and minimization decisions. |
| `SP-G3` IdentitySecrets | Identity, credential, session, permission, break-glass, revocation, rotation, audit, compatibility, and rollback demonstrate least privilege. | `IdentitySecretsProof` with principal/resource/action paths, required/granted privilege, auth points, token scope/expiry/revocation, separation, secret references only, denied-path tests, compatibility, audit events, and owners. |
| `SP-G4` AdversarialVerification | Representative adversarial testing is explicitly authorized, isolated/bounded, oracle-driven, safely stopped, and critical findings are remediated/retested or accountably accepted. | `AdversarialVerificationProof` with authorization, environment, data class, threat refs, limits/stops, cases, expected controls/results, severity, remediation/retest, evidence refs, and residual risks. |
| `SP-G5` IncidentRecovery | Detection through triage, containment, evidence preservation, communication, recovery, restore validation, and rollback/forward fix has exercised owners and authority. | `IncidentRecoveryProof` with scenarios/signals/coverage/tests, telemetry class, routes/owners, containment/credential actions, preservation, notification authority, recovery/validation, dependencies, and exercise refs. |
| `SP-G6` ObligationRights | Current obligations and user rights map to tested controls, evidence generation/integrity, exceptions, fulfillment, downstream propagation, and appeal/escalation. | `ObligationRightsProof` with authority/jurisdiction/scope/effective version, requirement/control/evidence/retention/access/owner, exceptions/conflicts, rights request authentication, fulfillment, propagation, appeal, tests, and disposition. |

## Safe Start And Protected Actions

Before an execution permit, safe start is limited to authorized read-only retrieval of code, IaC, configuration, catalogs, approved policies, metadata-only IAM/secret references, data-flow mapping, threat modeling, synthetic test design, and offline static checks. Production data, secret values, or privileged stores are not safe merely because access is read-only.

Keep viewing/exporting raw PII or secrets; credential use or impersonation; live scanning, fuzzing, exploitation, phishing, or abuse simulation; IAM/auth/token/secret/logging/collection/consent/sharing/retention/deletion/detection changes; containment/revocation/recovery; user/regulator communication; rollout, attestation, and final launch recommendation blocked until their action-stage gates pass. An emergency relies on exact pre-authorized decision rights and parent control, not a domain bypass.

When an authorized control change or adversarial test is necessary to produce result evidence, use a narrow parent `validation` permit after test authorization, environment isolation, data-class limits, oracles, stop/recovery conditions, and entry gates pass. Keep containment claims, rollout, attestation, and launch blocked under `result_gates_due`.

## Review Perspectives

- Asset, threat, control, and residual-risk analysis.
- Privacy/data governance, minimization, consent, retention, deletion, and rights.
- Identity, access, secrets, sessions, and least privilege.
- Abuse/adversarial verification and safety limits.
- Reliability, detection, incident response, evidence preservation, and recovery.
- Legal, compliance, policy, product, fairness, or domain expertise when applicable.

## Borrowed Lenses

- `workflow-design-software-reliability` for migrations, compatibility, rollout, observability, and rollback.
- `workflow-design-policy-governance` for rights, appeal, fairness, authority, and people-affecting enforcement.
- `workflow-design-tabular-ml-evaluation` for fraud/risk scores, thresholds, calibration, label bias, and monitoring.
- `workflow-design-llm-nlp` for prompt/tool injection, agent effects, generated explanations, and LLM-assisted security.
- `workflow-design-product-business-decision` for business purpose, affected non-users, adoption, counter-metrics, and launch decisions.

## Simplification Rules

- `SP-G1` always applies when security/privacy is primary. `SP-G2` applies to personal/sensitive data; `SP-G3` to identity/access/secrets; `SP-G4` to attacker-controlled surfaces or security claims; `SP-G5` to production controls or credible incidents; `SP-G6` to obligations, audit, rights, or people-affecting consequences.
- One local, non-production, synthetic-data, reversible scope may combine applicable proof into one compact packet and combine compatible perspectives. Gate decisions remain distinct.
- Production, regulated data, cross-boundary sharing, auth migration, irreversible deletion, adaptive attackers, active incidents, multiple jurisdictions, or business decisions require expanded proof.
- Missing evidence is never `not_applicable`; the parent alone decides runtime separation and direct-path eligibility.

## Blocking Failure Modes

Return `fail|escalate` when sensitive handling is assumed, threats are unlinked to controls/owners, auth changes lack lifecycle/compatibility/recovery, adversarial work lacks authorization and limits, evidence leaks sensitive material, or detection lacks accountable response and validated restoration.

## V4 Runtime Handoff

Return redacted marginal deltas to v4. Barriers precede raw sensitive access/export, credential use/impersonation, adversarial execution, IAM/data-lifecycle mutation, containment, and communications. Emit parent feedback for secret/PII exposure, unexpected class/processor/region, denied-path success, privilege expansion, test-scope escape, detection/containment failure, or evidence leakage. Safe stop may revoke/isolate/preserve evidence only under authorized incident ownership. A security idea is only a redacted `InsightCandidate`; it cannot broaden exploit scope, reveal sensitive material, or authorize access. Freeze the cheapest authorized falsifier and untouched control; safety vetoes dominate domain passes.

## Domain Gate Packet

```text
DomainGatePacket:
  parent_contract_version: v4
  packet_domain: Security/Privacy
  routing_role: primary|borrowed
  primary_domain: set by parent
  route_reason: dominant validity/risk or marginal domain delta
  marginal_gate_delta: [question, gate, proof, trigger, or protected action changed]
  omit_or_exception_reason: [plausible lens omitted or default-two exception]
  ledger_additions: [redacted field=value or stable_ref ...]
  knowledge_sources: [source, authority, effective_version_date_environment_jurisdiction, observed_at, applicability, conflicts, invalidation_trigger, status]
  freshness_required: [claim -> freshness or change trigger]
  retrieval_status: complete|partial|blocked
  required_questions: [direction-changing unknown -> accountable owner]
  reviewers: [perspective -> real runtime owner assigned by parent]
  domain_gates: [gate_id, action_stage, proof_phase, applicability, applicability_evidence_refs, decision, evidence_required, evidence_refs, open_gap_ids, blocked_commitments, required_change, reopen_or_invalidation_trigger]
  shared_evidence_refs: [artifact -> consuming domain gates]
  runtime_handoff: [semantic_barriers, anomaly_triggers, max_unchecked_interval_or_NA, direct_evidence_refs, safe_stop_state, observer_authority, affected_gate_proof_permit_descendants]
  insight_constraints: [protected_invariants, cheapest_falsifier, confirmation_boundary, contamination]
  handoff_status: ready|partial|blocked
  validation_artifacts: [redacted stable artifact refs]
  borrowed_lenses: [skill -> reason]
  stop_conditions: [authorization, exposure, safety, or evidence stop]
  simplification_triggers: [gate -> positive applicability evidence and reopen condition]
```

## Behavior Tests

| Task | Expected behavior |
| --- | --- |
| Remove and rotate a staging webhook secret. | Keep Security/Privacy primary and borrow Software/Reliability. Inspect references/exposure without revealing the value; require threat, identity, and `SP-G4` test-authorization proof before denied-path or replay testing. Unknown production/public exposure blocks closure or a contained claim. |
| Migrate static service tokens to OIDC. | Keep reliability primary; inventory clients/claims safely and require threat, identity, bounded adversarial, and incident proof. Unknown clients, mappings, revocation, or recovery blocks IdP changes and rollout. |
| Implement regulated deletion across databases, logs, backups, and derived features. | Keep Security/Privacy primary and borrow Policy/Governance plus Software/Reliability; require all gates. Jurisdiction, authority, lineage, backup behavior, and rights propagation must close before deletion or attestation. |
| Build a cross-product identity graph for personalization and measurement. | Keep product/business primary; require purpose/owner workflow/counter-metrics plus all relevant security and policy gates. Linking, collection, sharing, experiments, and launch remain protected. |

## Runtime Enforcement

The parent must evaluate each applicable gate as `pass|fail|escalate` against named evidence refs; prose that merely mentions a concern is not proof. Every `fail|escalate` record must list the protected action it blocks, the owner of the missing evidence, and the reopen trigger. `N/A` requires positive applicability evidence and a residual-limit statement. A threat model or scan with no exercised exploit path, owner, response SLA, and recovery rehearsal cannot authorize exposure.

## Self-Improvement Hook

After a task, emit a `DomainSkillUpdateCandidate` only when evidence shows a recurring missing trigger, gate, perspective, control, or abuse case. Include task evidence and one failing-then-passing behavior test. Do not mutate the installed skill unless the user requested or approved improvement.
