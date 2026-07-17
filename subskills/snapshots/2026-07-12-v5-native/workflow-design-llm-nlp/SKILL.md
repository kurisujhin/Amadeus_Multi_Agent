---
name: workflow-design-llm-nlp
description: Use with multi-agent-workflow-designer when designing workflows for LLM, NLP, RAG, prompt evaluation, agentic language apps, summarization, extraction, classification, chatbot, tool-use, or model-comparison tasks. Emphasize source grounding, eval validity, hallucination controls, prompt/model versioning, safety, latency, cost, and user workflow fit.
---

# Workflow Design: LLM/NLP

This domain subskill supplies LLM/NLP-specific deltas to `multi-agent-workflow-designer`. It does not replace the parent workflow.

## Trigger

Use as the primary domain for LLM apps, chatbots, RAG, agents, tool use, summarization, extraction, classification, translation, prompt evaluation, model comparison, benchmarks, or generated language. Use as a borrowed lens when another domain generates explanations, interprets natural language, or uses an LLM as an evaluator.

## Native V5 Parent Boundary

Emit marginal domain semantics only; the v5 parent owns workflow and effects as defined in `../SNAPSHOT.md`. This skill never issues permits, creates agents, chooses commit mode, resumes pauses, authorizes effects, or mutates canonical state.

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

## Native V5 Domain Delta

- `work_model_delta`: requests, retrieved chunks, generated/tool turns; retrieval/judge/tool fan-out; token/call cost, latency, unsupported-claim rate, corpus/index/model versions; calibrate ordinary and long-context/tool slices.
- `human_input_deltas`: output contract, authoritative corpus, failure tolerance, tool authority, and untouched boundary are user-owned when unavailable.
- `action_delta`: protect corpus/index mutation, tuning, privileged tools, and rollout; offline validation keeps result gates due.
- `anomaly_delta`: citation mismatch, injection/tool side effect, judge disagreement, corpus/model drift, token/latency amplification; distinguish corpus, retrieval, generation, rubric, judge-bias, tool, and configuration rivals using source traces, tool ledgers, an independent rubric, and version parity.
- `change_impact_delta`: output contract, governing policy, prompt/model/retriever/judge/corpus, and tool/configuration changes invalidate affected task/eval, grounding, regression, judge-calibration, tool-safety, safety, and holdout evidence.
- `insight_constraints`: preserve authoritative corpus, output/tool contract, and holdout; distinguish retrieval, corpus, generation, rubric, and judge-bias rivals with source traces and human-calibrated untouched confirmation.

## Native V5 Packet

Emit the complete `v5-domain-1` packet from the named domain sections with producer snapshot/fingerprint. The parent router and `../SNAPSHOT.md` own schema and authority rules. Reject unknown top-level fields; optional additions belong only in a namespaced `extensions` map.

## Behavior Tests

| Task | Expected behavior |
| --- | --- |
| Extract invoice fields from supplied PDFs into JSON. | Inspect native-text versus OCR modality and finite-batch versus reusable scope; define field correctness and failure handling, and use the compact path only after proving no retrieval, judge, tuning, external effect, generalization claim, or sensitive-data expansion. |
| Build an internal FAQ RAG assistant. | Require corpus authority/freshness, retrieval and citation evidence, representative evals, access controls, fallback, and versioned regression before rollout. |
| Compare two models using an LLM judge. | Keep the quality claim blocked until holdout isolation and human-calibrated judge validity pass; do not treat judge preference as ground truth. |
| Deploy an autonomous refund agent across US and EU markets. | Keep LLM/NLP primary only under a fixed authorized refund policy; make Policy/Governance primary when eligibility, rights, jurisdiction, or redress dominates. Borrow Security/Privacy for sensitive/tool effects and justify any further lens. Block monetary effects until rules, permissions, injection tests, appeal/escalation, rollback, and end-to-end evidence pass. |
