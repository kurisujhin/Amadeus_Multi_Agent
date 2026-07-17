# Disciplined Insight Protocol

## Status

An `InsightCandidate` is a provenance-labeled hypothesis. Suddenness, confidence, pleasure, surprise, novelty, or model eloquence may help triage attention but never establish truth, safety, authorization, or decision value.

## Optional InsightProbe

Trigger only on expected decision value: impasse, two no-value probes, unresolved contradiction, plausible fixation, or an unexpected opportunity. Before probing, freeze:

- Why, claim/action, and success/counter-metrics;
- constraints, protected invariants, authority, and mutable scope;
- attempted paths, current rivals, evidence snapshot, and confirmation holdout;
- time/probe budget and stop rule.

Use one bounded context shift: independent framing, analogy, different modality or evidence sample, constraint relaxation in scratch space, or a low-demand interval for a human participant. Count it against the inquiry budget. Null output is a valid result. Do not repeatedly incubate without changed evidence.

## InsightCandidate

```text
candidate_id, captured_at, origin_context, provenance
candidate_claim_or_action
assumption_or_interpretation_challenged
novelty_relative_to_attempted_paths
predicted_discriminating_observations
rival_explanations, cheapest_falsifier
authority_safety_scope_effects
evidence_used, confirmation_contamination
subjective_suddenness_or_confidence_optional
status: captured | screened_out | testing | rejected | supported_scoped | quarantined
```

Do not fabricate a causal narrative for opaque provenance. Evaluate observable consequences.

## InsightValidationGate

1. Screen authority, privacy, safety, scope, and testability. Recording an idea is not authorization to access or act.
2. Freeze falsifiable implications and rivals before new result evidence.
3. Run the cheapest discriminating falsifier; search for counterexamples and relevant prior evidence.
4. Compare with baseline or unchanged plan and test sensitivity.
5. Use untouched confirmation proportionate to generality and consequence.
6. Obtain context-separated review of evidence, contamination, semantics, and claim scope.

The gate returns `reject`, `support_scoped`, `needs_evidence`, or `quarantine`. Promotion changes the inquiry state only through explicit replan and partial invalidation. Protected downstream action still requires its permit.

## Anti-Patterns

- creativity quotas, mandatory brainstorming, or automatic extra agents;
- treating an Aha feeling, novelty, or consensus as evidence;
- post-hoc success criteria or reconstructed prediction;
- exposing holdouts during generation;
- sharing the candidate with a blind reviewer before precommitment;
- covert scope expansion, sensitive retrieval, or effectful probing;
- endless idea search after the circuit breaker fires.
