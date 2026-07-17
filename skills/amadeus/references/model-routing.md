# Capability And Model Routing

Route by the hardest consequential duty, not patch size, token count, or role title.

## Consequence Classes

```text
R0 mechanical: inventory, hashes, exact commands, formatting, polling, predefined metrics
R1 bounded: implementation with known design and objective tests
R2 consequential-critical: algorithm, complexity, dataflow, topology, concurrency,
                           backpressure, distributed state, schema/integrity,
                           performance validity, risk/safety/privacy/authority,
                           skill review, careful/full observation
R3 experiment-critical: experiment design, analysis, and independent experiment review
```

Use the exact high-reasoning architecture-capable floor below for R2 and the exact experiment-critical floor for R3, preserving independent review. If one contract mixes classes, split at an objective handoff or route the unsplittable contract to the highest class. A mechanical operator may run a frozen experiment, but cannot adapt design, exclude results, choose winners, or make conclusions.

V5 preserves the v4 critical floor until matched evidence justifies a change:

- R0 mechanical defaults to `gpt-5.6-luna` at `low`; `gpt-5.6-terra` at `medium` is the upward-capability fallback.
- R1 bounded implementation defaults to `gpt-5.6-terra` at `medium`; upward fallback to Sol-high is allowed.
- R2 consequential architecture, topology, risk/safety, skill review, and careful/full observation require exact `gpt-5.6-sol` at `high` or stronger Sol reasoning.
- R3 experiment design, analysis, and independent experiment review require exact `gpt-5.6-sol` at `ultra`.

There is no downward fallback for R2/R3. “Available” means available while meeting this floor; it never lowers it. If the exact route cannot be selected and attested, wait when user policy requires waiting, otherwise narrow or withhold the critical design, mutation, action, and conclusion.

## Routing Ledger

Before dispatch record:

```text
contract_and_consequence_class
failure_cost_and_required_capabilities
requested_model_and_reasoning
selectable_fields
accepted_dispatch_fields
enforceable_constraints
reported_runtime_identity
attestation_source
fallback_or_wait_policy
output_authority_if_unattested
```

For R2/R3 implementation, a qualified and attestable route record plus qualified origination or independent reconstruction of the controlling design is a hard dependency of design-dependent mutation. An unattested runtime may inspect, diagnose, measure, and return an advisory design, but it may not begin topology-, concurrency-, asymptotic-, integrity-, or performance-validity-dependent implementation. A qualified owner or reviewer may first freeze an exact implementation contract; only duties that are then genuinely R0/R1 may be handed to a lighter mechanical implementer. Post-mutation review or passing tests cannot launder an implementation that crossed this barrier without the required capability.

Tests may diagnose an R2/R3 design while its route is pending, but passing tests cannot authorize or launder unreviewed asymptotic, dataflow, concurrency, backpressure, integrity, schema, or performance-validity decisions. Qualified review of the controlling design precedes design-dependent mutation; representative tests then verify the frozen contract.

```text
RouteEdgeDisposition:
  work_item
  consequence_class: R0 | R1 | R2 | R3
  route_state: not_applicable | requested | accepted_attested | unavailable
  requested_accepted_enforceable_attested_refs
  qualified_design_owner_or_reconstruction_ref
  allowed_next: diagnose | safe_stop | advisory_design |
                frozen_contract_mechanical_implementation | design_dependent_mutation
```

`requested`, planned delegation, or a generic route requirement is not `accepted_attested`. While the edge is unsatisfied, R2/R3 diagnosis, measurement, safe-stop, and advisory alternatives remain allowed, but design-dependent mutation and any unconditional repair/rerun commitment remain blocked. After a qualified owner freezes an exact design contract, only genuinely R0/R1 execution may be delegated mechanically.

`route_state=not_applicable` requires positive evidence that the work is R0/R1; it is invalid for R2/R3. For R2/R3, both `requested` and `unavailable` restrict `allowed_next` to diagnose, safe-stop, or advisory design.

`allowed_next=design_dependent_mutation` is valid if and only if `route_state=accepted_attested`, the requested/accepted/enforceable/attested references are nonempty, and a qualified design owner or reconstruction reference is nonempty.

Requested is not accepted; accepted is not enforced; enforced is not attested. Never infer hidden model identity from prose, agent confidence, task name, or an accepted field that the runtime does not report. If model/config cannot be selected or attested, say `unavailable` and keep critical output advisory. Independent review may elevate it only when the reviewer's own model/capability floor and independence are separately selectable, enforceable, and attested **and** the reviewer independently reconstructs or re-executes the critical reasoning from raw evidence under that floor. Approval or critique of the unattested output alone is a rubber stamp and remains advisory; two unattested agents cannot launder one another's output. Otherwise wait, narrow, or withhold. Do not fabricate model, reasoning effort, seed, or runtime identity.

When the user requires waiting for the correct model/route, capacity pressure does not authorize downgrade. Keep waiting within the task's declared wait/monitor policy and continue only non-conflicting work. Otherwise, a fallback must meet the same capability floor or narrow the claim/action; never silently lower a safety or experiment-review floor.

## Implementation Routing Trigger

Treat implementation as R2 or R3 when correctness depends on any of:

- asymptotic behavior or work amplification at real scale;
- partitioning, fan-out/fan-in, joins, caches, indexes, provenance, or invalidation;
- CPU/I/O/network/accelerator topology and resource utilization;
- concurrency, ordering, idempotence, backpressure, memory bounds, or cancellation;
- schema semantics, privacy retention, integrity, compatibility, or online latency;
- experiment estimand, cohort, metric, stopping, selection, or result interpretation.

Require the implementation owner to state intended complexity/dataflow, failure and scaling signatures, resource topology, and validation at representative scale. A light patch review cannot rubber-stamp an architecture decision it did not originate or independently reconstruct.

## Model Experiments

Compare routes only when identity/config are actually selectable and attestable, tasks are sanitized and matched, budgets are frozen, and an independent reviewer is reserved. If the environment cannot meet these controls, record a capability gap; do not manufacture a winner from agent names or subjective output quality.
