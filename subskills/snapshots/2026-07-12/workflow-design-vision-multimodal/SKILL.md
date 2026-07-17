---
name: workflow-design-vision-multimodal
description: Use with multi-agent-workflow-designer when designing workflows for computer vision, image/video understanding, OCR, document AI, visual inspection, product tagging, multimodal models, or visual policy/safety systems. Emphasize data representativeness, annotation quality, slice robustness, privacy, visual QA, and actionability.
---

# Workflow Design: Vision/Multimodal

This domain subskill supplies vision and multimodal deltas to `multi-agent-workflow-designer`. It does not replace the parent workflow.

## Trigger

Use as the primary domain when visual-inference validity dominates the supported action and failure risk in image, video, OCR, document AI, detection, segmentation, classification, visual search, inspection, product tagging, visual moderation, or multimodal reasoning. Keep policy/governance primary for clinical triage or rights-affecting decisions when authority and human harm dominate; use Vision as a borrowed lens there.

## Parent Contract

- The parent owns real-subagent creation, runtime topology, ledgers, observer/restart behavior, permits, mutation ownership, synthesis, and final acceptance.
- Review perspectives below are competencies, never real or virtual agents. The parent maps required perspectives to real runtime owners and records their IDs.
- Each gate record needs `gate_id`, `action_stage`, `proof_phase=entry|result`, `applicability=applicable|not_applicable|unresolved`, and `applicability_evidence_refs`. Only `applicable` gates receive `decision=pass|fail|escalate`, with evidence and blocked commitments; `not_applicable` needs positive scope evidence and a reopen trigger, while `unresolved` blocks.
- Source claims require authority, rights/use compatibility, lineage, `observed_at`, effective version/date when available, deployment applicability, and retrieval status. Missing or stale high-impact facts remain unknown.
- Unknowns that could change capture, labels, modality, architecture, privacy, threshold, owner workflow, rollout, schedule, or scope cannot authorize execution or be invented.

## Domain Ledger Additions

- Visual task, target user/action, deployment surface, and failure cost.
- Asset source, capture device/environment, geography, rights, consent, retention, and lineage.
- Taxonomy, annotation instructions, reference standard, agreement/adjudication, and uncertain-label policy.
- Split unit, near-duplicate or asset-family policy, video boundaries, and slice coverage.
- Modality-specific contract for OCR layout/fields, video events/time, or multimodal pairing/grounding.
- Human review, override, appeal, correction, latency, fallback, monitoring, and rollback.

## Domain Gates

| Gate | Pass condition | Required proof |
| --- | --- | --- |
| `VM-G1` VisualUseCaseSourceClosure | The visual signal supports a defined action and assets are authoritative, lawful, representative, and usable for the planned purpose. | `VisualUseCaseSourceReport` with scenario/action map, source inventory, rights/consent, lineage, capture conditions, retention, and unresolved gaps. |
| `VM-G2` ReferenceStandardValidity | Taxonomy and labels distinguish the decision-relevant states with measured agreement and adjudication. | `ReferenceStandardReport` with instructions, provenance, inter-annotator results, disagreement slices, adjudication, uncertainty policy, and sampled visual QA. |
| `VM-G3` SplitLineageIntegrity | Splits prevent duplicate, identity, asset-family, location, document-template, and temporal leakage. | `SplitLineageReport` with split unit/rationale, hashes or lineage links, dedup tests, temporal boundary, and contamination findings. |
| `VM-G4` CoverageRobustness | Evaluation covers critical populations, environments, devices, corruptions, rare states, and protected slices. | `CoverageRobustnessReport` with deployment-to-data matrix, slice metrics/uncertainty, stress tests, sampled failures, and known unsupported conditions. |
| `VM-G5` EndToEndModalityValidation | The complete modality pipeline is validated against the actual downstream action. | `ModalityValidationReport`: OCR includes page/layout-to-critical-field and invalid-document tests; video includes clip/event/track and temporal-boundary/latency tests; multimodal includes pairing/alignment, ablation, missing/conflicting modality, grounding, and shortcut tests. |
| `VM-G6` ActionHumanSafety | Thresholds, human review, privacy, appeals, fallback, and rollback match the cost of false and missed actions. | `ActionHumanSafetyReport` with decision-cost matrix, threshold/capacity analysis, review protocol, privacy controls, override/appeal, fallback, monitoring, and residual-risk owner. |

## Safe Start And Protected Actions

Before an execution permit, safe start is limited to read-only asset/schema inventory, rights and lineage review, deidentified sample inspection, annotation-spec design, and synthetic or disposable scratch smoke tests that cannot change shared repository/environment state. Shared evaluation harnesses or annotation artifacts require a scoped permit. Diagnostic samples cannot support deployment claims.

Keep bulk collection, annotation procurement, sensitive-asset exposure, dataset mutation, training, threshold tuning, production integration, automated people-affecting decisions, experiments, and rollout blocked until their action-stage gates pass. A bounded annotation/evaluation/training step may receive a `validation` permit after entry gates pass; result reports remain due and downstream claims, decisions, and rollout stay blocked.

## Reviewer Perspectives

- Annotation and reference-standard validity.
- Slice, capture-condition, and visual failure analysis.
- OCR, video, or multimodal pipeline validity as applicable.
- Product/actionability and human factors.
- Privacy, fairness, policy, safety, legal, or domain expertise for faces, biometrics, minors, medical, workplace, identity, or enforcement contexts.

## Borrowed Lenses

- `workflow-design-search-ranking-recsys` when outputs affect retrieval, recommendation, taxonomy browse, or exposure.
- `workflow-design-policy-governance` for moderation, eligibility, enforcement, appeal, or people-affecting decisions.
- `workflow-design-llm-nlp` for OCR downstream language, generated text, VQA, or multimodal agents.
- `workflow-design-ops-forecasting-optimization` when detections trigger physical inspection, restock, routing, or maintenance.
- `workflow-design-product-business-decision` when model metrics must translate into adoption and business action.

## Simplification Rules

- A read-only inspection of a small, user-supplied, non-sensitive image set may use `VM-G1`, compact `VM-G2`, and visual QA from `VM-G5`; compact `VM-G2` still defines field/class semantics and includes independent spot-check or adjudication. No deployment or generalization claim is allowed.
- OCR, video, and multimodal proof branches apply only to their actual modality. A branch is `not_applicable` only after the input/output contract proves it is absent.
- `VM-G3` and `VM-G4` may be `not_applicable` only for a bounded supplied-set contract with no train/eval split, deployment population, robustness, or generalization claim. `VM-G6` remains applicable whenever outputs trigger consequential action or process sensitive data.
- Simplification reduces coordination only after applicability is recorded; it does not turn sample inspection into product evidence.

## Blocking Failure Modes

Block the affected commitment when labels are not decision-relevant, lineage or rights are unknown, aggregate metrics hide critical slice failures, modality-specific validation is absent, sensitive visual data is unowned, or no operator can act on and correct the output.

## V4 Runtime Handoff

Return marginal deltas to v4. Barriers are source/rights closure, reference-standard review, split lock, modality evaluation, threshold/human-workflow review, and rollout. Emit parent feedback for rights/consent/lineage gaps, annotation-disagreement spikes, duplicate leakage, unsupported capture slices, modality shortcuts/conflicts, or human-review overload. Link direct evidence without unnecessary sensitive disclosure and invalidate affected gates only. A novel augmentation, OCR heuristic, fusion, or visual feature is an `InsightCandidate`; freeze shortcut/capture rivals, cheapest visual falsifier, untouched asset-family/device/layout confirmation, and contamination. Independent visual spot-check is review, not observer approval.

## Domain Gate Packet

```text
DomainGatePacket:
  parent_contract_version: v4
  packet_domain: Vision/Multimodal
  routing_role: primary|borrowed
  primary_domain: set by parent
  route_reason: dominant validity/risk or marginal domain delta
  marginal_gate_delta: [question, gate, proof, trigger, or protected action changed]
  omit_or_exception_reason: [plausible lens omitted or default-two exception]
  ledger_additions: [field=value ...]
  knowledge_sources: [source, authority, rights, observed_at, effective_version_or_date_when_available, applicability, status]
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
| Extract totals and dates from a supplied invoice set. | Define critical fields, invalid-document handling, layout-aware visual QA, and the narrow no-generalization scope before using a compact path. |
| Detect safety events in factory video. | Require event boundaries, temporal leakage controls, rare-event coverage, camera-condition slices, latency, operator workflow, and false-alarm capacity evidence. |
| Auto-suspend marketplace listings using image and text signals. | Keep Policy/Governance primary and borrow Vision/Multimodal plus Product/Business; add Search or LLM only when its distinct gate, proof, observer trigger, or protected action justifies the v4 default-two exception and record marginal value in the runtime DAG. Block suspension until modality alignment, seller impact, threshold capacity, explanation, appeal, and rollback pass. |
| Triage emergency-care images across hospitals and devices. | Keep Policy/Governance primary and borrow Vision/Multimodal plus Ops. Treat source rights, clinical reference standard, site/device/population robustness, missing modalities, human override, monitoring, and unsupported conditions as release-blocking evidence. |

## Runtime Enforcement

The parent must evaluate each applicable gate as `pass|fail|escalate` against named evidence refs; prose that merely mentions a concern is not proof. Every `fail|escalate` record must list the protected action it blocks, the owner of the missing evidence, and the reopen trigger. `N/A` requires positive applicability evidence and a residual-limit statement. Do not infer visual quality, robustness, or deployment readiness from a small representative-looking sample.

## Self-Improvement Hook

After a task, emit a `DomainSkillUpdateCandidate` only when evidence shows a recurring missing trigger, slice, modality gate, reviewer perspective, or failure mode. Include task evidence and one failing-then-passing behavior test. Do not mutate the installed skill unless the user requested or approved improvement.
