---
name: amadeus
description: "Design, execute, observe, track, and evolve scope-faithful real-agent workflows with binding user constraints, minimum-sufficient work, typed replanning, explicit concurrency, workload-aware observation, verified change checkpoints, independent judgment, and compact reliability controls. Use when the user invokes this skill, requests real subagents, improves a reusable workflow or skill, or needs independent judgment for consequential experiments, evaluations, research, architecture, unfamiliar systems, surprising results, long-running work, or effectful actions."
---

# Multi-Agent Workflow Designer V5.1

## Golden Circle

Start with `Why` (decision, claim, learning objective, or protected outcome), `How` (evidence, independence, capabilities, feedback, and controls), and `What` (smallest topology, actions, artifacts, and terminal disposition). Do not begin with roles. A role exists only for a distinct uncertainty, capability, veto, effect, or independence boundary.

Read [research-basis.md](references/research-basis.md) when changing topology or insight policy. Human findings motivate workflow hypotheses; they do not prove optimal agent topology or that agents possess unconscious cognition.

## Choose Proportionally

- `direct`: coordinator executes; explicit invocation adds one bounded independent premise, risk, or result check.
- `compact`: one owner and one context-separated reviewer for bounded interpretation or experimentation.
- `careful`: add only specialists tied to applicable uncertainty; add an independent observer for production, external, irreversible, sensitive, difficult-to-rollback, long-running mistake-prone, or explicitly observed work.
- `full`: action-scoped approval, rollback, monitoring, recovery, restart fencing, and post-action validation for high-impact effects.

The user alone may waive explicitly requested real-agent independence or named topology. Never silently collapse requested roles. A parent-spawned bounded agent already satisfies its assigned real-agent contract and must not recurse merely because this skill is named.

## Honor Literal Scope And Simplicity

Freeze a compact `UserExecutionContract` from every explicit clause: requested outcome; allowed change; invariants and non-goals; data population and purpose; metrics, slices, and denominators; outputs and presentation; settled defaults and wait policy; resource and concurrency instructions; budget and deadline; and terminal cleanup or file-placement obligations. This is the controlling execution contract. A correction immediately replaces conflicting assumptions; never re-ask a choice whose answer or default the user already supplied.

Every nontrivial node must map to an explicit contract clause, a protected invariant, or a decision-changing uncertainty. Remove it otherwise. Interpret `only X`, approximate or minimum sample wording, `no preflight/dev/cohort`, and similar limits literally unless they violate an applicable safety or authority boundary or cannot support the requested claim. Never turn a demonstration into population validation, a minimum into an exact target, or a named metric into an adjacent aggregate.

Use the minimum-sufficient cycle: the smallest read, scan, sample, probe, test, and artifact set that can establish the requested outcome. Run a preflight only for a concrete plausible failure whose expected harm or replay cost exceeds the check. For low-risk behavioral changes, default to one structural check, up to three focused cases when needed, one independent review, and at most one retry after changed evidence. Expand only after a concrete failure, an applicable protected risk, or an explicit user/repository requirement.

During unavoidable waits, dispatch independent ready preparation without waiting for the blocked sibling. Honor explicit wait, no-downgrade, and no-ask policies. Track requested reports, presentation, teardown, and cleanup as terminal hard joins. When the user reports needless complexity or repeats a correction, trigger `ComplexityReset`: fence affected work, rebuild the contract from the latest instructions, delete unearned nodes and checks, preserve unaffected progress, and resume from the simpler graph.

## Close Context Before Commitment

Read [context-closure-and-human-input.md](references/context-closure-and-human-input.md). Before costly, protected, long-running, high-fanout, hard-to-reverse, or design-locking work, privately self-grill the goal, background, inputs/outputs, constraints, success and failure cost, authority, environment/topology, snapshot/arrival semantics, verification, rollback, and decisions the user must own.

Retrieve discoverable facts first. Then show one compact task digest and ask one consolidated set of unavailable direction-changing questions. Ask for background, intent, private constraints, authority, or value tradeoffs—not implementation details that sources, domain expertise, or objective tests can settle. Pause only affected commitments; safe read-only discovery and bounded reversible probes continue.

Re-run context disposition at decision-changing execution barriers. Retrieve discoverable facts, infer only inside a bounded reversible probe, defer facts that cannot affect the current branch, and ask one compact user batch only for unavailable user-owned choices before their mapped commitments. Do not make the user diagnose execution or repeatedly confirm prior instructions.

Use `PrecommitmentLeverage` when bounded thinking or a discriminating probe is materially cheaper than failure/replay: record action cost, decision-changing uncertainty, cheapest discriminator, planning cap, execute condition, and stop/replan trigger. Stop planning when the minimum safe/valid plan is closed and more thought has lower decision value than delay. Cheap, local, reversible, objectively checked work proceeds directly.

Before dispatching any action, classify whether it is affected by pending human input, protected, repository-writing or committing, long or scaling-sensitive, or R2/R3. Applicable controls are hard dependencies in this order: safe-fence affected work; accept any required designer impact verdict; close discoverable context, authority, and vetoes; freeze the applicable workload model, route record, and change-tracking mode; issue the permit; then mutate, launch, or commit. A later reviewer, successful result, or tool/harness rejection cannot cure a missing earlier dependency. `direct`, `cheap`, and `reversible probe` permissions apply only after this classification; record an inline `N/A` with positive evidence for genuinely inapplicable controls.

Diagnosis, measurement, safe-stop, and advisory design may continue while an R2/R3 route is pending. Design-dependent implementation is not ready until `RouteEdgeDisposition` records the requested, accepted, enforceable, and attested route plus qualified design origination or reconstruction. A plan or future-tense promise to implement, repair, optimize, prefetch, parallelize, or rerun does not satisfy this edge; label it `route_pending` and advisory until the edge closes.

Treat each semantic clause in a mid-task user message as a typed event: `replace`, `supplement`, `correction`, `status`, `authority`, or `presentation`. Compound status-plus-correction/authority messages keep every material type; a status clause cannot mask replanning. In direct low-risk work the coordinator may record the designer impact itself. In an active compact/careful/full real-agent workflow, direction-changing material returns to the designated workflow designer for whole-original-task review; the current executor/coordinator alone cannot dispose of it. The coordinator applies the impact verdict, fences affected nodes, and partially invalidates. Status and immutable presentation input stay lightweight.

For that active compact/careful/full handoff, record the designated designer runtime, dispatch/receipt snapshot, and accepted `TaskImpactPacket` reference before affected mutation, semantic-dependent tests, or restart. The packet contains the verdict; a bare verdict, coordinator saying “I reviewed,” or restated correction is not handoff evidence. Direct low-risk work may use one inline combined impact record; status, immutable presentation, and local non-material input need none.

## Route Domain Expertise

When domain semantics could change the supported action, validity claim, protected risk, evidence source, or observer trigger, read [domain-router.md](references/domain-router.md). Route from the decision and dominant validity/risk—not nouns, tools, or artifact type.

Select one primary domain whose gates own the dominant claim or risk, plus at most two borrowed lenses by default. A borrowed lens is justified only when it changes a question, gate, proof, anomaly trigger, counter-metric, or protected action. Exceed two only for a distinct applicable safety-critical or decision-critical delta and record the marginal value. A domain name is a competency, never an automatic agent; map compatible perspectives to existing runtime owners unless independence or capability requires separation.

Each selected subskill returns a `DomainGatePacket`. The parent owns routing, DAG, permits, observer/reviewer separation, conflict resolution, synthesis, and acceptance. Deduplicate overlapping domain proofs through shared evidence references while preserving separate gate verdicts; the stricter applicable veto wins. Freeze routing before owner conclusions when feasible. A material late route change is an explicit replan with partial invalidation.

A native domain handoff is incomplete until its exact rendered JSON passes the packaged validator. Semantic review cannot rescue an invalid packet.

## Understand Before Commitment

Maintain a revisable inquiry state, not mandatory phases. Read [adaptive-inquiry.md](references/adaptive-inquiry.md). Track live interpretations that could change the claim, evidence for and against, and the highest-value discriminating observation. Permit `unknown`, `N/A`, reordering, and omission with reason.

When interpretation matters, encounter representative raw ordinary, failed, extreme, boundary, and slice-specific evidence; inspect lineage and producer/consumer behavior; and compare documentation, implementation, and observation. Establish field, sentinel, label, cohort, denominator, and metric meaning before treating numerics or hashes as validity. Preserve structural, semantic, measurement, and decision validity as distinct layers.

Match sampling rigor to the claim. A presentation or demonstration sample needs only a valid bounded example satisfying the stated minimum; cap the scan and stop when one is adequate. Comparative or generalizing claims use an explicit frame combining systematic/random coverage with risk-, boundary-, transition-, and influence-based cases, separate exploration from untouched confirmation, and preserve meaningfully independent reviewer selection.

Inspect the least sensitive evidence that can discriminate. Sensitive access requires authority, purpose limitation, minimization, handling/storage boundaries, retention/deletion, and disclosure constraints before access.

## Build And Schedule The Runtime DAG

Before delegation, express the executable graph rather than a role list. Read [runtime-dag.md](references/runtime-dag.md). Critical, protected, or asynchronous nodes name contract, evidence target, scopes, authority, route, dependencies, typed join, deadlines, useful partial, retry, cancellation, and epoch. Edges are `hard_dependency`, `snapshot_dependency`, `safety_veto`, or `advisory`.

Dispatch ready independent nodes concurrently up to the cap; reserve required review/observer capacity; keep canonical write ownership disjoint. For `compact`, start owner and blind reviewer concurrently. The reviewer receives the raw task and source universe first and freezes scope, rivals, sample, and one expectation-independent control before owner conclusions.

At each scheduling sweep, enumerate the ready set and dispatch every mutually independent eligible node up to the effective cap without awaiting sibling completion. Record reviewer/observer reservations and a typed reason for every ready-but-undispatched node. Free effective capacity with an eligible undispatched node is a scheduler anomaly; “up to the cap” is not permission to serialize. Do not claim parallel execution from a plan or role list—distinguish dispatched, tool-queued, started, and observably overlapping work.

Type joins as `all_required`, `quorum(k)`, `first_sufficient`, or `deadline_with_partials`. No join waits indefinitely. Reviewer timeout narrows or withholds a claim; observer silence never approves continuation. Safety, privacy, and authorization vetoes survive timeout and quorum.

Default bounded direct/compact budgets: first decision-relevant evidence within 10 minutes, terminal disposition within 45 minutes, at most two concurrent reasoning agents, one focused review wave, one changed-evidence retry, and queue/wait no more than 25% of wall time. Override measured lower bounds explicitly.

Trip `InquiryCircuitBreaker` on projected deadline breach, queue exhaustion, two no-value probes, repeated unchanged objections, cancellation failure, stale-snapshot work, workload-envelope contradiction, or implausibly fast/incomplete coverage. Choose `continue_with_replan`, `narrow_or_withhold`, `block_action`, or `stop_execution`; do not add agents by default.

## Observe While Executing

The executor observes local state; the independent observer judges goal, safety, authority, drift, and continuation. They are not interchangeable. Read [execution-feedback.md](references/execution-feedback.md).

At declared semantic barriers and on material anomalies, the executor emits a compact, evidence-linked `ExecutionFeedbackEvent`. Use anomaly interrupts plus a consequence-scaled maximum unchecked interval, not continuous narration. The observer receives direct evidence access when authorized, returns a same-snapshot binding verdict within its declared authority, and may request one discriminating probe.

Before long work freeze a `PreExecutionWorkModel` from the controlling code/dataflow when code governs the work, otherwise from the query/plan, tool contract, workflow structure, or calibrated observation. Record semantic units/cardinality, loops/fan-out/repetition/access pattern, intended complexity and bytes/calls per unit, concurrency/backpressure/resource topology, and external lower bounds. Calibrate an expected progress/runtime range from applicable history, a microbenchmark, or a bounded early sample; expose confidence and uncertainty rather than inventing an ETA. Opaque expensive work narrows/blocks when it cannot be calibrated; cheap non-scaling work may mark this N/A with evidence.

Freeze the relational workload envelope with target coverage/completion signal, calibration basis/range, progress/resource counters, artifact/integrity checks, and safe-stop/resume boundary. Schedule the first check early enough to diagnose and act before expected completion or the upper range—a 30-minute first check is invalid for a phase expected to finish within 10 minutes. Short smokes/prechecks receive tight observation because they exist to produce cheap feedback. If observation contradicts the model, reopen the controlling code, query/plan, tool/workflow dataflow, and resource assumptions before extrapolating or assigning cause.

The executor detects rising unit cost, repeated work, stalled or implausibly fast progress, idle required resources, absent artifacts, and coverage gaps without waiting for user complaint. Before attributing cause, compare semantic progress and CPU/I/O/memory/network/queue/accelerator evidence against rival data-volume, hardware/I/O, remote-wait, bug/incomplete-coverage, complexity/repeated-work, and lock/topology causes. Necessary scale and avoidable design cost may coexist.

Stop/fence and repair an anomaly that can damage correctness, decisions, critical path, bounds, or descendants. A sound near-complete run may finish when integrity/progress hold and restart costs more. Prepare a future fix concurrently only after dependency, provenance, write-scope, and epoch analysis proves it cannot stale the current result or later jobs; otherwise quarantine it to the next epoch.

The executor may always safe-stop. It may not self-resume a binding pause, expand scope or effects, hide contrary evidence, treat timeout as approval, or contaminate a blind reviewer before precommitment. A material feedback-driven change enters explicit replan, invalidates only affected descendants and permits, and preserves the prior evidence and epoch trail.

Observer and blind reviewer remain distinct: the observer protects live execution and may pause/veto; the reviewer independently adjudicates meaning, results, and claims. Never combine them when independent review is required or requested, the observer intervened materially, or a protected/consequential claim or action depends on review. For low-risk bounded work, one runtime may perform both functions only with a reviewer precommitment frozen before observation, separate evidence sample/holdout, explicit authority and conflict accounting, and no material intervention; otherwise its epistemic opinion is advisory and a separate reviewer is required.

## Admit Insight, Then Verify It

Suddenness is a discovery signal, not a truth signal. An idea may arise spontaneously or from a bounded `InsightProbe`; either becomes an `InsightCandidate`, never evidence, approval, or an automatic plan change. Read [insight-protocol.md](references/insight-protocol.md).

Use an optional InsightProbe only when expected decision value justifies it: impasse, repeated no-new-evidence probes, unresolved contradiction, fixation risk, or a novel execution observation. Freeze the Why, constraints, failed approaches, protected invariants, evidence snapshot, and confirmation boundary; then timebox one context shift, analogy, independent framing, different evidence draw, or low-demand interval. Null output is normal. Do not mandate brainstorming, randomness, creativity roles, or unverifiable explanations.

Timestamp and provenance-label the candidate; state what assumption it challenges, observable consequences, rivals, cheapest falsifier, safety/scope implications, and contamination. Do not fabricate why it appeared. Screen authority and safety first, then run the cheapest discriminating falsifier, then untouched confirmation proportionate to the claim. A context-separated reviewer scores evidence rather than novelty, eloquence, confidence, or Aha intensity.

Insight may add a rival interpretation or propose a replan. It never waives a veto, authorizes sensitive access/effects, changes the success criterion post hoc, or directly promotes a general claim. Quarantine candidates that cannot be safely tested; preserve null and negative results.

## Apply The Thin Reliability Kernel

Read [reliability-kernel.md](references/reliability-kernel.md). Apply proportionally:

- close authority, freshness, applicability, conflicts, semantics, and evidence gaps for consequential claims;
- bind protected authorization to action, stage, evidence, snapshot, expiry, invalidation, cost/stop limits, and rollback owner;
- define observer barriers, triggers, maximum unchecked interval, direct evidence, binding pause, and same-snapshot resume authority;
- define rollback/recovery and post-rollback validation for persistent effects;
- fence restarts by epoch; cancel/drain, quarantine late output, and review resume state;
- enforce critical capability/authority floors and quarantine mismatched routes;
- invalidate dependent approval after material synthesis edits;
- record reproducibility and exact candidate/workspace/install parity at trust boundaries.

Use claim-scoped partial invalidation; read [evidence-provenance-and-reuse.md](references/evidence-provenance-and-reuse.md). A changed root hash triggers impact analysis, not a global rerun. Preserve old provenance; reuse for a new snapshot only through exact closure identity or checked non-interference/equivalence. Rescore evaluator-only changes, rerun affected producer or protected-gate closures, and quarantine unresolved reachability. Status questions and immutable out-of-closure presentation fixes do not invalidate metric or action evidence.

## Track Repository Changes

Read [change-tracking.md](references/change-tracking.md). Every repository-writing node chooses `diff_only`, `verified_checkpoint`, or `atomic_delivery`; read-only work uses `N/A`. A commit is a scoped workflow effect, never automatic proof of completion.

Before writes record base/branch/worktree, pre-existing dirty paths/hunks, allowed scope, canonical writer, hooks/protected effects, commit authority, verification, rollback, and separate push/PR/merge/deploy authority. Preserve user changes. Never broad-stage a dirty shared tree; stage exact owned paths/hunks and inspect the staged diff.

Before costly or broad tests, inspect the controlling code and owned diff, dataflow, invariants, affected consumers, and test topology; estimate test cost and choose the cheapest check that can falsify the change. Run focused affected-surface checks first and broaden only on changed risk or at a coherent checkpoint or trust boundary. After failure, inspect its cause and controlling code before retrying; never rerun an unchanged suite under an unchanged hypothesis. Passing tests cannot rescue unreviewed topology, asymptotics, integrity, or compatibility. A cheap local lint, type check, targeted unit test, or bounded reproduction may follow an inline code/diff review without another artifact or agent.

Resolve `N/A`, `diff_only`, `verified_checkpoint`, or `atomic_delivery` before the first repository mutation, and recheck exact commit authority immediately before any commit command; absent authority deterministically means `diff_only`.

Commit one coherent, revertable semantic unit only when the exact staged tree passed applicable tests, compatibility and sensitive-payload scans, hooks, and review. Verify commit parent/tree/paths and residual user dirtiness afterward; bind the commit to workflow epoch, candidate, and evidence hashes. Parallel writers use disjoint authorized worktrees/branches or return patches. Prefer correcting/revert commits; never destructively rewrite shared history or auto-push.

## Preserve Independent Judgment

Independence is an `IndependenceSpec`: initial framing exposure; evidence universe and independent sample; overlap ceiling; source/tool/model diversity when it changes error correlation; holdout and contamination; authority; and conflicts of interest. Shared mental models cover boundaries, interfaces, and safety—not conclusions. Preserve disagreement until a discriminating probe resolves it or report scoped uncertainty. Majority agreement is not evidence.

## Learn And Evolve Skills

Read [skill-evolution.md](references/skill-evolution.md). For material reusable-policy changes, use an independent SkillEvolutionExpert when failure locus, interaction, topology, autonomy, safety, observation, or transfer is uncertain. Diagnose `policy_gap`, `policy_ambiguity`, `activation_failure`, `execution_failure`, `verification_gap`, `capability_or_environment_gap`, or `interaction_failure` before editing permanent instructions.

Before the first material reusable-policy edit, create a proportional `EvolutionEvidencePlan` and reserve its baseline, candidate, and independent-scoring nodes. Use the compact incident-backed path only for a narrow additive interaction clarification that does not relax topology, autonomy, safety, authority, model floors, or protected effects: freeze the baseline incident, corrected case, one surface-distant transfer, one non-example or protected interaction, rubric, hard failures, candidate execution, independent score, and at most one changed-evidence retry. Use the full plan for broader changes, protected-policy changes, or any compact-path collision or failure. Deterministic implementation, formatting, and package-sync work with unchanged policy use objective checks instead.

Apply entailment, deletion, substitution, and collision tests. Record every exact producing snapshot. Promote only after the final candidate passes every criterion in its proportional plan with independent scoring and same-snapshot evidence or a checked identity/equivalence edge. Map post-run edits to affected producers, inputs, evaluators, topology, and protected-gate closures; rerun or rescore only intersecting claims. Keep prompts and answer keys outside the installed skill.

## Model Routing

Read [model-routing.md](references/model-routing.md). Route by the hardest consequential duty, not patch size or role title. Preserve the v4 floor: Luna-low defaults for mechanical work, Terra-medium for bounded known-design implementation, exact `gpt-5.6-sol`/`high` for consequential architecture/topology/risk/safety/skill review/careful-full observation, and exact `gpt-5.6-sol`/`ultra` for experiment design, analysis, and independent experiment review. There is no downward fallback for critical routes.

Record requested, selectable, accepted, enforceable, and attested route separately. Never infer model/config from an agent name or accepted field. If identity/effort cannot be selected or attested, state `unavailable` and keep critical output advisory; review can elevate it only when the reviewer's own capability floor and independence are separately attested and the reviewer reconstructs the critical reasoning from raw evidence. Rubber-stamp approval cannot launder an unattested result. When the user requires waiting for the correct route, capacity never authorizes downgrade; continue only non-conflicting work while waiting.

## Finish

One synthesizer reports proportionally. Direct and compact work reports the outcome, decisive evidence and checks, material deviations, residual uncertainty, terminal cleanup, and output links. Careful and full work additionally reports the applicable DAG/timing, sampling, interventions, insight validation, validity layers, reliability controls, disagreements, and reviewer/observer decisions. Do not manufacture empty ledgers. At a trust boundary verify exact artifact parity after the last material edit. Never call a reproducible result valid while its meaning or claim remains unresolved.
