# Execution Feedback And Independent Observation

## Distinct Duties

The executor owns action-local sensing and truthful reporting. The observer owns cross-cutting judgment about intent, invariants, authority, drift, and continuation. The designated designer owns whole-task impact judgment; the coordinator applies canonical state transitions from accepted replans. A blind reviewer owns independent epistemic assessment after its precommitment.

Do not route executor conclusions to a blind reviewer before the reviewer freezes scope, rivals, sample, and independent control. For protected action, the observer must be able to inspect authorized primary evidence rather than only an executor-curated narrative.

## ExecutionFeedbackEvent

```text
event_id, epoch, snapshot_rev, node_id, observed_at
event_type: barrier | anomaly | assumption_break | evidence_conflict |
            failed_hypothesis | effect_drift | scope_cost_deadline_drift |
            rollback_degradation | unexpected_opportunity
expected_state, observed_state, evidence_refs
affected_goal_invariant_permit_scope
in_flight_effects, safe_stop_state
executor_assessment, proposed_discriminating_probe
sensitivity_and_disclosure_limits
```

Emit at declared semantic barriers and immediately for material deviations. Batch ordinary progress. Set a maximum unchecked interval when consequence, latency, or mistake accumulation warrants it; for a non-accumulating one-shot barrier record `N/A` with reason.

## Workload Envelope And Anomaly Detection

Before a potentially long smoke, precheck, scan, build, evaluation, migration, research operation, tool sequence, or protected loop, inspect the controlling implementation/workflow and freeze a `PreExecutionWorkModel`:

```text
applicable_source: code | query_plan | tool_contract | workflow_structure |
                   calibrated_observation | mixed | N/A
source_refs_and_positive_applicability_evidence
code_query_plan_tool_or_workflow_dataflow
semantic_units_and_input_cardinality
loops_fanout_fanin_repetition_and_access_pattern
intended_complexity_and_bytes_or_calls_per_unit
concurrency_backpressure_and_resource_topology
external_service_io_or_hardware_lower_bounds
historical_analogues_and_applicability
```

Then freeze the workload envelope:

```text
semantic_work_unit_and_phase
target_population_coverage_and_completion_signal
preexecution_work_model_ref
calibration_basis_and_sample_size
expected_runtime_or_progress_range
confidence_uncertainty_and_applicability
progress_cpu_io_memory_network_queue_and_accelerator_counters
artifact_and_integrity_checkpoints
safe_stop_cancel_resume_and_invalidation_boundary
first_check_at_time_and_semantic_progress
maximum_unchecked_interval
```

Estimate a range, not a false-precision ETA. When code controls the work, inspect it as the expectation basis. Otherwise derive the model from query/plan, tool contract, workflow structure, applicable history, a representative microbenchmark, or an early bounded sample. `N/A` requires positive evidence that the action is cheap, non-scaling, and objectively bounded. For opaque, unknown, or remote-heavy expensive work, run one cheap calibration probe before launch; if calibration is impossible, narrow/block the permit or claim and expose uncertainty rather than inventing a duration or code-level facts.

Calibration selection is a prelaunch gate, not a post-hoc explanation. Historical evidence qualifies only when its tier, object/work-unit shape, access pattern, concurrency, and relevant environment are shown comparable. Ordinary long remote or cold-storage work uses a representative cold-unit microbenchmark or bounded early sample when comparable history is unavailable, then freezes the expected range, uncertainty, first check, remaining-work rule, and safe-stop point before launch. If an inherited already-running node lacks this envelope, freeze a measured envelope at the next safe barrier before a decision-changing continuation; do not retroactively label the launch calibrated. A sound near-complete run may still finish only when direct integrity/progress evidence, a supported external lower bound, and the remaining-work rule jointly support continuation.

The envelope is relational, not a universal stopwatch. Schedule the first check early enough to observe semantic progress, diagnose, cancel, or replan before the expected completion or failure-cost boundary; it cannot occur after the upper expected range. Waiting 30 minutes for the first check of a phase expected to finish within 10 minutes is invalid by construction. Short smokes/prechecks deserve tighter observation because their purpose is cheap feedback. Unexpected scale, implausibly fast completion, low semantic coverage, rising unit cost, idle required resources, repeated reads/digests, stalled queues, or absent artifacts trigger review even when no duration threshold has expired.

The executor must detect these triggers; do not wait for a user status complaint. When the user asks for status, answer with measured work, cause confidence, remaining uncertainty, and disposition rather than using the question as the anomaly detector.

An anomaly may expose a context gap, but executor/observer evidence first discriminates runtime and semantic causes. CPU availability, worker idleness, progress, queues, output paths, code/dataflow, and preflight behavior are discoverable evidence, not user questions. Emit a `RuntimeContextGap` to the designer only when diagnosis reaches an unavailable user-owned choice; run its `ExecutionContextCheckpoint` at the resulting semantic barrier, not on routine progress or a conversational timer.

For a failed verification node record:

```text
TestFailureDisposition:
  candidate_snapshot, failing_test_and_oracle, failure_signature
  affected_invariant_and_surface
  controlling_code_diff_and_dataflow_review
  candidate_causes_and_cheapest_discriminator
  changed_code_config_environment_hypothesis_or_evidence
  next_focused_check, broad_rerun_trigger_or_NA
```

Inspect the failure, controlling path, diff, and relevant environment before retry. Never repeat a suite merely hoping for another result. Prespecified bounded repetition is allowed to diagnose flakiness, races, nondeterminism, or variance only with a sample cap, oracle, and stop condition. Infrastructure retry requires evidence of changed service/runner/network state. If a focused failure exposes wider impact, expand the review before the suite.

```text
SchedulerAnomaly:
  epoch, sweep_id, observed_at, cap_and_reservations
  ready_at_by_node, dispatched_at_by_node
  tool_queued_started_and_running_state
  eligible_undispatched_nodes
  claimed_block_reason_and_evidence
  actual_free_effective_slots
  cause_rivals: real_dependency_or_resource | coordinator_sequentialization |
                scheduler_or_tool_bug
  critical_path_correctness_and_decision_impact
  corrective_dispatch_or_replan
```

Trigger when eligible ready work remains undispatched with a free effective slot, an artificial edge or join serializes independent work, optional work consumes reserved review capacity, claimed parallel work never dispatches/overlaps, or queue/resource evidence invalidates the assumed cap. Dispatch missed work when safe; otherwise recalibrate the cap from evidence. Distinguish `ready`, `dispatched`, `tool_queued`, `started`, and `running`; only observed overlap supports a runtime-parallelism claim.

For a material deviation create an `AnomalyDisposition`:

```text
observation_scale_and_affected_units
expected_vs_observed_relation
candidate_causes: [data_volume, hardware_or_io_bound, remote_or_queue_wait,
                   bug_or_incomplete_coverage, poor_complexity_or_repeated_work,
                   lock_stall_or_resource_topology, unknown]
supported_causes[{cause, evidence_refs, confidence, necessary_or_avoidable,
                  estimated_contribution, interactions}]
cheapest_discriminating_probe
cause_evidence_and_confidence
correctness_and_decision_validity_impact
critical_path_and_downstream_dag_impact
current_progress_integrity_and_remaining_work
stop_continue_or_repair
fix_epoch_and_invalidation_boundary
repair_consequence_class
route_edge_disposition_ref_or_NA
repair_authority: advisory_only | executable
qualified_design_contract_ref_or_NA
```

CPU/RSS, a long duration, or a large dataset alone does not establish cause. Inspect semantic progress and the relevant dataflow/resource counters. If progress or unit scaling contradicts the model, reopen the controlling code, query/plan, tool/workflow contract, dataflow/access assumptions, input cardinality, and resource topology before extrapolating or attributing cause. Necessary scale cost and avoidable design cost may coexist; decompose them instead of choosing one story. Apply the same check symmetrically to suspiciously fast completion, which may mean skipped coverage or a broken counter.

Stop/fence and repair when the anomaly can make results incomplete/incorrect, corrupt decisions, invalidate descendants, create unacceptable critical-path amplification, violate authority/privacy/resource bounds, or make the main run infeasible. Do not continue merely because partial outputs look correct.

Diagnosis and safe-stop may precede repair routing. If a proposed repair changes asymptotic behavior, dataflow, concurrency, backpressure, resource topology, integrity, or performance-validity assumptions, set `repair_authority=advisory_only` until its R2/R3 `RouteEdgeDisposition` is `accepted_attested`. Until then, say “candidate repair” or `route_pending`, never unconditionally promise to implement, repair, prefetch, parallelize, optimize, or rerun. This does not block a valid unaffected epoch or other ready branches.

A valid non-damaging run close to completion may finish when snapshot/integrity/progress checks pass and restart would cost more. A future fix may proceed concurrently only after dependency, write-scope, provenance, and active-epoch analysis proves it cannot stale or alter the current result or downstream jobs. Otherwise quarantine the fix to the next epoch. For recurring or partitioned work, compare lifecycle/topology alternatives—parallel decomposition, changed access pattern, caching/index/materialization, incremental metadata, or no change—against measured update cadence, consumer needs, invalidation, storage duplication, and complexity. No particular architecture is mandatory.

## ObserverCheck

```text
event_id, epoch, snapshot_rev, evidence_seen
verdict: proceed | warn | pause_replan | pause_restart | stop | escalate
rationale, required_probe_or_repair
affected_nodes_and_authorizations
resume_authority, acknowledgement_deadline
```

The observer may request a bounded discriminating probe within its authority. Its pause/stop is binding. Silence, timeout, stale epoch, or unreadable evidence is not approval. The executor may safe-stop but cannot self-resume. Late or stale checks are quarantined.

Feedback edges are typed `advisory`, `snapshot_dependency`, or `safety_veto`. A material change invalidates only affected DAG descendants, evidence, and permits. Preserve old snapshots and in-flight-effect handling.

## Proportionality

Routine reversible deterministic work needs no independent continuous observer. Ordinary tests and one result check suffice unless an anomaly appears. For protected work use pre-execution, result-handoff, and pre-publication barriers by default; add event barriers and a maximum unchecked interval for active effects.

Prevent alert fatigue and anchoring: report versioned deltas, include contrary evidence, minimize sensitive content, and separate facts from executor interpretation. The observer advises or vetoes; it does not become a second canonical editor.
