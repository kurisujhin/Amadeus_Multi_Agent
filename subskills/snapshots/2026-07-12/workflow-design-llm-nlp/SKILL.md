---
name: workflow-design-llm-nlp
description: Use with multi-agent-workflow-designer when designing workflows for LLM, NLP, RAG, prompt evaluation, agentic language apps, summarization, extraction, classification, chatbot, tool-use, or model-comparison tasks. Emphasize source grounding, eval validity, hallucination controls, prompt/model versioning, safety, latency, cost, and user workflow fit.
---

# Workflow Design: LLM/NLP

This domain subskill supplies LLM/NLP-specific deltas to `multi-agent-workflow-designer`. It does not replace the parent workflow.

## Trigger

Use as the primary domain for LLM apps, chatbots, RAG, agents, tool use, summarization, extraction, classification, translation, prompt evaluation, model comparison, benchmarks, or generated language. Use as a borrowed lens when another domain generates explanations, interprets natural language, or uses an LLM as an evaluator.

## Parent Contract

- The parent owns real-subagent creation, runtime topology, ledgers, observer/restart behavior, permits, mutation ownership, synthesis, and final acceptance.
- Review perspectives below are competencies, never real or virtual agents. The parent maps required perspectives to real runtime owners and records their IDs.
- Return domain deltas through a `DomainGatePacket`. Each gate record needs `gate_id`, `action_stage`, `proof_phase=entry|result`, `applicability=applicable|not_applicable|unresolved`, and `applicability_evidence_refs`. Only `applicable` gates receive `decision=pass|fail|escalate`, with evidence and blocked commitments; `not_applicable` needs positive scope evidence and a reopen trigger, while `unresolved` blocks.
- A source-dependent claim is closed only with authority, `observed_at`, effective version/date when available, task applicability, and retrieval status. Missing or stale high-impact facts remain unknown.
- An unresolved fact that could change architecture, corpus, model, tool permissions, evaluation, safety posture, rollout, owner, threshold, schedule, or scope cannot authorize execution or be filled in by invention.

## Domain Ledger Additions

- Language task, output contract, target users, scenario, and supported action.
- Source of truth or grounding corpus, including index and document versions.
- Model, prompt, tool, retrieval, policy, and decoding versions.
- Evaluation population, gold source, judge protocol, holdout boundary, and evidence standard.
- Failure costs for hallucination, omission, refusal, leakage, prompt injection, unsafe tool effects, and overconfidence.
- Latency, cost, privacy, retention, human escalation, and rollback constraints.

## Domain Gates

| Gate | Pass condition | Required proof |
| --- | --- | --- |
| `LLM-G1` TaskOutputContract | Correctness, abstention, format, user action, and failure cost are operationally defined. | `TaskOutputContract` with representative inputs, acceptable outputs, forbidden outputs, and owner-approved acceptance criteria. |
| `LLM-G2` GroundingRetrieval | Claims trace to allowed sources and retrieval works on representative and adversarial cases. | `GroundingRetrievalReport` with corpus/index versions, retrieval metrics, citation checks, unsupported-claim rate, fallback tests, and sampled failures. |
| `LLM-G3` EvalValidity | The evaluation population, labels, metrics, slices, and counter-metrics match deployment use. | `EvalValidityReport` with sampling frame, rubric, label provenance/agreement, metric rationale, critical slices, uncertainty, and error analysis. |
| `LLM-G4` EvalIsolation | Prompts, examples, retrieval, tuning, selection, and judges cannot leak or overfit the final holdout. | `EvalIsolationReport` with lineage, access boundary, dedup/contamination checks, selection history, and untouched final-test procedure. |
| `LLM-G5` JudgeValidity | Any model judge is calibrated against independent human/domain judgment for the claims it supports. | `JudgeValidityReport` with blinded comparison, agreement and bias by slice, failure taxonomy, judge/version lock, and human override rule. |
| `LLM-G6` ConfigurationRegression | Model/prompt/tool/retriever changes are versioned and replayable against baseline and known failures. | `ConfigurationRegressionReport` with immutable config, baseline deltas, failure replay, latency/cost, reproducible command, and rollback candidate. |
| `LLM-G7` AgentToolSafety | Tool permissions, injection boundaries, side effects, confirmation, idempotency, and recovery match the action risk. | `AgentToolSafetyReport` with threat cases, least-privilege map, sandbox results, side-effect ledger, confirmation rules, and recovery tests. |
| `LLM-G8` SafetyPrivacy | Safety, privacy, retention, rights, and human escalation controls cover affected users and data. | `SafetyPrivacyReport` with policy source/version, data-flow map, abuse tests, protected slices, escalation path, retention/deletion, and residual-risk owner. |

## Safe Start And Protected Actions

Before an execution permit, safe start is limited to read-only inventory, version capture, deidentified sample inspection, read-only harness design, synthetic tests, and isolated in-memory or disposable scratch smoke tests that cannot change shared repository/environment state. Shared scaffolding requires a scoped permit. Synthetic or smoke results are diagnostic and cannot support deployment claims.

Keep production prompt/model/retriever/tool changes, corpus/index mutation, training/fine-tuning, holdout tuning, privileged effects, user-facing claims, experiment ramps, and rollout blocked until their action-stage gates pass. A bounded evaluation or training step may receive a `validation` permit only after entry gates pass; its not-yet-produced reports remain under `result_gates_due`, and all claims and rollout stay blocked.

## Reviewer Perspectives

- Grounding and retrieval validity.
- Evaluation validity, isolation, and judge calibration.
- Product/user workflow and failure cost.
- Agent/tool reliability and security.
- Policy, privacy, safety, legal, or domain expertise when outputs affect rights, health, finance, education, hiring, enforcement, or other high-impact actions.

## Borrowed Lenses

- `workflow-design-search-ranking-recsys` for retrieval, ranking, exposure, and online metric alignment.
- `workflow-design-tabular-ml-evaluation` for leakage, calibration, thresholds, uncertainty, and claim discipline.
- `workflow-design-policy-governance` for people-affecting decisions, appeals, audit, and rights.
- `workflow-design-software-reliability` and `workflow-design-security-privacy` for production tools, side effects, observability, permissions, and recovery.
- `workflow-design-product-business-decision` when model quality is only useful through adoption or a supported business action.

## Simplification Rules

- A finite deterministic transformation over supplied native text, with no OCR, retrieval, judge, tuning, comparison, reusable-service claim, or external effect, may use compact gates `LLM-G1`, `LLM-G3`, and `LLM-G6`; safety/privacy still applies when data or outputs are sensitive.
- `LLM-G2` is `not_applicable` only when no external or indexed grounding is claimed. `LLM-G4` is `not_applicable` only when there is no tuning, comparison, selection, generalization, or reusable-service claim. `LLM-G5` is `not_applicable` only when no model judge supplies evidence.
- `LLM-G7` is `not_applicable` only when there is no networked, privileged, or state-changing tool path. A side-effect-free local parser inside the evaluation harness does not activate `LLM-G7`, but its version and regression evidence remain in `LLM-G6`.
- `LLM-G8` is `not_applicable` only when a data-flow and impact classification proves no sensitive data, retention, rights, safety, protected-population, or escalation obligation.
- Simplification reduces artifacts and agents only after applicability is recorded; it never weakens an applicable proof standard.

## Blocking Failure Modes

Block the affected commitment when correctness, source truth, holdout isolation, user action, tool authority, or high-impact escalation is undefined; when an eval is contaminated or unrelated to deployment; or when latency, cost, privacy, and model-version drift have no owner or evidence.

## V4 Runtime Handoff

Return marginal domain deltas to `multi-agent-workflow-designer-v4`; do not create a parallel observer or insight system. Barriers are retrieval evaluation, judge calibration, tool sandbox result, and pre-rollout configuration review. Emit parent execution feedback for unsupported claims/citation mismatch, injection or tool side effects, corpus/index/model drift, judge disagreement, or latency/cost/privacy excursion. Map direct evidence, safe-stop state, and affected gates/permits. A novel prompt, retriever, judge, or agent strategy is only an `InsightCandidate`; freeze the cheapest source-grounded or human-calibrated falsifier, untouched confirmation, and contamination. Gate pass never overrides an observer pause, and material observer intervention requires a separate claim reviewer.

## Domain Gate Packet

```text
DomainGatePacket:
  parent_contract_version: v4
  packet_domain: LLM/NLP
  routing_role: primary|borrowed
  primary_domain: set by parent
  route_reason: dominant validity/risk or marginal domain delta
  marginal_gate_delta: [question, gate, proof, trigger, or protected action changed]
  omit_or_exception_reason: [plausible lens omitted or default-two exception]
  ledger_additions: [field=value ...]
  knowledge_sources: [source, authority, observed_at, effective_version_or_date_when_available, applicability, status]
  freshness_required: [claim -> freshness rule]
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
  stop_conditions: [concrete stop or escalation trigger]
  simplification_triggers: [gate -> applicability evidence]
```

## Behavior Tests

| Task | Expected behavior |
| --- | --- |
| Extract invoice fields from supplied PDFs into JSON. | Inspect native-text versus OCR modality and finite-batch versus reusable scope; define field correctness and failure handling, and use the compact path only after proving no retrieval, judge, tuning, external effect, generalization claim, or sensitive-data expansion. |
| Build an internal FAQ RAG assistant. | Require corpus authority/freshness, retrieval and citation evidence, representative evals, access controls, fallback, and versioned regression before rollout. |
| Compare two models using an LLM judge. | Keep the quality claim blocked until holdout isolation and human-calibrated judge validity pass; do not treat judge preference as ground truth. |
| Deploy an autonomous refund agent across US and EU markets. | Keep LLM/NLP primary and borrow Policy/Governance plus Security/Privacy by default. Add Product/Business or Software/Reliability only when its distinct gate, proof, observer trigger, or protected action justifies the v4 default-two exception; record marginal value and any omitted lens. Block monetary side effects until jurisdictional rules, permissions, injection tests, appeal/escalation, rollback, and end-to-end evidence pass. |

## Runtime Enforcement

The parent must evaluate each applicable gate as `pass|fail|escalate` against named evidence refs; prose that merely mentions a concern is not proof. Every `fail|escalate` record must list the protected action it blocks, the owner of the missing evidence, and the reopen trigger. `N/A` requires positive applicability evidence and a residual-limit statement. Do not infer model quality, user intent, or production readiness from a successful smoke test.

## Self-Improvement Hook

After a task, emit a `DomainSkillUpdateCandidate` only when evidence shows a recurring missing trigger, gate, reviewer perspective, or failure mode. Include the observed task evidence and one failing-then-passing behavior test. Do not mutate the installed skill unless the user requested or approved improvement.
