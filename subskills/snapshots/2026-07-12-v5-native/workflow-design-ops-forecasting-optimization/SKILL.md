---
name: workflow-design-ops-forecasting-optimization
description: Use with multi-agent-workflow-designer when designing workflows for operations, forecasting, optimization, routing, scheduling, staffing, inventory, capacity, ETA, demand planning, alert prioritization, predictive maintenance, dispatch, logistics, or cost/latency reduction. Emphasize owner action, constraints, uncertainty, stress cases, override, monitoring, and operational feasibility.
---

# Workflow Design: Ops/Forecasting/Optimization

This domain subskill supplies operational decision, forecast, and optimization deltas to `multi-agent-workflow-designer`. It does not replace the parent workflow.

## Trigger

Use as the primary domain when operational action validity is the dominant risk in demand/capacity/ETA forecasting, inventory, maintenance, staffing, routing, scheduling, dispatch, alerts, queues, logistics, or cost/latency optimization. Use as a borrowed lens whenever another domain produces alerts, predictions, recommendations, or constraints that operators or automation must act on.

## Native V5 Parent Boundary

Emit marginal domain semantics only; the v5 parent owns workflow and effects as defined in `../SNAPSHOT.md`. This skill never issues permits, creates agents, chooses commit mode, resumes pauses, authorizes effects, or mutates canonical state.

## Domain Ledger Additions

- Supported action, accountable owner, cadence, data cutoff, horizon, granularity, lead time, execution window, owner capacity, late/missing fallback, and error costs.
- Hard/soft constraints, authority/effective interval, units, objective terms/weights, infeasible behavior, solver/rule/version, and baseline.
- Forecast vintages, train/tune/test windows, rolling origins, leakage checks, distributions/intervals, asymmetric loss, tails, OOD/missing data, and stress scenarios.
- Operator arrival/service rates, backlog/SLA, adoption/training, explanation, overrides/escalation, unavailable-operator fallback, and audit.
- Comparator, intervention/attribution, exposure/action logs, outcomes/counter-metrics, label delay, monitoring, kill/rollback, in-flight reconciliation, and reentry.

## Domain Gates

| Gate | Pass condition | Required proof |
| --- | --- | --- |
| `OPS-G1` ActionTimingFit | Output is available early and granular enough for an owned action within capacity and a defined execution window. | `OpsDecisionTimingSpec` with action, owner, cadence, cutoff, horizon, granularity, lead time, window, capacity, fallback, and false/late/missed-action costs. |
| `OPS-G2` ConstraintFeasibility | Candidate plans satisfy authoritative hard constraints, expose soft tradeoffs, handle infeasibility, and beat an operational baseline. | `OpsConstraintFeasibilityReport` with constraint class/authority/effective scope/units, objective terms/weight authority, plan/solver version, violations/slack/penalties, infeasible behavior, baseline, and acceptance. |
| `OPS-G3` UncertaintyTailSafety | Forecast or plan uncertainty is calibrated for the action horizon and protects asymmetric loss, tails, OOD, and missing-data cases. | `OpsUncertaintyTailReport` with target/horizon/segment/vintage, distribution/interval method, calibration/coverage, tail quantiles/scenarios, loss, thresholds, sensitivity, OOD behavior, fallback, and acceptance. |
| `OPS-G4` TemporalReplayValidity | Evaluation uses only information available at each decision time, independent rolling origins, valid baselines, stress regimes, and reproducible simulations. | `OpsTemporalReplayReport` with cutoffs/as-of vintages, windows/splits, leakage, metrics by horizon/segment/regime, costs, stress cases, assumptions, constraint violations, seeds/versions, and acceptance. |
| `OPS-G5` OperatorCapacityOverride | Human or automated consumers can process expected load, understand inputs, override/escalate, audit exceptions, and fall back safely. | `OpsOperatorControlPlan` with roles, arrival/service capacity, SLA/backlog, adoption/training, explanation inputs, override modes, escalation, logs, fallback, and drill result. |
| `OPS-G6` OutcomeValidation | Claimed operational/business improvement has a prespecified comparator, attribution design, logs, measurement window, uncertainty, counter-metrics, and decision rule. | `OpsOutcomeValidationProtocol`; after action, `OpsOutcomeValidationReport` with adherence, results/uncertainty, slices, harms, and decision. |
| `OPS-G7` MonitoringRollback | Input freshness, drift, calibration, feasibility, SLO, operator load, adoption, outcomes, and counter-metrics have authoritative triggers, owners, safe fallback, reconciliation, and reentry. | `OpsMonitoringRollbackRunbook` with signals, threshold authority, detection/response latency, alert/rollback authority, last known good, fallback, in-flight reconciliation, drill evidence, and reentry criteria. |

## Safe Start And Protected Actions

Before an execution permit, safe start is limited to read-only source/lineage/schema inventory, existing-baseline reproduction, descriptive profiling, and cost-capped sandbox replay or solver checks on synthetic, redacted, or approved frozen samples. Outputs remain explicitly non-operational.

Keep sensitive or broad production extraction, model training, costly optimization/simulation, shadow/pilot/online experiments, publishing into operator workflows, changing dispatch/routes/schedules/staffing/inventory/orders/capacity/alerts, reserving resources, notifying external parties, rollout/rollback, and final recommendation blocked until their action-stage gates pass. Emergency rollback is allowed only through an exact pre-authorized trigger and owner.

When costly simulation is required to produce `OPS-G2`, `OPS-G3`, or `OPS-G4` result evidence, use a narrow parent `validation` permit only after simulation authorization, data/environment scope, authoritative constraints and horizon, resource/cost cap, protocol, seeds, oracles, and stop/recovery controls pass as entry proof. Put the three reports under `result_gates_due`; keep operational recommendations, pilots, workflow publication, rollout, and final claims blocked.

## Review Perspectives

- Operations/domain action, timing, and capacity.
- Forecasting, temporal evaluation, uncertainty, and tail risk.
- Constraints, optimization, infeasibility, and simulation.
- Reliability/SLO, monitoring, fallback, and rollback.
- Product, finance, policy, safety, privacy, or security expertise when interventions affect people, money, regulated services, or trust.

## Borrowed Lenses

- `workflow-design-tabular-ml-evaluation` for labels, time leakage, calibration, thresholds, and reproducibility.
- `workflow-design-product-business-decision` for ROI, adoption, decision quality, and tradeoff authority.
- `workflow-design-software-reliability` for deployment, queues, observability, incident readiness, and graceful degradation.
- `workflow-design-policy-governance` for medical/safety/student routing or other high-impact intervention.

## Simplification Rules

- `OPS-G1` applies to every operational recommendation. `OPS-G2` applies to constrained decisions; `OPS-G3` to uncertain inputs/outputs; `OPS-G4` to empirical, heuristic, learned, repeated, or consequential decisions; `OPS-G5` when humans or automation consume output; `OPS-G6` when improvement is claimed; `OPS-G7` for pilots, recurring use, or live operation.
- Low-risk, reversible, single-scope work may combine all applicable proof into one compact packet and combine compatible perspectives. Gate IDs and decisions remain distinct.
- Scope expansion invalidates prior `not_applicable` records. Live/multisite/high-cost/tail/people/safety/delayed-outcome/difficult-rollback work requires expanded proof.
- The parent alone decides runtime separation and whether a direct path is valid.

## Blocking Failure Modes

Return `fail|escalate` when average accuracy hides wrong action timing, retrospective data leaks future information, constraints or tail cases are untested, operator capacity/override is missing, or monitoring covers model quality without operational outcomes and recovery.

## Native V5 Domain Delta

- `work_model_delta`: entity×horizon×scenario, solver iterations, routes/jobs/SKUs; vintage scans, simulations, constraint/solver complexity; feasibility, slack, tail coverage, action-window progress.
- `human_input_deltas`: objective weights, hard constraints, horizon, cadence/cutoff/lead time, capacity, execution window, risk tolerance, fallback/rollback authority, and override owner.
- `action_delta`: protect costly simulation, published plans, reservations, dispatch, and operational pointer changes.
- `anomaly_delta`: infeasibility, as-of leakage, missed window, tail/calibration breach, backlog/override spike; distinguish demand/regime, constraint/objective, data-vintage, solver-scaling, and operator-capacity rivals using constraint cores, vintage lineage, stress slices, and capacity ledgers.
- `change_impact_delta`: objective/constraint/horizon/capacity/vintage/solver changes invalidate feasibility, replay, stress/tail, override, and outcome evidence.
- `insight_constraints`: freeze objective, constraints, as-of vintage, and action window; distinguish demand, constraint, data-vintage, solver, and capacity rivals with feasibility/stress falsifiers and untouched future-vintage confirmation.

## Native V5 Packet

Emit the complete `v5-domain-1` packet from the named domain sections with producer snapshot/fingerprint. The parent router and `../SNAPSHOT.md` own schema and authority rules. Reject unknown top-level fields; optional additions belong only in a namespaced `extensions` map.

## Behavior Tests

| Task | Expected behavior |
| --- | --- |
| Reorder three sandbox batch jobs under fixed windows. | Retrieve objective/deadline authority, runtime variability, dependencies, and one-off versus recurring scope; replay safely with timing, constraints, and temporal proof. An actual scheduler edit remains protected. |
| Forecast next-day bakery demand and prep quantities. | Keep Ops primary when forecast/prep feasibility and execution dominate; make Product primary only for a launch/economics decision. Require waste/stockout weights, lead time, calibrated tails, holiday replay, capacity, outcome pilot, and fallback. |
| Allocate retail inventory across hundreds of stores. | Route product and reliability; require source `observed_at`/effective intervals/invalidation triggers, as-of vintages, constraints, infeasibility and disruption tests, planner capacity, outcome counter-metrics, and order rollback. |
| Recommend grid dispatch during heat waves. | Route reliability and policy/safety; require current source timestamps/invalidation triggers, network/outage constraints, probabilistic peak tails, contingency simulation, reserve authority, operator drills, outcome counter-metrics, and safe-state recovery. Missing risk tolerance or authority blocks dispatch commitment. |
