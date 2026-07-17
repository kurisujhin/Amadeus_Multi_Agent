# Runtime DAG And Concurrency

Critical/protected/asynchronous nodes record purpose, evidence target, inputs/outputs, scopes, authority, requested/selectable/accepted/enforceable/attested route, dependencies, typed join, timing, workload envelope, queue budget, useful partial, retry, cancellation, change-tracking mode, epoch, and status. Statuses include `pending`, `ready`, `running`, `sufficient_partial`, `complete`, `timed_out`, `blocked`, `cancelled`, and `late_quarantined`.

For long, asynchronous, joined, or scaling-sensitive nodes record a `PreExecutionWorkModel` derived from the controlling code, query/plan, tool contract, workflow structure, or calibrated observation; use `N/A` only with positive cheap/non-scaling evidence. Record calibration basis/range/confidence and `ready_at`, `dispatched_at`, `started_at`, `first_evidence_at`, `completed_at`, first-check point, queue wait, service/run time, blocked/wait reason, semantic units complete, unit-cost trend, work amplification, resource utilization versus intended topology, useful-partial validity, and critical-path impact/efficiency. The first check must occur early enough to react before expected completion/upper range, not at an unrelated fixed duration. These counters supply the workload envelope and observer; timestamps alone never decide abnormality.

After every material transition compute the ready set, dispatch independent nodes to the cap, keep write ownership disjoint, reserve review/safety capacity, coalesce at semantic barriers, partially invalidate descendants, and quarantine late output.

```text
SchedulingSweep:
  epoch, sweep_id, observed_at, concurrency_cap
  required_reservations[purpose, node_or_role, slots, becomes_ready_by,
                        expiry_or_release]
  effective_owner_slots
  blocked_or_not_ready[node_id, reason, evidence_refs, recheck_trigger]
  ready_nodes[node_id, ready_at, dependency_snapshot, authority_snapshot,
              writer_scope, resource_class]
  constrained_ready[node_id, reason, evidence_refs, recheck_trigger]
  eligible_ready_nodes[node_id]
  dispatched_nodes[node_id, dispatched_at, tool_or_runtime_ref,
                   state: dispatched | tool_queued | started | running]
  eligible_undispatched[node_id, reason, evidence_refs, recheck_trigger]
  free_effective_slots_after_dispatch, scheduler_anomaly_ids
```

Partition every considered node before dispatch. `blocked_or_not_ready` covers an unsatisfied hard/snapshot dependency or join, veto, route/permit/context wait, cancellation, or epoch fence. A `ready` node has those edges satisfied; writer, rate, resource/backpressure, ordered-semantics, or required-reservation evidence may place it in `constrained_ready`. Remaining mutually independent nodes are `eligible_ready`. Dispatch eligible nodes up to effective slots in one sweep—accepted dispatches occur without awaiting sibling completion even if tool calls are separate. Accepted tool queueing is dispatched with state `tool_queued`, never undispatched or running. Capacity overflow uses `capacity_queue`.

Every constrained or eligible-undispatched node records its typed reason and positive evidence. Free effective capacity plus an `eligible_ready` node left undispatched is `SchedulerAnomaly: missed_ready_dispatch`; hidden convenience sequencing is not a dependency. Recompute after completion, failure, cancellation, human/context/permit/route/resource change, or reservation release. If tiny independent work is cheaper together, coalesce it into one bounded node during DAG construction with positive cost evidence; once separate nodes are eligible, vague coordination overhead cannot serialize them.

A join consumes predecessor results; it never serializes independent predecessors. An ordering edge names its data, authority, safety, writer, resource, contamination, or semantic dependency. Overlapping shared-writer scopes serialize; disjoint authorized worktrees/patch nodes and read-only nodes may run concurrently. Required reviewer/observer reservations move `planned → active → consumed | released | expired`, name `becomes_ready_by` and release/expiry evidence, and reduce effective capacity until explicit consumption, release, expiry, or replacement. A planned reservation becomes stale when its readiness bound passes without activation evidence; staleness triggers replan and blocks optional admission but never cancels the protected role or frees its slot by itself. Release, expiry, or replacement immediately recomputes the ready set and effective slots. Optional work may backfill only when it is cancellable before the protected role's readiness bound and cannot delay that role.

Claim concurrency only from distinct accepted dispatch records and, when observable, session IDs, start/tool-queue states, and overlapping intervals. Concurrent dispatch is not proof of concurrent execution. Direct one-node work may record inline `ready={node}; cap=1; dispatched={node}; anomaly=none`; never create work merely to fill a slot.

Before dispatching an expensive or high-replay-cost node, attach the compact `PrecommitmentLeverage` record from `context-closure-and-human-input.md`. A direction-changing unresolved fact is a hard dependency for the commitments it can change, not for unrelated read-only discovery. For cheap reversible direct nodes, a one-line intent and objective result check is enough.

Model agent-discovered context gaps as graph state. `retrieve` creates an evidence dependency; `infer_for_probe` unlocks only the named reversible probe while descendants remain blocked; `defer_to_barrier` schedules an expiring checkpoint; `ask_user` is a hard dependency only for mapped actions; `resolved` links closure evidence. At decision-changing barriers, an `ExecutionContextCheckpoint` batches compatible user-owned questions and keeps independent branches ready. Dev/smoke/full-evaluation or scratch/publication branches remain separate so a late private choice does not force a global restart.

Model human messages as graph events. A material `supplement`, `correction`, `replace`, or `authority` event returns to the designer, updates the original-task impact map, fences affected in-flight work, and creates a new epoch or partial invalidation. For each affected mutation, semantic-dependent test, or restart, the accepted `TaskImpactPacket` edge is a `hard_dependency`; safe-fencing occurs before that packet is produced. A `status` or presentation-only event may add a reporting node but does not invalidate semantic descendants.

In active compact/careful/full work the executable input edge is `accepted DesignerHandoffRecord → accepted TaskImpactPacket → affected mutation/test/restart`. For R2/R3 anomaly repair it is `accepted_attested RouteEdgeDisposition → design-dependent mutation`. Diagnosis, safe-stop, advisory design, valid current-epoch continuation, and unaffected branches do not depend on the latter edge.

For repository writes, the DAG names one canonical writer per branch/worktree/epoch and carries a `ChangeTrackingContract`. Verification and commit are separate nodes when a commit has audit/recovery value. Evidence records preserve their exact producing candidate/tree and depend on named semantic producer, input, evaluator, environment, topology, authority, and freshness edges—not on the root hash as a universal dependency. On change, build the `ChangeImpactClosure` in [evidence-provenance-and-reuse.md](evidence-provenance-and-reuse.md), preserve unaffected ready/completed nodes, and add rerun, rescore, or protected-gate nodes only for intersecting or unresolved closures. A global new-epoch rerun edge requires a demonstrated shared dependency. Push, merge, deploy, and publication are separate protected edges.

Disjoint claim-impact closures remain independent and dispatchable in the same scheduling sweep. An unresolved dynamic edge blocks only mapped claims; it never becomes a global provenance join without evidence that the dependency is shared.

Order costly verification as `CodeImpactReview → VerificationPlan → focused test → affected-surface expansion when triggered → full suite at coherent checkpoint/trust boundary`. A cheap targeted check may combine review and plan inline. A broad or expensive node is not ready before its review edge. After failure, require `TestFailureDisposition` and a changed code/config/environment/hypothesis/evidence condition before focused retry; an identical command on the same fingerprint is a no-value probe and trips the circuit breaker, except a prespecified bounded diagnostic repetition with a sample cap, oracle, and stop condition. Keep unrelated verification branches ready.

Independent code-impact reviews and focused checks on disjoint surfaces dispatch concurrently after their own dependencies close; do not create one global review bottleneck. The full suite remains behind its focused-check join. Shared mutable worktrees/fixtures serialize unless safely isolated, and internal test-runner parallelism is a separate measured resource/topology decision.

Joins are `all_required`, `quorum(k)`, `first_sufficient`, or `deadline_with_partials`; each defines timeout disposition, cancellation, late treatment, and separate veto behavior.

Trip the circuit breaker on no-progress probes, unchanged objections, projected breach, queue exhaustion, stale epoch, failed cancellation, workload-envelope contradiction, or implausibly fast/incomplete coverage. Narrow, replan, block, or stop without lowering safety standards.
