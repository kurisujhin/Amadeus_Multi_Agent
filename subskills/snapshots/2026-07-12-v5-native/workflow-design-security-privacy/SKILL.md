---
name: workflow-design-security-privacy
description: Use with multi-agent-workflow-designer when designing workflows for security, privacy, auth, access control, secrets, PII, sensitive data, data retention, permissions, threat modeling, abuse prevention, fraud, compliance evidence, audit logging, incident response, or high-risk data flows. Emphasize assets, trust boundaries, adversaries, data minimization, consent, auditability, detection, response, and recovery.
---

# Workflow Design: Security/Privacy

This domain subskill supplies security, privacy, abuse, and sensitive-data deltas to `multi-agent-workflow-designer`. It does not replace the parent workflow.

## Trigger

Use as the primary domain when security/privacy validity is the dominant risk in auth, permissions, secrets, PII, retention/deletion, consent, export, fraud/abuse, threats, audit, incidents, or sensitive data flows. Use as a borrowed lens when another domain touches identity, payment, enforcement, regulated data, or adversarial behavior. Security vocabulary alone does not decide primary routing; an auth migration can remain reliability-primary.

## Native V5 Parent Boundary

Emit marginal domain semantics only; the v5 parent owns workflow and effects as defined in `../SNAPSHOT.md`. This skill never issues permits, creates agents, chooses commit mode, resumes pauses, authorizes effects, or mutates canonical state.

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

## Native V5 Domain Delta

- `work_model_delta`: asset×boundary×threat path, principal×resource×action, data element×lifecycle stage; denied paths, privilege, data locations, detection/recovery coverage.
- `human_input_deltas`: purpose/authority, test authorization, residual-risk acceptance, incident/communication authority, processor/region policy.
- `action_delta`: protect raw access, credential use, adversarial execution, IAM/data-lifecycle mutation, containment, and disclosure.
- `anomaly_delta`: secret/PII exposure, new processor/region/class, privilege expansion, denied-path success, test-scope escape; distinguish configuration error, control bypass, identity failure, and scope escape using redacted audit trail, boundary map, denied control, and recovery evidence.
- `change_impact_delta`: purpose/authority/retention/boundary/data-class/permission/processor changes invalidate threat, lifecycle, identity, adversarial, incident, rights, and recovery evidence; packet references remain redacted.
- `insight_constraints`: no idea expands exploit/test scope, raw access, disclosure, or containment authority; preserve redaction and use a denied-path/boundary falsifier plus independent recovery confirmation.

## Native V5 Packet

Emit the complete `v5-domain-1` packet from the named domain sections with producer snapshot/fingerprint. The parent router and `../SNAPSHOT.md` own schema and authority rules. Reject unknown top-level fields; optional additions belong only in a namespaced `extensions` map.

## Behavior Tests

| Task | Expected behavior |
| --- | --- |
| Remove and rotate a staging webhook secret. | Keep Security/Privacy primary and borrow Software/Reliability. Inspect references/exposure without revealing the value; require threat, identity, and `SP-G4` test-authorization proof before denied-path or replay testing. Unknown production/public exposure blocks closure or a contained claim. |
| Migrate static service tokens to OIDC. | Keep reliability primary; inventory clients/claims safely and require threat, identity, bounded adversarial, and incident proof. Unknown clients, mappings, revocation, or recovery blocks IdP changes and rollout. |
| Implement regulated deletion across databases, logs, backups, and derived features. | Keep Security/Privacy primary and borrow Policy/Governance plus Software/Reliability; require all gates. Jurisdiction, authority, lineage, backup behavior, and rights propagation must close before deletion or attestation. |
| Build a cross-product identity graph for personalization and measurement. | Keep product/business primary; require purpose/owner workflow/counter-metrics plus all relevant security and policy gates. Linking, collection, sharing, experiments, and launch remain protected. |
