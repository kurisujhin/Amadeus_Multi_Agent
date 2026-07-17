---
name: workflow-design-policy-governance
description: Use with multi-agent-workflow-designer when designing workflows for policy, governance, moderation, approval/denial, eligibility, appeals, audits, fairness, compliance, fraud/risk, safety, or high-impact people-affecting systems in domains such as finance, health, education, hiring, refunds, workplace, or content enforcement. Emphasize stakeholders, rights, appeal, auditability, fairness, privacy, enforceability, and human override.
---

# Workflow Design: Policy/Governance

This domain subskill supplies policy and governance deltas to `multi-agent-workflow-designer`. It does not replace the parent workflow.

## Trigger

Use as the primary domain when policy validity, rights, enforcement, or governance risk dominates: moderation, eligibility, approval/denial, appeals, audit, compliance, fraud/risk, safety, workforce, education, health, finance, housing, hiring, refunds, or public-impact decisions. Use as a borrowed lens whenever an artifact can materially affect rights, access, opportunity, safety, reputation, money, or enforcement.

## Parent Contract

- The parent owns real-subagent creation, runtime DAG and budgets, ledgers, execution feedback, observer/reviewer separation, permits, protected-action dispatch, mutation ownership, insight validation, synthesis, and final acceptance.
- Review perspectives below are competencies, never real or virtual agents. The parent assigns required perspectives to real runtime owners.
- Each gate record needs `gate_id`, `action_stage`, `proof_phase=entry|result`, `applicability=applicable|not_applicable|unresolved`, and `applicability_evidence_refs`. Only `applicable` gates receive `decision=pass|fail|escalate`, with evidence and blocked commitments; `not_applicable` needs positive scope evidence and a reopen trigger, while `unresolved` blocks.
- Binding claims need controlling authority, jurisdictional and temporal applicability, hierarchy, version, conflicts, and retrieval status. Operational evidence can prove feasibility but cannot create authority.
- Unresolved jurisdiction, authority, effective date, hierarchy, population, owner, capacity, threshold, appeal obligation, schedule, or rollout scope cannot authorize a commitment or be invented.

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

## V4 Runtime Handoff

Return marginal deltas to v4. Barriers precede published guidance, threshold adoption, people-affecting action, notices, and rollout. Emit parent feedback for controlling-source/jurisdiction conflict, newly affected population/right, unexplained disparity, appeal/complaint surge, capacity breach, or override abuse. Authority, rights, and safety drift require binding pause; a separate reviewer judges interpretation and impact. A novel policy mechanism is only an `InsightCandidate`: it cannot create authority or waive notice, redress, privacy, fairness, or human override. Evaluate all gates and pass every applicable gate; a lens-count default never suppresses a distinct safety-critical lens.

## Domain Gate Packet

```text
DomainGatePacket:
  parent_contract_version: v4
  packet_domain: Policy/Governance
  routing_role: primary|borrowed
  primary_domain: set by parent
  route_reason: dominant validity/risk or marginal domain delta
  marginal_gate_delta: [question, gate, proof, trigger, or protected action changed]
  omit_or_exception_reason: [plausible lens omitted or default-two exception]
  ledger_additions: [field=value ...]
  knowledge_sources: [source, authority_class, jurisdiction, version_dates, observed_at, applicability, conflicts, status]
  freshness_required: [claim -> validity or event recheck]
  retrieval_status: complete|partial|blocked
  required_questions: [direction-changing unknown -> empowered owner]
  reviewers: [perspective -> real runtime owner assigned by parent]
  domain_gates: [gate_id, action_stage, proof_phase, applicability, applicability_evidence_refs, decision, evidence_required, evidence_refs, open_gap_ids, blocked_commitments, required_change, reopen_or_invalidation_trigger]
  shared_evidence_refs: [artifact -> consuming domain gates]
  runtime_handoff: [semantic_barriers, anomaly_triggers, max_unchecked_interval_or_NA, direct_evidence_refs, safe_stop_state, observer_authority, affected_gate_proof_permit_descendants]
  insight_constraints: [protected_invariants, cheapest_falsifier, confirmation_boundary, contamination]
  handoff_status: ready|partial|blocked
  validation_artifacts: [stable artifact refs]
  borrowed_lenses: [skill -> distinct marginal value]
  stop_conditions: [concrete stop, invalidation, or escalation trigger]
  simplification_triggers: [gate -> applicability evidence and recheck]
```

## Behavior Tests

| Task | Expected behavior |
| --- | --- |
| Summarize an approved refund policy for internal agents. | Verify controlled version, jurisdiction, scope, and nonbinding output; publication as decision guidance stays blocked if any is unknown. |
| Update marketplace moderation for coordinated false reports. | Require authority, rights, capacity, redress, abuse, fairness, and monitoring proof; unknown appeal or review capacity blocks recommendation and rollout. |
| Build a credit-approval model to reduce manual review cost. | Keep Tabular ML/Evaluation primary and borrow Policy/Governance plus Product/Business. Block data expansion, training, thresholds, ROI claims, and rollout until authority, labels, fairness, explanations, appeals, capacity, and monitoring pass. |
| Launch global biometric age assurance that restricts minors' accounts. | Route vision and security/privacy; require region-specific authority hierarchy, children's rights, lifecycle controls, redress, abuse, regional capacity, and change monitoring. Conflicts permit research only. |

## Runtime Enforcement

The parent must evaluate each applicable gate as `pass|fail|escalate` against named evidence refs; prose that merely mentions a concern is not proof. Every `fail|escalate` record must list the protected action it blocks, the owner of the missing evidence, and the reopen trigger. `N/A` requires positive applicability evidence and a residual-limit statement. An undated or non-authoritative policy source cannot authorize eligibility, enforcement, rollout, or user-impacting action.

## Self-Improvement Hook

After a task, emit a `DomainSkillUpdateCandidate` only when evidence shows a recurring missing trigger, gate, perspective, or failure mode. Include task evidence and one failing-then-passing behavior test. Do not mutate the installed skill unless the user requested or approved improvement.
