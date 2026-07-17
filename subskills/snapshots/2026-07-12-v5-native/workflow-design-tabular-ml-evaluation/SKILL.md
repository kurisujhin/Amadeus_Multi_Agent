---
name: workflow-design-tabular-ml-evaluation
description: Use with multi-agent-workflow-designer when designing workflows for tabular ML, classifiers, risk scores, lead scoring, churn prediction, fraud models, forecasting baselines, evaluation frameworks, benchmark harnesses, metrics, calibration, thresholds, or claims about model quality. Emphasize label validity, leakage, baselines, calibration, action costs, reproducibility, and monitoring.
---

# Workflow Design: Tabular ML/Evaluation

This domain subskill supplies prediction, scoring, evaluation, and quality-claim deltas to `multi-agent-workflow-designer`. It does not replace the parent workflow.

## Trigger

Use as the primary domain when predictive or evaluation validity is the dominant risk in a classifier, score, benchmark, metric, model comparison, calibration, threshold, or feature workflow. A business, policy, or operations skill should remain primary when the real question is product fit, rights, or operational decisions; borrow this lens for labels, leakage, estimates, calibration, and reproducibility.

## Native V5 Parent Boundary

Emit marginal domain semantics only; the v5 parent owns workflow and effects as defined in `../SNAPSHOT.md`. This skill never issues permits, creates agents, chooses commit mode, resumes pauses, authorizes effects, or mutates canonical state.

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

## Native V5 Domain Delta

- `work_model_delta`: entity-time rows, features, folds, thresholds, slices, runs; joins/materialization/training; label maturity, leakage, overlap, calibration, capacity, hashes and rerun tolerance.
- `human_input_deltas`: label/estimand authority, action costs, threshold authority, target cohort, intervention, operational capacity, and claim type.
- `action_delta`: protect materialization, training, benchmark selection, threshold publication, and intervention.
- `anomaly_delta`: cohort/count/hash drift, label maturity change, leakage, base-rate/calibration/capacity breach; distinguish refresh, selection, maturity, leakage, and code-path rivals using as-of lineage, overlap, raw cases, row/feature/fold/run calibration, and capacity model.
- `change_impact_delta`: label/cohort/as-of/split/feature/metric/threshold/intervention/capacity changes invalidate evaluation, reproducibility, operating point, intervention, and monitoring evidence.
- `insight_constraints`: adaptive discovery cannot consume untouched confirmation or turn prediction into causal/ROI evidence; use as-of raw-case falsifiers and an untouched entity-time split.

## Native V5 Packet

Emit the complete `v5-domain-1` packet from the named domain sections with producer snapshot/fingerprint. The parent router and `../SNAPSHOT.md` own schema and authority rules. Reject unknown top-level fields; optional additions belong only in a namespaced `extensions` map.

## Behavior Tests

| Task | Expected behavior |
| --- | --- |
| Compare two classifiers on a frozen dataset. | Apply `TML-G1`, `TML-G2`, `TML-G3`, `TML-G4`, and `TML-G6`; after protocol and lineage entry proof, allow a narrow benchmark permit while result gates remain due. No winner claim before held-out results and rerun proof. |
| Build lead scoring to improve sales conversion. | Route product/business; treat attribution, sales capacity, contact cost, and cadence as direction-changing. Block training, threshold, and ROI claims until the action and evaluation chain closes. |
| Build a churn model to target retention offers. | Detect offer-altered labels, selective outcomes, post-treatment leakage, capacity limits, causal claim boundaries, and intervention-aware monitoring; AUC alone cannot authorize launch. |
| Deploy multi-region credit approval. | Route policy/governance; require reject-inference limits, delayed defaults, fairness, explanation/appeal, jurisdiction, risk appetite, decision rights, thresholds, sensitive access, and macro-drift evidence before dependent actions. |
