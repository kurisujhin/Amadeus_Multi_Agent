---
name: workflow-design-search-ranking-recsys
description: Use with multi-agent-workflow-designer when designing workflows for search, retrieval, ranking, recommendation, feeds, ads ranking, personalization, marketplace exposure, reranking, candidate generation, or relevance evaluation. Emphasize user intent, offline-online metric alignment, bias, diversity, ecosystem effects, serving constraints, and experiments.
---

# Workflow Design: Search/Ranking/Recsys

This domain subskill supplies retrieval, ranking, recommendation, and exposure-allocation deltas to `multi-agent-workflow-designer`. It does not replace the parent workflow.

## Trigger

Use as the primary domain when ordering, retrieval, or exposure validity dominates the supported action in search relevance, candidate generation, ranking, feeds, recommendation, ads, personalization, reranking, or marketplace matching. Keep Product/Business primary for a GMV-led build or business decision, and keep Policy/Governance primary when the action is eligibility or denial rather than ordering. Record the primary-route rationale and justify any exception beyond two borrowed lenses.

## Native V5 Parent Boundary

Emit marginal domain semantics only; the v5 parent owns workflow and effects as defined in `../SNAPSHOT.md`. This skill never issues permits, creates agents, chooses commit mode, resumes pauses, authorizes effects, or mutates canonical state.

## Domain Ledger Additions

- Product surface, query/user scenario, intent classes, supported action, and affected stakeholders.
- Candidate generation, filtering, ranking, policy, blending, and presentation stages with owners and versions.
- Label/judgment provenance, logging policy, exposure mechanism, and selection/position/feedback bias.
- Offline, online, business, user, supplier, fairness, diversity, safety, and abuse metrics.
- Serving latency, freshness, capacity, availability, fallback, experiment, ramp, monitoring, and rollback.

## Domain Gates

| Gate | Pass condition | Required proof |
| --- | --- | --- |
| `SRR-G1` SurfaceSourceClosure | Surface, intent, stage boundaries, candidate eligibility, source versions, and supported action are closed. | `RankingScopeEvidence` with stage/owner map, source and policy versions, intent taxonomy, affected populations, eligibility rules, and unresolved facts. |
| `SRR-G2` StageLabelValidity | Labels and judgments represent the target intent and are attributable to the stage being changed. | `StageLabelReport` with provenance, rubric, agreement, stage attribution, sampling, critical slices, uncertainty, and disagreement analysis. |
| `SRR-G3` MetricClaimAlignment | Each metric supports the claimed user/product outcome and has baseline, counter-metrics, and bounded causal language. | `MetricClaimReport` mapping stage change to offline evidence, expected mechanism, online outcome, counter-metrics, baseline, uncertainty, and claim limits. |
| `SRR-G4` BiasExposureFeedback | Logging, position, selection, exposure, popularity, and feedback-loop biases are measured or bounded. | `BiasExposureReport` with logging-policy/version, propensity or diagnostic method, cold-start analysis, exploration assumptions, bias by slice, and mitigation tests. |
| `SRR-G5` EcosystemImpact | User, supplier/creator/advertiser, marketplace, diversity, fairness, safety, and abuse effects are explicitly traded off. | `EcosystemImpactReport` with stakeholder map, exposure distributions, concentration/coverage, protected counter-metrics, abuse cases, and residual-risk owners. |
| `SRR-G6` OnlineExperimentReadiness | Experiment unit, power, interference, ramp, guardrails, decision rule, owners, and rollback fit the surface. | `OnlineReadinessPlan` with hypotheses, allocation/unit, sample/power assumptions, novelty/seasonality, interference, guardrails, ramp, stop rules, and decision owner. |
| `SRR-G7` ServingFallbackReadiness | Latency, freshness, availability, capacity, monitoring, fallback quality, and rollback meet product constraints. | `ServingReadinessReport` with budgets, load/failure tests, freshness path, fallback cases, observability, canary/ramp, and rollback rehearsal. |

## Safe Start And Protected Actions

Before an execution permit, safe start is limited to read-only stage/config inventory, frozen versioned log diagnostics, label-policy inspection, read-only harness design, and synthetic or disposable scratch smoke tests that cannot change shared repository/environment state. Shared harness setup requires a scoped permit. Logged associations and synthetic results cannot establish online product impact.

Keep ranking/index/config/eligibility mutation, model training, new labeling spend, live exploration/exposure, experiments, ramps, product claims, and rollout blocked until their action-stage gates pass. A bounded offline evaluation/training/experiment step may receive a `validation` permit after entry gates pass; result reports remain due and product claims, allocation changes, and rollout stay blocked.

## Reviewer Perspectives

- Intent, relevance, label, and stage-attribution validity.
- Bias, causal inference, and online experimentation.
- Product, marketplace, and ecosystem impact.
- Serving reliability and fallback.
- Safety, abuse, privacy, fairness, finance, or legal expertise when exposure has sensitive or high-impact effects.

## Borrowed Lenses

- `workflow-design-product-business-decision` for GMV, conversion, retention, adoption, and strategic claims.
- `workflow-design-tabular-ml-evaluation` for leakage, calibration, thresholds, causal claims, and observational bias.
- `workflow-design-llm-nlp` for semantic retrieval, RAG, generated answers, query understanding, and LLM judging.
- `workflow-design-security-privacy` and `workflow-design-policy-governance` for abuse, sensitive personalization, eligibility, fairness, and appeals.

## Simplification Rules

- A static offline reranking study on frozen, independently judged data may mark `SRR-G4` through `SRR-G7` `not_applicable` only when it makes no online, feedback, ecosystem, serving, or rollout claim; `SRR-G1` through `SRR-G3` still apply.
- A read-only diagnosis of logged behavior may mark `SRR-G5` through `SRR-G7` `not_applicable` when it changes no allocation and makes no launch recommendation; `SRR-G4` remains applicable.
- Candidate-generation, reranking, blending, and presentation evidence may not be substituted for one another without explicit stage attribution.
- Simplification reduces coordination only after applicability is recorded and never upgrades offline association into product evidence.

## Blocking Failure Modes

Block the affected commitment when offline gains are treated as product success, clicks/GMV/engagement have no counter-metrics, logged labels have no bias analysis, a stage change is evaluated at the wrong stage, or rollout lacks serving, guardrail, owner, and rollback evidence.

## Native V5 Domain Delta

- `work_model_delta`: query/user×candidate×stage, impressions/exposures, experiment units; retrieval/ranking/blending fan-out; stage coverage, bias, diversity, latency/freshness and candidate scans.
- `human_input_deltas`: surface/intent/stage ownership, eligibility, objective tradeoffs, exploration risk, guardrails, allocation authority, and snapshot/epoch semantics.
- `action_delta`: protect index/ranker/eligibility mutation, exploration, ramp, canonical cohort/pointer changes, and online allocation.
- `anomaly_delta`: stage mismatch, label/log-policy drift, exposure/fairness breach, interference, fallback degradation, repeated scans or idle serving resources; distinguish attribution, logging drift, interference, semantic mismatch, and serving rivals using stage traces, lineage, head/tail/query/candidate slices, and topology.
- `change_impact_delta`: candidate/eligibility/assignment/label/logging/objective/stage/ranker/model/config/serving-topology changes invalidate stage attribution, bias, metric, ecosystem, serving, experiment, and affected holdout evidence.
- `insight_constraints`: offline lift cannot authorize exposure or revise counter-metrics; use the cheapest stage-correct falsifier and untouched judged/online confirmation.

## Native V5 Packet

Emit the complete `v5-domain-1` packet from the named domain sections with producer snapshot/fingerprint. The parent router and `../SNAPSHOT.md` own schema and authority rules. Reject unknown top-level fields; optional additions belong only in a namespaced `extensions` map.

## Behavior Tests

| Task | Expected behavior |
| --- | --- |
| Compare two rerankers on a frozen judged query set. | Use the offline simplification only after bounding the claim to that set; retain scope, label, metric, uncertainty, and stage-attribution evidence. |
| Improve cold-start recommendations on a homepage. | Require exposure/feedback analysis, new-user and sparse-item slices, diversity, fallback, serving, and online experiment readiness. |
| Increase marketplace GMV with personalized ranking. | Keep Product/Business primary and Search borrowed; reject GMV-only optimization until buyer, seller, concentration, trust, margin, retention, and experiment counter-metrics are owned. |
| Rank global gig workers for high-value opportunities. | Keep Search primary only while the action is ordering/exposure; reroute Policy primary for eligibility/denial. Record the route rationale and any exception beyond two lenses, then block rollout until fairness, feedback bias, explanation/appeal, fraud, jurisdiction, serving, and rollback evidence pass. |
