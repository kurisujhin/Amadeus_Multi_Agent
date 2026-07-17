# Evidence Provenance And Claim-Scoped Reuse

Hashes identify bytes; they do not define the causal blast radius of a change. Preserve every old artifact with its original provenance. A changed root or candidate hash starts impact analysis, not an automatic global rerun and never relabels old evidence as if new bytes produced it.

## Evidence Dependency Record

Bind evidence to the claim it actually supports:

```text
EvidenceDependencyRecord:
  evidence_id, raw_artifact_refs_and_fingerprints, observed_at
  supported_claim_ids_and_exact_scope
  producer_closure[controlling_code, modules, schemas, queries, prompts,
                   templates, generated_or_dynamic_edges, model_tool_runtime]
  effective_inputs[rendered_bytes, source_or_data_slice, cohort_and_selection_semantics,
                   config, flags, seeds]
  evaluator_closure[rubric, key, metric, threshold, scorer_code_model_and_config]
  environment_dependencies[semantic, performance, availability_only, proven_irrelevant]
  topology_dependencies[ordering, concurrency, shared_state, cache, contamination,
                        blinding, resources_and_backpressure]
  authority_freshness_permit_reviewer_dependencies_and_expiry
  unknown_dynamic_edges_and_evidence_refs
```

Separate raw execution, score, approval, permit, and release parity. Also separate semantic behavior, latency/performance, availability, and reproducibility claims. A runtime change may preserve functional evidence while invalidating latency; an evaluator change may preserve raw output while requiring rescoring.

## Change Impact Closure

For each atomic change, map direct and transitive intersections with the record, including imports, reflection, plugins, generated code, package metadata, global state, shared caches, order, and resource topology.

```text
ChangeImpactClosure:
  old_and_new_candidate_refs, atomic_change_units
  direct_intersections_and_transitive_consumers
  changed_semantics_invariants_interfaces_and_topology
  claim_by_artifact_disposition:
    retain_historical | reuse_exact | reuse_via_equivalence | rescore |
    rerun_focused | rerun_protected_gate | quarantine
  equivalence_or_non_interference_proof_refs
  uncertainty, reviewer_when_consequential
  affected_descendants_joins_and_reopen_triggers
```

Use these dispositions:

- `retain_historical`: keep truthful old output or negative evidence under its old snapshot; it does not alone support the new candidate.
- `reuse_exact`: the claim is unchanged and every dependency value and currentness condition in its closure is identical.
- `reuse_via_equivalence`: objective analysis or deterministic parity proves that old and new producer/evaluator behavior is equivalent for the claim. Path names, diff size, confidence, or unrelated passing tests are not proof.
- `rescore`: producer and effective inputs are unchanged but the evaluator changed. Keep raw output and rerun scoring only.
- `rerun_focused`: a producer/effective-input dependency, source selection semantics, prompt/model/config, shared state, order, or relevant topology changed.
- `rerun_protected_gate`: a current safety, privacy, authority, freshness, compatibility, install, release, or rollback dependency changed or expired.
- `quarantine`: dynamic reachability, dependency inventory, environment effect, topology effect, or equivalence remains unresolved. Run the cheapest discriminating dependency probe and block only mapped claims.

Choose the cheaper of an adequate consequence-proportionate non-interference proof and the affected focused rerun. A tiny change may use an inline reviewed diff plus an executable import/render/selection trace. Do not create a proof ceremony whose cost approaches the rerun. Consequential cross-cutting or dynamic changes require transitive evidence or rerun.

## Boundaries That Stay Hard

Exact final candidate, staged-tree, commit, package, hook, and installed-copy provenance remains mandatory at its trust boundary. A final claim names the final candidate and cites either evidence produced on its effective closure or an explicit checked old-to-new identity/equivalence edge.

Untouched cases freeze candidate-relevant producer, input, and evaluator contracts before reveal. A post-reveal change selected using untouched results contaminates the untouched claim; rescoring or an equivalence certificate cannot repair it. A truly out-of-closure edit may reuse behavior through independent non-interference evidence, while affected inventory/package gates still rerun.

Unknown reachability never justifies optimistic reuse or whole-repository invalidation. Quarantine the mapped claim, inspect the cheapest dependency edge, and keep unrelated branches ready.
