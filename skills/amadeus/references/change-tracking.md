# Change Tracking And Verified Commits

Commits are scoped workflow effects, not automatic proof of progress.

## ChangeTrackingContract

For every repository-writing node choose a mode; use `N/A` when there are no repository writes.

- `N/A`: read-only diagnosis, review, status, or other work with no repository mutation and no commit.
- `diff_only`: owned repository writes are delivered as an uncommitted diff/patch because commit authority, separability, maturity, or audit value is absent.
- `verified_checkpoint`: one coherent tested commit preserves resumable recovery/audit state on an authorized isolated or local branch; it may be intermediate and is never represented as final delivery.
- `atomic_delivery`: one coherent fully validated commit is the requested or repository-required final local handoff for that semantic unit.

```text
repo_root_owner_and_policy
base_commit_branch_worktree_and_upstream
preexisting_dirty_paths_and_hunk_fingerprints
owned_paths_or_hunks_and_canonical_writer
mode, commit_authorization_source_and_scope
hooks_signing_ci_deploy_or_protected_effects
verification_and_sensitive_payload_gates
epoch_candidate_and_evidence_fingerprints
rollback_or_revert_owner
push_pr_merge_deploy_authority
failure_disposition
```

Inspect local status, diff, instructions, hooks, and conventions before writes. Classify existing paths/hunks as `user_owned`, `workflow_owned`, or `ambiguous`. Dirtiness never implies ownership.

For a cheap local reversible edit in a clean or clearly separable tree, record only an inline compact form: `mode, base, owned_scope, preexisting_dirty, objective_check, commit_authority`. Expand to the full contract for commits, dirty/ambiguous/shared trees, concurrent writers, protected effects, consequential changes, or policy-triggered hooks. Do not burden a tiny rename with branch topology, agents, or commit ceremony unless the user or repository requires a commit.

## Commit Decision

Resolve mode and exact local commit authority before the first commit command. If commit authority for the exact scope is absent or unresolved, select `diff_only`; do not attempt a commit as a probe and do not infer commit authority from permission to edit, build, test, or deliver a patch. An effect-tool rejection cannot supply or validate commit authority.

Create a local commit only when:

- an explicit user instruction, repository policy, or established task workflow supplies local commit authority for the exact scope; ordinary permission to edit/build does not automatically authorize a commit;
- the change is one coherent, revertable semantic unit with recovery/audit value;
- exact owned scope is separable from user work;
- the staged tree is the tree that passed applicable tests, compatibility checks, and secret/PII/raw-payload scans;
- hooks/signing requirements can run without bypass;
- the commit does not implicitly push, deploy, publish, or mutate a protected branch.

Use `diff_only` for incomplete/advisory patches, ambiguous overlap, unavailable identity/signing requirements, or useful uncommitted edits. Read-only diagnosis is `N/A`, not `diff_only`. A `verified_checkpoint` on an isolated workflow branch may preserve useful incomplete recovery state only when clearly labeled and not represented as valid completion. Use `atomic_delivery` only after final acceptance checks for the semantic unit pass.

## Dirty Trees And Staging

Preserve user changes. Never use destructive reset/checkout/clean to obtain a clean tree. Do not use broad `git add .` or `git add -A` in a dirty shared tree. Stage exact owned paths or hunks; inspect the staged diff, compare with the ownership ledger, and leave unrelated changes in their original state. If owned and user hunks overlap ambiguously, use an authorized isolated branch/worktree from the agreed base or pause the affected write.

One canonical writer owns a branch/worktree/epoch. Parallel implementers use disjoint authorized worktrees/branches or return patches/change packets without committing. The coordinator integrates only fresh-parent, independently verified changes and reruns affected joins; reviewers and observers do not commit artifacts they independently judge.

## Code Review Before Broad Verification

Before a costly or broad test/build/evaluation, freeze the proportional review and verification ladder:

```text
CodeImpactReview:
  candidate_snapshot_and_owned_diff
  controlling_code_and_dataflow
  invariants_and_contracts
  affected_consumers_and_surfaces
  topology_complexity_integrity_or_compatibility_risks
  test_topology_and_estimated_cost
  review_gaps_and_evidence_refs

VerificationPlan:
  cheapest_focused_falsifier
  affected_test_set_and_oracles
  expansion_trigger
  full_suite_justification_or_NA
  coherent_checkpoint_or_trust_boundary
  stop_on_failure
  retry_requires_changed_evidence
```

Map each check to the reviewed surface. Use `code/diff review → cheap static/schema/syntax check → focused affected tests → broader suite when triggered`. Full-suite entry requires cross-cutting impact, compatibility or protected invariants, a release/trust boundary, repository/user mandate, or an exact coherent checkpoint—not merely an available command. Mandatory hooks, security scans, release checks, and requested acceptance suites remain applicable. A passing test establishes only its oracle and covered surface; testing a different tree does not verify the candidate.

For a tiny local change, one inline record—`reviewed exact diff + affected invariant → targeted objective check`—is sufficient. “Thorough” means complete for plausible affected contracts and risks, not exhaustive repository reading or a new agent. Docs/format-only work uses link/lint/render checks; a bounded regression reproduction may run after inspecting its immediate code path.

## Verification And Evidence Binding

Before commit: inspect exact status and staged diff; inspect generated/binary/LFS content; scan secrets, PII, raw payloads, and private evaluation keys; run required review gates. Compute the staged tree OID, materialize that exact tree in an isolated clean checkout/worktree, and run semantic tests plus applicable format/type/static/schema/API checks against it. This is the tested staged tree. If isolation is unavailable, record workspace/index/generated/untracked fingerprints and prove every relevant tested byte equals the staged tree; any relevant unstaged/untracked ambiguity blocks commit.

Run hooks without bypass. If a hook changes the index, generated files, or tested content, compute a new staged tree OID and rerun every affected check on the new exact tree. Record the final tested staged tree OID immediately before commit.

After commit verify:

```text
commit_hash_and_parents
tested_staged_tree_oid
commit_tree_oid_and_exact_equality_to_tested_staged_tree
expected_branch_and_owned_paths_only
message_and_trailers_truthful
residual_worktree_matches_preexisting_user_state
affected_descendant_evidence
```

Bind each commit to workflow epoch, candidate/source/config/fixture hashes, and verification evidence. A commit does not validate policy. Any semantic edit creates a new candidate fingerprint and triggers the claim-scoped impact analysis in [evidence-provenance-and-reuse.md](evidence-provenance-and-reuse.md); exact staged-tree and install/release checks still apply, but unrelated semantic evidence does not rerun without an intersecting dependency. A final commit may cite retained evidence only through an explicit identity or equivalence certificate and never rewrites its original provenance. Keep policy/candidate, evaluation evidence, and generated documentation in separate coherent commits when their rollback or validation boundaries differ.

Follow repository message conventions. Otherwise use an imperative scoped subject and a body explaining why, behavioral/compatibility change, invalidation, and checks. Factual trailers such as `Workflow-Epoch`, `Evidence-Snapshot`, `Verification`, and `Change-Owner` are allowed. Never fabricate human, reviewer, model, or coauthor identity.

## Effects And Recovery

Local commit authority is not authority to push, open a PR, merge, deploy, or publish. Treat hooks that trigger costly CI, external effects, data exposure, or deployment as protected actions with their own permit and rollback.

Prefer a new correcting or `git revert` commit for shared history. Amend/rebase is limited to isolated unpublished workflow branches with no consumers and explicit policy support. Never force-push or destructively rewrite shared/user history without exceptional explicit authority. A code revert does not reverse data or external effects; those need their own recovery path.
