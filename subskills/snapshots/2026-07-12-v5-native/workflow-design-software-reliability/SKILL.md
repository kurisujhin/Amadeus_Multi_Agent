---
name: workflow-design-software-reliability
description: Use with multi-agent-workflow-designer when designing workflows for software architecture, refactors, migrations, distributed systems, API/config/schema compatibility, incident analysis, flaky tests, reliability, latency, SLOs, observability, rollout, rollback, capacity, or production operations. Emphasize impact maps, compatibility contracts, test matrices, canaries, observability, and incident readiness.
---

# Workflow Design: Software/Reliability

This domain subskill supplies software compatibility, integrity, and recovery deltas to `multi-agent-workflow-designer`. It does not replace the parent workflow.

## Trigger

Use as the primary domain when software compatibility, availability, data integrity, or recovery is the dominant risk in architecture, refactors, migrations, public API/config/schema/event changes, distributed systems, incidents, flaky failures, SLOs, observability, rollout, or rollback. Use as a borrowed lens when another domain must become a reliable service or pipeline. Capacity or incident vocabulary alone does not decide routing.

## Native V5 Parent Boundary

Emit marginal domain semantics only; the v5 parent owns workflow and effects as defined in `../SNAPSHOT.md`. This skill never issues permits, creates agents, chooses commit mode, resumes pauses, authorizes effects, or mutates canonical state.

## Domain Ledger Additions

- Workspace fingerprint, dirty/in-flight state, deployed versions, services/modules/jobs/data, direct/indirect consumers, owners, dependency/data-flow edges, and blast radius.
- Current/target API, schema, config, event, CLI, file, and storage contracts; producer/consumer version skew and transition constraints.
- Migration preconditions, states/invariants, phase order, dual read/write, replay/backfill, idempotency, reconciliation, cutover, abort, rollback/forward recovery, and irreversibility.
- Failure signatures/hypotheses, test levels/environments/oracles, load/fault profiles, residual gaps, rollout cohorts, and recovery evidence.
- SLI/SLO/error budget, latency distribution, demand bursts, quotas/headroom, observability, data integrity, on-call, runbooks, authority, and communications.

## Domain Gates

| Gate | Pass condition | Required proof |
| --- | --- | --- |
| `SR-G1` CurrentImpact | The current workspace/deployed state, mutable work, consumers, owners, dependencies, and blast radius are current, with no unowned high-impact edge. | `CurrentStateImpactMap` with fingerprints, deployed versions by environment, modules/services/jobs/data, direct/indirect consumers, dependency/data-flow edges, owners, blast radius, and unknown edges. |
| `SR-G2` ContractCompatibility | Current and target contracts support required backward, forward, coexistence, read/write, and rollback semantics across actual producer/consumer versions. | `ContractCompatibilityMatrix` with surface/kind, contract refs, versions, defaults/unknown fields/validation, compatibility modes, transition constraints, and contract-test refs. |
| `SR-G3` MigrationIntegrity | Migration invariants are testable and version skew, replay, reconciliation, cutover, abort, and recovery are feasible. | `MigrationIntegrityPlan` with preconditions, states/invariants, phase dependencies, coexistence, backfill/replay/idempotency/ordering, dual paths, reconciliation, criteria, abort, rollback/forward recovery, owners, and rehearsal refs. |
| `SR-G4` FailureValidation | Tests target stable failure hypotheses with explicit oracles at the levels and environments warranted by risk. | `FailureHypothesisTestMatrix` with signature, mechanism, slice, changed variable, test level, environment/data, fault/load profile, oracle, expected/result refs, coverage gaps, and residual risk. |
| `SR-G5` RolloutRecovery | Stages, cohorts, dependency order, entry/exit, signals, abort authority, state recovery, and rollback/forward-fix meet accepted recovery targets. | `RolloutRecoveryPlan` with release unit, stages/cohorts, criteria, guardrail refs, abort authority, disable/rollback, restore/reconciliation, recovery-time evidence, forward fix, rehearsal, and owner. |
| `SR-G6` ServiceReadiness | SLI/SLO/error budget, baseline, latency, peak/burst demand, quotas, capacity/headroom, integrity checks, observability, and alert ownership are evidenced. | `ServiceReadinessEnvelope` with formula/source, windows, distributions, demand/resource model, load refs, failure-to-signal map, log/metric/trace/dashboard/alert refs, integrity checks, and owners. |
| `SR-G7` IncidentOwnership | Current reachable owners have explicit deploy, abort, rollback, incident-command, access, escalation, and communication authority with exercised runbooks. | `IncidentOwnershipRecord` with change/deploy/rollback roles, on-call ref, commander rule, runbook, detection-to-recovery, targets, access, dependency contacts, handoff, communications, and exercise ref. |

## Safe Start And Protected Actions

Before an execution permit, safe start is limited to authorized read-only repository/worktree/deployment inspection, dependency/consumer inventory, contract/config/schema comparison, bounded telemetry/catalog retrieval, and isolated local builds/tests/falsification probes with no shared write, production traffic, sensitive-data expansion, or material cost.

Keep code/config/contract mutations; migrations, backfills, replays, or dual writes; shared-environment tests; load/fault injection; deploys, canaries, flags, traffic shifts, scaling, restart/failover/rollback; SLO/alert/on-call changes; external communications; and final go/no-go recommendations blocked until their action-stage gates pass.

When shared rehearsal, load, fault, or recovery testing is required to produce `SR-G5` or `SR-G6` result evidence, use a narrow parent `validation` permit after authorization, isolation, limits, oracles, stop/recovery conditions, and entry gates pass. Keep rollout and final readiness claims blocked under `result_gates_due`.

## Review Perspectives

- Current architecture, dependency, and impact mapping.
- Contract, schema, config, and migration compatibility.
- Failure hypotheses, test validity, and data integrity.
- SRE, service capacity, observability, rollout, and recovery.
- Security, privacy, data, product, policy, or domain expertise where the change affects those risks.

## Borrowed Lenses

- `workflow-design-security-privacy` for auth, access, secrets, PII, abuse, threats, and compliance.
- `workflow-design-tabular-ml-evaluation` for ML pipelines, feature stores, evaluation reproducibility, and model monitoring.
- `workflow-design-product-business-decision` when changes alter user workflow, product behavior, economics, or business risk.
- `workflow-design-ops-forecasting-optimization` for operational decisions, capacity allocation, queues, scheduling, and SLO tradeoffs.

## Simplification Rules

- `SR-G1` and `SR-G4` always apply to an executable software change or final recommendation.
- Contract, migration, rollout, service, and incident gates apply when their boundary or operational predicate is present. A current map proving a predicate absent may support `not_applicable`; missing investigation cannot.
- A simple local change may combine evidence into one compact `ReliabilityProof`, but every gate keeps an applicability record and proof reference.
- Simplification does not waive parent permits, real-agent requirements, observer/restart duties, source closure, or synthesis.

## Blocking Failure Modes

Return `fail|escalate` when shared-surface impact, contracts, invariants, test oracles, recovery, service evidence, or current ownership is unresolved; when local happy-path tests stand in for distributed validation; or when retries/timeouts replace a stable failure hypothesis without changed evidence.

## Native V5 Domain Delta

- `work_model_delta`: consumers/contracts/versions, migration records/partitions, requests/cohorts; dependency traversal, retries/reconciliation; skew, invariants, SLO/capacity, rollout progress.
- `human_input_deltas`: compatibility promise, recovery target, abort authority, rollout scope, maintenance window, and canonical-pointer authority.
- `action_delta`: protect shared test/mutation, migrations, traffic shifts, deployment, rollback, and publication of canonical build state.
- `anomaly_delta`: new consumer, contract mismatch, invariant failure, rising unit cost/repeated work, idle intended resources, telemetry blind spot, guardrail/recovery miss; distinguish workload scaling, dependency latency, lock contention, retry amplification, instrumentation error, and code-path rivals using code/dataflow, profiles, reconciliation, and dependency maps.
- `change_impact_delta`: API/schema/config/dependency/deployment changes invalidate impact, compatibility, migration, rollout, readiness, and descendant tests/evidence.
- `insight_constraints`: preserve compatibility, invariants, rollback, and stable failure signature; a retry/timeout increase is not a fix without causal evidence; falsify with contract/replay/reconciliation and confirm through bounded canary/recovery evidence.

## Native V5 Packet

Emit the complete `v5-domain-1` packet from the named domain sections with producer snapshot/fingerprint. The parent router and `../SNAPSHOT.md` own schema and authority rules. Reject unknown top-level fields; optional additions belong only in a namespaced `extensions` map.

## Behavior Tests

| Task | Expected behavior |
| --- | --- |
| Extract a private helper in one module. | Repository inspection, a compact owned-write/change-tracking record, and isolated tests suffice when existing task authority covers the exact local edit. Do not invent a separate protected permit or commit; escalate only if shared/protected effects or ambiguity appear. |
| Rename a config key used by three services. | Require runtime consumer inventory, default semantics, coexistence/dual-read transition, contract tests, staged rollout, signals, and disable path. Unknown consumers or compatibility-critical version-skew timing blocks mutation; unconfirmed calendar dates remain `TBD` without blocking read-only planning. |
| Fix a flaky distributed lease test. | Borrow Tabular ML/Evaluation for reproducibility; require a reproduced signature and race/clock/network/isolation hypothesis. Increasing retries or timeouts is blocked without changed evidence; runtime gates activate if production code changes. |
| Migrate a payment-ledger schema and event API at peak. | Apply all gates and borrow security/product lenses; require static/runtime consumers, version-skew compatibility, ledger invariants, reconciliation, peak load, recovery rehearsal, SLO impact, and incident command. Unknown cohorts, abort thresholds, recovery time, or owners blocks commitment. |
