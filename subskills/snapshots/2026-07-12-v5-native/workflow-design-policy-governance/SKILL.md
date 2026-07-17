---
name: workflow-design-policy-governance
description: Use with multi-agent-workflow-designer when designing workflows for policy, governance, moderation, approval/denial, eligibility, appeals, audits, fairness, compliance, fraud/risk, safety, or high-impact people-affecting systems in domains such as finance, health, education, hiring, refunds, workplace, or content enforcement. Emphasize stakeholders, rights, appeal, auditability, fairness, privacy, enforceability, and human override.
---

# Workflow Design: Policy/Governance

This domain subskill supplies policy and governance deltas to `multi-agent-workflow-designer`. It does not replace the parent workflow.

## Trigger

Use as the primary domain when policy validity, rights, enforcement, or governance risk dominates: moderation, eligibility, approval/denial, appeals, audit, compliance, fraud/risk, safety, workforce, education, health, finance, housing, hiring, refunds, or public-impact decisions. Use as a borrowed lens whenever an artifact can materially affect rights, access, opportunity, safety, reputation, money, or enforcement.

## Native V5 Parent Boundary

Emit marginal domain semantics only; the v5 parent owns workflow and effects as defined in `../SNAPSHOT.md`. This skill never issues permits, creates agents, chooses commit mode, resumes pauses, authorizes effects, or mutates canonical state.

## Domain Ledger Additions

- Decision/action, authority type, binding status, jurisdiction, covered entity/product/population, effective and transition dates, hierarchy, delegation, exceptions, and supersession.
- Stakeholders and affected non-users, rights/interests, vulnerabilities, accessibility needs, harms, safeguards, and remedies.
- Enforcement authority, forecast volume, staffing/capacity, consistency standard, separation of duties, override, notice, explanation, appeal, and audit trail.
- Sensitive data purpose, authority/consent, necessity, access, sharing/transfer, retention, deletion, and audit.
- Fairness estimands/slices, abuse and insider cases, monitoring, complaints, incidents, change watch, and rollback.

## Domain Gates

| Gate | Pass condition | Required proof |
| --- | --- | --- |
| `PG-G1` AuthorityApplicability | Current controlling authority applies to the exact jurisdiction, entity, product, population, and action; hierarchy conflicts and exceptions are resolved. | `AuthorityApplicabilityMatrix` with issuer, authority type, binding status, scope, publication/effective/transition/end dates, version, hierarchy, delegation, exceptions, supersession, conflicts, and interpretation owner. |
| `PG-G2` StakeholderRights | Users, affected non-users, operators, and vulnerable groups have mapped rights/interests, harms, safeguards, and remedies. | `StakeholderRightsHarmMap` with scenario/effect, right or duty, accessibility need, severity/likelihood, notice/consent, safeguard, and remedy owner. |
| `PG-G3` EnforceabilityCapacity | The authorized workflow can operate consistently at expected volume with trained capacity, QA, and failure handling. | `EnforcementCapacityEvidence` with authority, workflow, volume, staffing/skills/language coverage, SLA, rubric, QA results, overflow, separation of duties, and fallback. |
| `PG-G4` RedressAuditOverride | Notice, explanation, provenance, appeal, independent review, authorized override, accessibility, and remedy work end to end. | `RedressAuditOverrideTest` with notice channels/timing, explanation fields, audit schema/retention/access, appeal path/SLA, override authority, accessibility, remedies, and test results. |
| `PG-G5` FairnessImpact | Decision and error outcomes, uncertainty, proxies, intersections, threshold tradeoffs, and mitigations are measured for affected slices. | `FairnessImpactRecord` with population/baseline, outcome/error metrics, sample limits, protected/vulnerable slices, proxy analysis, mitigation, residual disparity owner, and monitoring trigger. |
| `PG-G6` PrivacyLifecycle | Every data element is necessary, authorized, purpose-bound, access-controlled, retained/deleted appropriately, and auditable. | `PrivacyDataLifecycleMap` with subject, purpose, authority/consent, source, sensitivity, collection/use/sharing/transfer, access, retention/deletion, audit controls, and required approvals. |
| `PG-G7` AbuseMisuse | External, insider, false-report, evasion, gaming, and appeal-abuse paths have tested prevention, detection, and response. | `AbuseMisuseCaseRegister` with actor/target/capability/incentive, entry point, harm, detectability, controls, response, test evidence, and residual-risk owner. |
| `PG-G8` MonitoringChange | Outcomes, complaints, appeals, authority changes, capacity, abuse, fairness, and privacy have owners, triggers, response, and revalidation. | `GovernanceMonitoringChangePlan` with denominated/sliced metrics, data quality, evidence-backed triggers, cadence, escalation, incident/kill path, audit sampling, change watch, and retention. |

## Safe Start And Protected Actions

Before an execution permit, safe start is limited to read-only source/version retrieval, stakeholder/data/decision/current-process inventories, conditional matrices with unknowns marked `TBD`, historical capacity/complaint/appeal analysis, and cost-capped tests on synthetic or already-authorized deidentified data. Draft options and red-team cases may not be published as decision guidance.

Keep policy adoption, final recommendation, approval/denial/ranking/moderation/sanction/eligibility/enforcement, threshold selection, model training, experiments, production configuration, sensitive-data expansion/transfer, notices, residual-risk acceptance, and rollout blocked until their action-stage gates pass. A bounded authorized policy/evaluation probe may receive a `validation` permit after entry gates pass; result evidence remains due and no policy recommendation, people-affecting action, claim, or rollout is unlocked.

## Review Perspectives

- Policy/domain authority and jurisdiction.
- Rights, affected stakeholders, fairness, and accessibility.
- Privacy, legal, and safety.
- Enforcement operations, audit, appeal, and human override.
- Abuse/adversarial behavior and monitoring.

## Borrowed Lenses

- `workflow-design-tabular-ml-evaluation` for scores, labels, calibration, thresholds, and impact measurement.
- `workflow-design-llm-nlp`, `workflow-design-vision-multimodal`, or `workflow-design-speech-audio` when those modalities drive decisions or explanations.
- `workflow-design-security-privacy` for sensitive data, access, audit logs, abuse, and incident execution.
- `workflow-design-product-business-decision` when adoption, economics, or no-build alternatives affect the recommendation.

Choose at most two borrowed lenses by default. Add another only when its distinct risk changes a gate, proof artifact, or protected action.

## Simplification Rules

- A single-jurisdiction, nonbinding analysis with no personal data, automation, enforcement, or people-affecting recommendation may combine proof into a `CompactPolicyReview`, but each applicable gate retains a separate decision.
- Automation, multiple jurisdictions, sensitive data, high-impact decisions, or deployment prohibit artifact simplification.
- A gate is `not_applicable` only with scoped evidence and a recheck trigger; missing or ambiguous applicability is `unresolved`, not `not_applicable`.
- Simplification never waives source closure, unknown blocking, parent permits, independent observation, restart review, or synthesis.

## Blocking Failure Modes

Block the affected commitment when authority, jurisdiction, hierarchy, rights, redress, enforceability, fairness, privacy, or abuse evidence is missing; when detection optimization ignores false harm; or when a changed source invalidates the snapshot supporting the permit.

## Native V5 Domain Delta

- `work_model_delta`: jurisdiction×population×decision×authority version plus cases/appeals; authority coverage, reviewer capacity, disparity, complaint/appeal volume.
- `human_input_deltas`: controlling interpretation owner, intended jurisdiction/population/scope, decision rights, residual-risk acceptance, thresholds, notice and appeal policy.
- `action_delta`: protect guidance adoption, thresholds, people-affecting decisions, notices, and redress workflow changes.
- `anomaly_delta`: controlling-source conflict, new right/population, disparity, capacity breach, override abuse; distinguish rule/source ambiguity, population shift, selective labels, implementation drift, disparate impact, capacity, and override rivals using controlling text, case samples, disparity decomposition, and redress queues.
- `change_impact_delta`: authority/jurisdiction/population/right/data-lifecycle/workflow/threshold changes invalidate applicability, rights, fairness, privacy, notice/redress, throughput, and monitoring evidence.
- `insight_constraints`: an idea cannot create authority or waive notice, redress, fairness, privacy, or override; distinguish source conflict, population shift, capacity, and implementation rivals using controlling text, case samples, and untouched jurisdiction/population review.

## Native V5 Packet

Emit the complete `v5-domain-1` packet from the named domain sections with producer snapshot/fingerprint. The parent router and `../SNAPSHOT.md` own schema and authority rules. Reject unknown top-level fields; optional additions belong only in a namespaced `extensions` map.

## Behavior Tests

| Task | Expected behavior |
| --- | --- |
| Summarize an approved refund policy for internal agents. | Verify controlled version, jurisdiction, scope, and nonbinding output; publication as decision guidance stays blocked if any is unknown. |
| Update marketplace moderation for coordinated false reports. | Require authority, rights, capacity, redress, abuse, fairness, and monitoring proof; unknown appeal or review capacity blocks recommendation and rollout. |
| Build a credit-approval model to reduce manual review cost. | Keep Policy/Governance primary because approval/denial and rights dominate; borrow Tabular ML/Evaluation and Product/Business. Block data expansion, training, thresholds, ROI claims, and rollout until authority, labels, fairness, explanations, appeals, capacity, and monitoring pass. |
| Launch global biometric age assurance that restricts minors' accounts. | Route vision and security/privacy; require region-specific authority hierarchy, children's rights, lifecycle controls, redress, abuse, regional capacity, and change monitoring. Conflicts permit research only. |
