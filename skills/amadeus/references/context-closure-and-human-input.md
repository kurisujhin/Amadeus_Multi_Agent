# Context Closure, Precommitment, And Human Input

## Self-Grill Before Commitment

Before a costly, protected, long-running, high-fanout, hard-to-reverse, or design-locking action, the designer privately grills the task. This is retrieval and decision closure, not a questionnaire shown to the user.

Check:

```text
goal_and_supported_action
background_and_current_state
inputs_outputs_and_owners
scope_constraints_non_goals
success_countermetrics_and_failure_cost
authority_privacy_and_effect_boundaries
environment_capacity_topology_and_dependencies
snapshot_freshness_and_arrival_semantics
verification_rollback_stop_and_resume
decisions_the_user_must_own
```

For each missing fact record:

```text
fact, decisions_it_can_change, impact
discoverable_from_local_or_authoritative_sources
cheapest_safe_retrieval_or_probe
owner, blocked_nodes, bounded_default_if_any
```

Retrieve discoverable facts before asking. Inspect the smallest sufficient source set and batch compatible read-only checks. Ask the user once for unavailable direction-changing facts, prefaced by a compact task digest so omissions or misunderstandings are visible. Ask about background, intent, private constraints, authority, or value tradeoffs—not implementation details that repository evidence, domain expertise, or objective tests can settle.

An unresolved direction-changing fact pauses only commitments it can change. Safe read-only discovery and bounded reversible probes continue. A bounded assumption is allowed only when the action is itself an explicitly labeled reversible probe, the falsifier and cost cap are frozen, and every downstream commitment remains blocked.

## Close Context During Execution

At a semantic barrier, new evidence, assumption break, route/domain change, anomaly reclassification, or transition into a full evaluation, publication, rollout, pointer change, or other protected phase, re-dispose newly relevant facts:

```text
RuntimeContextGap:
  fact, evidence_already_searched, decisions_actions_claims_changed
  owner_class: source | environment | domain | user | external_authority
  disposition: retrieve | infer_for_probe | defer_to_barrier | ask_user | resolved
  probe_scope_falsifier_and_cost_cap
  defer_barrier_expiry_and_reopen_trigger
  affected_nodes_and_blocked_commitments
  safe_parallel_branches
  question_necessity_evidence
```

The executor emits a gap; the designated designer adjudicates a direction-changing gap; the coordinator alone changes canonical DAG state. Ask the user only when all are true: the fact can change a mapped commitment before its next safe barrier; authorized local, authoritative, environmental, or bounded-probe evidence cannot resolve it; no reversible assumption isolates it; and the user owns the intent, private constraint, value/risk/cost/priority tradeoff, snapshot/arrival policy, or exact authority. Otherwise retrieve it, infer only for the named reversible probe, or defer it with an expiry.

Repository facts, schemas, field lineage, code/dataflow, current runtime state, CPU/worker availability, queue progress, and objective implementation choices are evidence to inspect—not questions. Do not re-ask an explicit prior instruction unless conflicting or materially stale evidence appears. Batch compatible questions at the next affected barrier; interrupt immediately only when a protected or in-flight action cannot remain safe. Each question states the materially different outcomes it selects between and the exact commitment blocked. Unrelated discovery, scratch work, and independent smoke branches continue.

Record the barrier result:

```text
ExecutionContextCheckpoint:
  epoch, node, barrier, observed_at
  new_or_changed_facts, context_need_dispositions
  task_digest_delta, questions_due_now
  deferred_questions_and_deadlines, hard_join_updates
  safe_continuing_branches, partial_invalidation
```

An answer re-enters as a typed `HumanInputEvent`. Material answers require the same whole-task `TaskImpactPacket` and partial-invalidation rules below. No answer means only mapped commitments remain blocked; a default is never invented merely to avoid waiting.

## Precommitment Leverage

Planning is cheap only relative to the action. Use this compact record when a plausible failure or replay is materially more expensive than bounded reasoning or a discriminating probe:

```text
action_cost
uncertainty_that_can_change_action
cheapest_discriminator
planning_cap
execute_when
stop_or_replan_trigger
```

Precommit when uncertainty could change design, authorization, correctness, cost, invalidation, snapshot, or stop strategy; when an alternative could remove material work/risk; or when a failed action has large replay/fanout.

Stop planning and execute when the minimum safe and valid plan is closed and another planning step has lower expected decision value than its delay, or when the remaining uncertainty can only be resolved by bounded execution evidence. Cheap, local, reversible, objectively checked work uses a one-line intent and proceeds. Do not turn “think first” into analysis paralysis, mandatory artifacts, or extra agents.

## Typed Human Input

Every mid-task user message becomes a `HumanInputEvent` before the coordinator changes canonical state:

```text
event_id, observed_at, message_ref
primary_kind: replace | supplement | correction | status | authority | presentation
secondary_kinds: [zero or more additional kinds]
materiality: none | local | direction_changing | protected
affected_claims_nodes_artifacts_and_effects
in_flight_safe_stop_or_continue
authority_change_and_evidence
designer_impact_verdict
new_epoch_or_partial_invalidation
user_response
```

Segment compound messages by semantic clause. A status or presentation clause never masks a correction, supplement, replacement, or authority clause in the same message; process every material component and join their effects before resuming. Choose `primary_kind` by the component with greatest effect on goal, authority, validity, or in-flight work, not by sentence order.

- `replace`: reopen the goal and dependency graph; cancel or fence incompatible work.
- `supplement`: add background, constraint, or desired output; the designer reviews the whole original task for implications.
- `correction`: mark contradicted assumptions/evidence, fence affected work, audit neighboring decisions produced by the same inference, and rerun affected descendants.
- `authority`: validate issuer, exact action/scope/stage/expiry; it may expand or narrow permits but never silently waive another binding veto.
- `status`: answer with evidence and current disposition; do not globally invalidate.
- `presentation`: change wording/layout only unless semantics or an accepted artifact changes.

A material supplement/correction is not handled solely inside the current executor. The designer safe-pauses affected work when needed, updates the task ledger and DAG, checks topology and in-flight effects, preserves unaffected nodes, and issues a visible impact verdict. Status and immutable presentation input remain lightweight.

The designer is the canonical planning function; the coordinator remains the sole canonical-state mutator. In a `direct` low-risk workflow the coordinator may combine designer and coordinator duties with an explicit impact record. In an active `compact`, `careful`, or `full` real-agent workflow, a direction-changing supplement, correction, replacement, or authority change must be reviewed by the designated workflow designer as a whole-original-task delta; the current executor or coordinator alone cannot dispose of it. The designer returns a binding `TaskImpactPacket`, and the coordinator applies it only after snapshot/authority checks. An executor may propose an impact but cannot silently substitute for designer review.

```text
DesignerHandoffRecord:
  event_id, topology_mode
  sender_runtime_id, designated_designer_runtime_id
  dispatched_at, original_task_and_durable_state_snapshot_ref
  accepted_at, accepted_task_impact_packet_ref
  affected_nodes_and_hard_join_refs
```

For direction-changing input in active compact/careful/full work, an accepted `DesignerHandoffRecord` is evidence for the existing `TaskImpactPacket` hard dependency. Coordinator-local analysis, an unaccepted dispatch, or retrospective review does not satisfy it. If the designated designer is unavailable, affected work stays fenced while unrelated discovery and execution continue. Direct low-risk work records `topology_mode=combined_direct` inline and creates no extra runtime.

For a direction-changing event, safe-fencing of affected work is immediate. The accepted `TaskImpactPacket` is a hard dependency of every affected patch or write, every test whose oracle or expected result depends on the changed semantics, and every affected restart or descendant dispatch. The order is `safe-pause/fence → freeze original task + durable state + delta → accepted TaskImpactPacket → route/permit refresh → mutation or restart`. Unaffected read-only discovery and objectively independent work may continue. Retrospective review cannot validate mutation performed before this barrier.

The `TaskImpactPacket` carries the original-task snapshot, changed-fact dispositions, consolidated question batch if any, affected graph and hard joins, safe continuing branches, and partial invalidation. A subskill or executor may nominate a fact but cannot decide that the user must be asked.

## Context Closure Output

Before the first commitment, expose only what helps the user verify the task:

```text
task_digest: why, requested outcome, key constraints, protected boundaries
retrieved_facts: decision-relevant facts, not an inventory dump
questions: one batch of unavailable direction-changing decisions
safe_work_continuing: read-only or bounded probes
blocked_commitments: exact nodes and why
```

Do not claim context is closed because a template is filled. Closure means every direction-changing commitment has retrieved evidence, explicit user direction, or a bounded probe contract.
