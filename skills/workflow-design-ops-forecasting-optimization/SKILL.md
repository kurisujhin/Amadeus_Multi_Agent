---
name: workflow-design-ops-forecasting-optimization
description: Use with multi-agent-workflow-designer when designing workflows for operations, forecasting, optimization, routing, scheduling, staffing, inventory, capacity, ETA, demand planning, alert prioritization, predictive maintenance, dispatch, logistics, or cost/latency reduction. Emphasize owner action, constraints, uncertainty, stress cases, override, monitoring, and operational feasibility.
---

# Workflow Design: Ops/Forecasting/Optimization

This domain subskill supplies operational decision, forecast, and optimization deltas to `multi-agent-workflow-designer`. It does not replace the parent workflow.

## Trigger

Use as the primary domain when operational action validity is the dominant risk in demand/capacity/ETA forecasting, inventory, maintenance, staffing, routing, scheduling, dispatch, alerts, queues, logistics, or cost/latency optimization. Use as a borrowed lens whenever another domain produces alerts, predictions, recommendations, or constraints that operators or automation must act on.

## Parent Contract

- The parent owns real-subagent creation, runtime DAG and budgets, ledgers, execution feedback, observer/reviewer separation, permits, protected-action dispatch, mutation ownership, insight validation, synthesis, and final acceptance.
- Review perspectives below are competencies, never real or virtual agents. The parent maps them to real runtime owners.
- Each gate record needs `gate_id`, `action_stage`, `proof_phase=entry|result`, `applicability=applicable|not_applicable|unresolved`, and `applicability_evidence_refs`. Only `applicable` gates receive `decision=pass|fail|escalate`, with evidence and blocked commitments; `not_applicable` needs positive scope evidence and a reopen trigger, while `unresolved` blocks.
- Operational facts need authority, `observed_at`, effective interval, site/region/asset/SKU/shift/units/horizon applicability, lineage/reconciliation, conflicts, and refresh or invalidation trigger.
- Unknown owner, horizon, lead time, capacity, hard constraint, objective weight, tail-risk tolerance, threshold, schedule, or deployment scope cannot authorize a commitment or be invented. A bounded assumption may support only a reversible falsification probe.

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

## V4 Runtime Handoff

Return marginal deltas to v4. Barriers precede costly simulation, shadow/pilot, operator publication, resource reservation, and dispatch. Emit parent feedback for infeasibility/constraint violation, as-of leakage, tail/calibration breach, missed action window, operator backlog/override spike, stale input, or counter-metric harm. Safe stop names last-known-good/manual fallback and in-flight reconciliation. A novel forecast, objective, or policy is only an `InsightCandidate`; falsify by as-of replay and stress regimes under frozen objectives/constraints, then untouched confirmation. No idea may relax a hard constraint or change the objective post hoc.

## Domain Gate Packet

```text
DomainGatePacket:
  parent_contract_version: v4
  packet_domain: Ops/Forecasting/Optimization
  routing_role: primary|borrowed
  primary_domain: set by parent
  route_reason: dominant validity/risk or marginal domain delta
  marginal_gate_delta: [question, gate, proof, trigger, or protected action changed]
  omit_or_exception_reason: [plausible lens omitted or default-two exception]
  ledger_additions: [field=value ...]
  knowledge_sources: [source, authority, effective_interval, observed_at, operational_scope, lineage_reconciliation, conflicts, refresh_trigger, status]
  freshness_required: [claim -> usable action interval or change trigger]
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
  simplification_triggers: [gate -> positive applicability evidence and residual limits]
```

## Behavior Tests

| Task | Expected behavior |
| --- | --- |
| Reorder three sandbox batch jobs under fixed windows. | Retrieve objective/deadline authority, runtime variability, dependencies, and one-off versus recurring scope; replay safely with timing, constraints, and temporal proof. An actual scheduler edit remains protected. |
| Forecast next-day bakery demand and prep quantities. | Route product/business; require waste/stockout weights, prep lead time, calibrated tails, holiday replay, manager capacity, outcome pilot, and manual fallback. Unknown weights block deployment-directed training, model choice, and pilot. |
| Allocate retail inventory across hundreds of stores. | Route product and reliability; require source `observed_at`/effective intervals/invalidation triggers, as-of vintages, constraints, infeasibility and disruption tests, planner capacity, outcome counter-metrics, and order rollback. |
| Recommend grid dispatch during heat waves. | Route reliability and policy/safety; require current source timestamps/invalidation triggers, network/outage constraints, probabilistic peak tails, contingency simulation, reserve authority, operator drills, outcome counter-metrics, and safe-state recovery. Missing risk tolerance or authority blocks dispatch commitment. |

## Runtime Enforcement

The parent must evaluate each applicable gate as `pass|fail|escalate` against named evidence refs; prose that merely mentions a concern is not proof. Every `fail|escalate` record must list the protected action it blocks, the owner of the missing evidence, and the reopen trigger. `N/A` requires positive applicability evidence and a residual-limit statement. A mathematically optimal plan cannot authorize execution without feasibility, operator capacity, tail-risk, fallback, and rollback evidence.

## Self-Improvement Hook

After a task, emit a `DomainSkillUpdateCandidate` only when evidence shows a recurring missing trigger, gate, perspective, stress case, or failure mode. Include task evidence and one failing-then-passing behavior test. Do not mutate the installed skill unless the user requested or approved improvement.
