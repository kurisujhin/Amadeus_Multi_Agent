---
name: workflow-design-tabular-ml-evaluation
description: Use with multi-agent-workflow-designer when designing workflows for tabular ML, classifiers, risk scores, lead scoring, churn prediction, fraud models, forecasting baselines, evaluation frameworks, benchmark harnesses, metrics, calibration, thresholds, or claims about model quality. Emphasize label validity, leakage, baselines, calibration, action costs, reproducibility, and monitoring.
---

# Workflow Design: Tabular ML/Evaluation

This domain subskill supplies prediction, scoring, evaluation, and quality-claim deltas to `multi-agent-workflow-designer`. It does not replace the parent workflow.

## Trigger

Use as the primary domain when predictive or evaluation validity is the dominant risk in a classifier, score, benchmark, metric, model comparison, calibration, threshold, or feature workflow. A business, policy, or operations skill should remain primary when the real question is product fit, rights, or operational decisions; borrow this lens for labels, leakage, estimates, calibration, and reproducibility.

## Parent Contract

- The parent owns real-subagent creation, runtime DAG and budgets, ledgers, execution feedback, observer/reviewer separation, permits, protected-action dispatch, mutation ownership, insight validation, synthesis, and final acceptance.
- Review perspectives below are competencies, never real or virtual agents. The parent maps them to real runtime owners.
- Each gate record needs `gate_id`, `action_stage`, `proof_phase=entry|result`, `applicability=applicable|not_applicable|unresolved`, and `applicability_evidence_refs`. Only `applicable` gates receive `decision=pass|fail|escalate`, with evidence and blocked commitments; `not_applicable` needs positive scope evidence and a reopen trigger, while `unresolved` blocks.
- Source claims need authority, effective version/date, exact cohort/product/region applicability, `observed_at`, and `valid_until` or refresh trigger. Stale, conflicting, or unavailable high-impact evidence remains blocking.
- Unknowns that could change target, cohort, label, split, action, metric, threshold, cost, capacity, owner, intervention, schedule, or scope cannot authorize execution or be invented.

## Domain Ledger Additions

- Supported action, decision owner/cadence, affected population, current workflow, capacity, adoption/intervention path, and false-positive/false-negative costs.
- Entity key, unit, eligibility, index/prediction time, feature cutoff/lookback, outcome window, label rule/source/version, maturity, censoring, selection, and deduplication.
- Feature event/availability time and as-of rule; split time/unit; entity/duplicate overlap; preprocessing fit scope.
- Estimands, baselines, metrics, comparison margin, uncertainty, slices, multiplicity, calibration, threshold, and guardrails.
- Dataset/code/environment/config/run lineage, intervention assumptions, monitoring, retraining, disable, and rollback.

## Domain Gates

| Gate | Pass condition | Required proof |
| --- | --- | --- |
| `TML-G1` ActionFit | Prediction or metric supports an owned action at a defined cadence with capacity, costs, success metrics, and counter-metrics. | `ActionFitProof` with action, owner, population, workflow/baseline, cadence, capacity, FP/FN costs, constraints, metrics, and adoption/intervention path. |
| `TML-G2` CohortLabel | Entity-time cohort and label represent the intended outcome without immature, censored, duplicated, or selectively observed distortion. | `EntityTimeLabelProof` with entity/unit, eligibility, index time, cutoffs/windows, rule/source/version, maturity, censoring, missingness, selection bias, dedup/linkage, policy provenance, and counts. |
| `TML-G3` LeakageSplit | Features and preprocessing obey production availability and splits prevent temporal, identity, duplicate, target, post-outcome, and post-treatment leakage. | `LeakageSplitProof` with feature source/event/availability/as-of inventory, prohibited features, split time/unit, overlaps, preprocessing scope, train/serve checks, and test results. |
| `TML-G4` BaselineEvaluation | A prespecified held-out evaluation estimates decision-relevant metrics against current, naive, and simple baselines with uncertainty and slices. | `EvaluationProtocol` plus `EvaluationResultReport` containing estimands, metrics, partitions, baselines, margin, multiplicity, dataset snapshot, counts, estimates/intervals, slices, deltas, and failed assumptions. |
| `TML-G5` CalibrationThreshold | Probabilities and operating points remain valid under base-rate uncertainty and fit action cost, fairness, volume, and capacity. | `OperatingPointProtocol` plus `OperatingPointReport` with calibration split/method, base rate, candidate rules, confusion counts by volume/slice, expected cost/utility, capacity load, sensitivity, guardrails, and owner evidence. |
| `TML-G6` UncertaintyReproducibility | Results rerun from immutable data/code/environment/config with justified uncertainty and bounded numerical variation. | `ReproducibilityProof` with dataset/query hashes, revisions, commit/environment lock, config/seeds, partitions, run IDs/artifact hashes, interval method, rerun command/tolerance/result. |
| `TML-G7` InterventionEffect | Predictive, causal, and ROI claims are separated; treatment, selective labels, policy changes, and feedback loops are identified or bounded. | `InterventionEffectProof` with claim type, assignment mechanism, prior exposure, post-treatment controls, policy changes, feedback channels, identification assumptions, holdout/experiment, contamination, and scope limits. |
| `TML-G8` MonitoringRollback | Delayed labels, data/prediction/performance/calibration drift, action volume/capacity, realized outcomes, and intervention effects have owners and recovery. | `MonitoringRollbackProof` with reference windows, maturity lag, metrics/slices, drift, capacity, realized cost/yield, alert rules/authority, runbook, retrain/disable/rollback, and audit retention. |

Gate decisions are action-stage specific. For a benchmark, approved `EvaluationProtocol` and reproducibility entry controls may support a narrow `validation` permit; `EvaluationResultReport` and rerun result remain result proof due before a winner or quality claim. Use `result_gates_due`, never `not_applicable`, for evidence the permitted action has not produced yet. Apply the same entry/result split to materialization, training, thresholding, intervention, and deployment.

## Safe Start And Protected Actions

Before an execution permit, safe start is limited to read-only source/lineage mapping, schema and timestamp inspection, synthetic checks, bounded profiling of already-authorized data, and protocol drafting with unknowns marked `TBD`. These actions make no model-quality, causal, or business-impact claim.

Keep sensitive extraction, shared cohort/label materialization, training/tuning, benchmark runs, model selection, quality claims, threshold commitments, causal/ROI recommendations, interventions, production monitoring changes, retraining, and rollout blocked until the parent permits the action and applicable gates pass on the same snapshot.

## Review Perspectives

- Entity-time cohort, label, and data validity.
- Leakage, split, and train/serve validity.
- Statistical evaluation, uncertainty, and reproducibility.
- Calibration, action cost, capacity, and intervention effects.
- Fairness, privacy, policy, finance, operations, or domain expertise for consequential scores.

## Borrowed Lenses

- `workflow-design-product-business-decision` for workflow fit, adoption, ROI, or recommendation quality.
- `workflow-design-policy-governance` for eligibility, approval/denial, fraud, education, health, hiring, finance, or appeals.
- `workflow-design-ops-forecasting-optimization` for forecast horizons, capacity, scheduling, inventory, dispatch, and intervention planning.
- `workflow-design-software-reliability` for production pipelines, feature stores, CI/CD, observability, and rollback.
- `workflow-design-security-privacy` for sensitive financial/PII extraction, access, retention, and fraud-model abuse.

## Simplification Rules

- `TML-G1` through `TML-G4` and `TML-G6` apply to every training or comparative quality claim.
- `TML-G5` is `not_applicable` only when no probability, cutoff, prioritization, or capacity allocation is used. `TML-G7` is `not_applicable` only for a strictly predictive, non-actioned analysis that excludes causal and ROI claims. `TML-G8` is `not_applicable` only for a one-off immutable analysis with no repeated decision loop.
- Moderate work may combine proofs into one compact review bundle and combine compatible perspectives, but gate semantics and evidence decisions remain distinct.
- Simplification never weakens parent permits, real-agent requirements, observer duties, source closure, or final synthesis.

## Blocking Failure Modes

Block the affected commitment when action fit, entity-time labels, leakage, baseline, uncertainty, threshold capacity, intervention assumptions, or reproducibility are unresolved; when historical policy labels are accepted as truth without review; or when AUC/accuracy is treated as business impact.

## V4 Runtime Handoff

Return marginal deltas to v4. Barriers are cohort/label materialization, split lock, held-out evaluation, operating-point selection, and deployment review. Emit parent feedback for label-maturity or cohort-count drift, leakage discovery, dataset/split/hash change, calibration/base-rate/capacity breach, invalid uncertainty, or intervention feedback. Map affected gates, result claims, permits, and rerun boundary. An unexpected feature, transform, threshold, or estimand is an `InsightCandidate`; freeze availability/label semantics, leakage rivals, cheapest as-of falsifier, locked evaluation boundary, baseline, and contamination. Adaptive discovery cannot consume untouched confirmation or convert prediction into causal/ROI evidence.

## Domain Gate Packet

```text
DomainGatePacket:
  parent_contract_version: v4
  packet_domain: Tabular ML/Evaluation
  routing_role: primary|borrowed
  primary_domain: set by parent
  route_reason: dominant validity/risk or marginal domain delta
  marginal_gate_delta: [question, gate, proof, trigger, or protected action changed]
  omit_or_exception_reason: [plausible lens omitted or default-two exception]
  ledger_additions: [field=value ...]
  knowledge_sources: [source, authority, effective_version, observed_at, applicability, valid_until_or_trigger, status]
  freshness_required: [claim -> freshness rule]
  retrieval_status: complete|partial|blocked
  required_questions: [direction-changing unknown -> owner]
  reviewers: [perspective -> real runtime owner assigned by parent]
  domain_gates: [gate_id, action_stage, proof_phase, applicability, applicability_evidence_refs, decision, evidence_required, evidence_refs, open_gap_ids, blocked_commitments, required_change, reopen_or_invalidation_trigger]
  shared_evidence_refs: [artifact -> consuming domain gates]
  runtime_handoff: [semantic_barriers, anomaly_triggers, max_unchecked_interval_or_NA, direct_evidence_refs, safe_stop_state, observer_authority, affected_gate_proof_permit_descendants]
  insight_constraints: [protected_invariants, cheapest_falsifier, confirmation_boundary, contamination]
  handoff_status: ready|partial|blocked
  validation_artifacts: [stable artifact refs]
  borrowed_lenses: [skill -> reason]
  stop_conditions: [concrete stop, invalidation, or escalation trigger]
  simplification_triggers: [gate -> applicability evidence and residual limits]
```

## Behavior Tests

| Task | Expected behavior |
| --- | --- |
| Compare two classifiers on a frozen dataset. | Apply `TML-G1`, `TML-G2`, `TML-G3`, `TML-G4`, and `TML-G6`; after protocol and lineage entry proof, allow a narrow benchmark permit while result gates remain due. No winner claim before held-out results and rerun proof. |
| Build lead scoring to improve sales conversion. | Route product/business; treat attribution, sales capacity, contact cost, and cadence as direction-changing. Block training, threshold, and ROI claims until the action and evaluation chain closes. |
| Build a churn model to target retention offers. | Detect offer-altered labels, selective outcomes, post-treatment leakage, capacity limits, causal claim boundaries, and intervention-aware monitoring; AUC alone cannot authorize launch. |
| Deploy multi-region credit approval. | Route policy/governance; require reject-inference limits, delayed defaults, fairness, explanation/appeal, jurisdiction, risk appetite, decision rights, thresholds, sensitive access, and macro-drift evidence before dependent actions. |

## Runtime Enforcement

The parent must evaluate each applicable gate as `pass|fail|escalate` against named evidence refs; prose that merely mentions a concern is not proof. Every `fail|escalate` record must list the protected action it blocks, the owner of the missing evidence, and the reopen trigger. `N/A` requires positive applicability evidence and a residual-limit statement. Require data-access proof before profiling, locked evaluation after adaptive tuning, and an operational stress/fallback proof before deployment.

## Self-Improvement Hook

After a task, emit a `DomainSkillUpdateCandidate` only when evidence shows a recurring missing trigger, leakage/label pattern, gate, perspective, or failure mode. Include task evidence and one failing-then-passing behavior test. Do not mutate the installed skill unless the user requested or approved improvement.
