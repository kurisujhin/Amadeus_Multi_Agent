---
name: workflow-design-vision-multimodal
description: Use with multi-agent-workflow-designer when designing workflows for computer vision, image/video understanding, OCR, document AI, visual inspection, product tagging, multimodal models, or visual policy/safety systems. Emphasize data representativeness, annotation quality, slice robustness, privacy, visual QA, and actionability.
---

# Workflow Design: Vision/Multimodal

This domain subskill supplies vision and multimodal deltas to `multi-agent-workflow-designer`. It does not replace the parent workflow.

## Trigger

Use as the primary domain when visual-inference validity dominates the supported action and failure risk in image, video, OCR, document AI, detection, segmentation, classification, visual search, inspection, product tagging, visual moderation, or multimodal reasoning. Keep policy/governance primary for clinical triage or rights-affecting decisions when authority and human harm dominate; use Vision as a borrowed lens there.

## Native V5 Parent Boundary

Emit marginal domain semantics only; the v5 parent owns workflow and effects as defined in `../SNAPSHOT.md`. This skill never issues permits, creates agents, chooses commit mode, resumes pauses, authorizes effects, or mutates canonical state.

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

## Native V5 Domain Delta

- `work_model_delta`: assets/pages/frames/tracks/regions/pairs×capture slice; decoding/annotation/model fan-out; lineage, duplicates, disagreement, device/layout coverage and modality alignment.
- `human_input_deltas`: asset rights, taxonomy/reference authority, action thresholds, sensitive use, collection scope, and review capacity.
- `action_delta`: protect collection/annotation procurement, sensitive exposure, training, thresholds, and automated decisions.
- `anomaly_delta`: rights/lineage gap, disagreement spike, duplicate leakage, unsupported capture slice, shortcut/conflicting modality, review overload; distinguish taxonomy, annotator, capture, duplicate, shortcut, and modality rivals using source chain, clusters, disagreement samples, and modality/device/layout slices.
- `change_impact_delta`: rights/consent/asset/taxonomy/split/device/layout/modality/threshold/review-workflow changes invalidate source, reference, lineage, robustness, modality, and human-safety evidence.
- `insight_constraints`: preserve rights, reference authority, sensitive-use limits, threshold and human-review capacity; use shortcut/capture falsifiers and untouched device/layout confirmation. Visual review never substitutes for parent observer approval.

## Native V5 Packet

Emit the complete `v5-domain-1` packet from the named domain sections with producer snapshot/fingerprint. The parent router and `../SNAPSHOT.md` own schema and authority rules. Reject unknown top-level fields; optional additions belong only in a namespaced `extensions` map.

## Behavior Tests

| Task | Expected behavior |
| --- | --- |
| Extract totals and dates from a supplied invoice set. | Define critical fields, invalid-document handling, layout-aware visual QA, and the narrow no-generalization scope before using a compact path. |
| Detect safety events in factory video. | Require event boundaries, temporal leakage controls, rare-event coverage, camera-condition slices, latency, operator workflow, and false-alarm capacity evidence. |
| Auto-suspend marketplace listings using image and text signals. | Keep Policy/Governance primary and borrow Vision/Multimodal plus Product/Business; add Search or LLM only when its distinct gate, proof, observer trigger, or protected action justifies the parent default-two exception and record marginal value in the runtime DAG. Block suspension until modality alignment, seller impact, threshold capacity, explanation, appeal, and rollback pass. |
| Triage emergency-care images across hospitals and devices. | Keep Policy/Governance primary and borrow Vision/Multimodal plus Ops. Treat source rights, clinical reference standard, site/device/population robustness, missing modalities, human override, monitoring, and unsupported conditions as release-blocking evidence. |
