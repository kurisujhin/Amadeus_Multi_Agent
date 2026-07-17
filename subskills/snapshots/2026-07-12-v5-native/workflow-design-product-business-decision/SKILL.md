---
name: workflow-design-product-business-decision
description: Use with multi-agent-workflow-designer when designing workflows for product/model fit, business use cases, feature strategy, decision analysis, launch/build/buy/price/invest recommendations, market entry, GMV/conversion/retention goals, or any model/feature whose success depends on user scenario, adoption, ROI, or decision quality. Emphasize target users, scenarios, supported action, metric alignment, counter-metrics, evidence standard, and recommendation.
---

# Workflow Design: Product/Business Decision

This domain subskill supplies product, business, and decision-quality deltas to `multi-agent-workflow-designer`. It prevents implementation, experiments, or research from being mistaken for use-case success.

## Trigger

Use as the primary domain when product/model fit, adoption, economics, options, or recommendation quality is the dominant risk: build/buy/launch/price/invest/enter/pivot/stop decisions; business features or models; and GMV, conversion, retention, support, sales, marketplace health, quality, or adoption goals. Product vocabulary alone is not enough. Use as a borrowed lens whenever another domain's output matters only through a stakeholder action or owner workflow.

## Native V5 Parent Boundary

Emit marginal domain semantics only; the v5 parent owns workflow and effects as defined in `../SNAPSHOT.md`. This skill never issues permits, creates agents, chooses commit mode, resumes pauses, authorizes effects, or mutates canonical state.

## Domain Ledger Additions

- Objective, decision and action owners, decision rights, target users, affected non-users, common/edge/high-cost scenarios, baseline, non-goals, and failure costs.
- Supported action, owner response/capacity, acceptance criteria, adoption workflow, instrumentation, and evidence standard.
- Status quo, manual/process, no-build, build/buy/partner options; value, lifecycle cost, burden, opportunity cost, reversibility, and disqualifiers.
- User/product/business metrics, causal assumptions, counter-metrics, guardrails, unit economics, sensitivity, break-even, and confidence.
- Staged commitment, maximum exposure, rollout/fallback, kill triggers, trigger authority, and evidence that would change the recommendation.

## Domain Gates

| Gate | Pass condition | Required proof |
| --- | --- | --- |
| `PBD-G1` UseCase | The real objective, users/non-users, common/edge/high-cost scenarios, baseline, supported action, owner/capacity, non-goals, criteria, and failure costs are evidenced before implementation. | Parent `ProductFitLedger` plus `PreExecutionProof.scenario_traces` with source-linked baseline and owner-confirmed action contract. |
| `PBD-G2` Alternatives | Status quo, manual/process, no-build, build, buy, and partner options are compared where feasible. | `OptionComparison` with scenario coverage, value, lifecycle cost, owner burden, opportunity cost, reversibility, evidence refs, and disqualifiers. |
| `PBD-G3` MetricChain | Evidence links intervention/output to owner action, user outcome, product/business metrics, and counter-metrics without hiding causal assumptions. | `MetricChainRecord` with authorized estimand, confounders, measurement window, scenario, action/response, outcomes, metrics, assumptions, instrumentation/version, threshold source, uncertainty, and evidence refs. |
| `PBD-G4` EconomicsAdoption | Volume, unit value, lifecycle cost, sensitivity, break-even, owner capacity, UX/training change, adoption, and fallback support the claim. | `EconomicsAdoptionCapacityRecord` with sourced volume/value and full lifecycle costs, sensitivity/break-even cases, owner capacity, workflow/training change, staged adoption definitions and measurement path, fallback, and owner approvals. |
| `PBD-G5` Reversibility | Decision rights, staged exposure, rollback/exit, kill triggers, and trigger authority match commitment risk. | Parent `DecisionLedger` plus `ReversibilityPlan` with one-way/two-way classification, maximum exposure, rollback/exit, kill criteria, authority, and evidence refs. |
| `PBD-G6` CounterMetricHarm | Every material stakeholder failure has a sourced counter-metric/limit, owner, escalation, and stop action. | `CounterMetricGuardrailMatrix` with stakeholder, failure mode, metric, limit/source, lag/noise and measurement window, monitor owner, override/escalation, hard-stop semantics, and stop action. |
| `PBD-G7` Recommendation | The recommendation compares options against authorized criteria, contrary evidence, uncertainty, sensitivities, confidence, and change conditions. | `RecommendationEvidenceMap` plus parent `DecisionLedger` with authorized priority order, tie/defer rule, option results, supporting/contrary evidence, claim confidence, and evidence that would change it. |
| `PBD-G8` SourceClosure | Every direction-changing business claim is authoritative, current, applicable, conflict-resolved, and dispositioned. | Parent `KnowledgePacket.claims` and `UnknownResolution` records covering intent, metrics, costs, capacity, feasibility, market/regulatory facts, and claim uncertainty. |

## Safe Start And Protected Actions

Before an execution permit, safe start is limited to read-only retrieval, baseline/option inventory, draft ledgers, source classification, stakeholder-question preparation, and reversible cost-capped falsification probes with explicit caps and stops.

Keep implementation commitments, spend/procurement, sensitive-data access, customer/vendor contact, experiments, model training, production mutation, pricing/policy changes, rollout, external publication, and final build/buy/launch/invest recommendations blocked until their action-stage gates pass. A bounded prototype or evidence-gathering step may receive a `validation` permit after entry gates pass; result evidence remains due and no business-impact claim or final recommendation is unlocked.

## Review Perspectives

- Use case, product workflow, users, and affected non-users.
- Decision quality, alternatives, uncertainty, and reversibility.
- Finance, unit economics, and business impact.
- Operations/GTM, adoption, owner capacity, and instrumentation.
- Domain, policy, safety, privacy, security, marketplace, or data-science expertise when the use case requires it.

## Borrowed Lenses

- `workflow-design-search-ranking-recsys` for search, feed, exposure, marketplaces, and personalization.
- `workflow-design-tabular-ml-evaluation` when scores, forecasts, labels, thresholds, or model metrics drive action.
- `workflow-design-policy-governance` for rights, eligibility, appeals, fairness, and regulated decisions.
- `workflow-design-ops-forecasting-optimization` for capacity, scheduling, routing, staffing, and physical operations.
- `workflow-design-llm-nlp`, `workflow-design-vision-multimodal`, or `workflow-design-speech-audio` for model-specific validity.

## Simplification Rules

- `PBD-G1`, `PBD-G2`, `PBD-G6`, and `PBD-G8` apply to every primary product/business commitment.
- When this skill is borrowed, `PBD-G1` applies to the supported use-case/action claim, `PBD-G3` to any metric-to-outcome claim, `PBD-G6` to affected-stakeholder harm, and `PBD-G8` to the business facts used by the parent. Other gates apply according to the protected action and claim.
- `PBD-G3` applies whenever measured effects support success. `PBD-G4` applies when adoption, budget, ROI, or operational action is claimed. `PBD-G5` is deferred during exploration but applies before commitment. `PBD-G7` applies to a final recommendation.
- Moderate work may satisfy several gates through one compact ledger and combine compatible perspectives, but gate decisions and source evidence remain distinct.
- The parent decides whether perspectives need independent real runtimes; simplification cannot waive permits, observer/restart duties, or synthesis.

## Blocking Failure Modes

Return `fail|escalate` when a plan explains how to build but not why it fits; when no user scenario, owner action, no-build option, adoption path, metric chain, counter-metric, or recommendation evidence exists; or when a direction-changing unknown is silently assumed.

## Native V5 Domain Delta

- `work_model_delta`: scenarios, users/cohorts, options, funnel stages, cost/revenue drivers; adoption, owner capacity, sensitivities, counter-metrics.
- `human_input_deltas`: target action/segment/timing, objective priority, budget, risk tolerance, decision rights, hurdle and kill criteria.
- `action_delta`: protect spend, customer/vendor contact, experiments, pricing, launch, and final recommendation publication.
- `anomaly_delta`: owner/action contradiction, economic boundary crossing, adoption failure, capacity gap, new stakeholder harm; distinguish adoption, attribution/estimand, instrumentation, capacity, segment, owner-workflow, and economic-boundary rivals using scenario ledgers, sensitivity boundaries, workflow traces, and counter-metric slices.
- `change_impact_delta`: objective/owner/capacity, scenario/segment, estimand/instrumentation/window, economics, adoption definition, counter-metric, or decision-rule changes invalidate option comparison, metric chain, economics, adoption, guardrail, and recommendation evidence.
- `insight_constraints`: preserve objective, decision owner, estimand, economics, and guardrails; distinguish adoption, attribution, capacity, segment, and economic-boundary rivals with sensitivity tests and staged outcome confirmation.

## Native V5 Packet

Emit the complete `v5-domain-1` packet from the named domain sections with producer snapshot/fingerprint. The parent router and `../SNAPSHOT.md` own schema and authority rules. Reject unknown top-level fields; optional additions belong only in a namespaced `extensions` map.

## Behavior Tests

| Task | Expected behavior |
| --- | --- |
| Add bulk export for twelve internal account managers. | Retrieve usage/support evidence, compare manual/no-build, verify owner workflow and data harm, and permit at most a bounded prototype until action and policy facts close. |
| Build churn prediction and a retention workflow. | Route tabular ML; require valid labels, intervention capacity, causal limits, alternatives, economics, and counter-metrics. AUC alone cannot permit training or experimentation. |
| Decide whether to launch in Brazil next year. | Require current market evidence, internal economics, build/partner/no-build options, sensitivities, reversibility, and kill criteria; unknown budget, decision rights, risk tolerance, or timing blocks recommendation. |
| Launch an AI refund copilot across US and EU markets. | Make Product/Business primary for the launch/economics decision, or Policy primary when eligibility/rights dominate; use LLM/NLP primary only for a fixed-policy language-system validity claim. Borrow Security/Privacy for customer data. Require rules, audit/override/appeal, capacity, economics, counter-metrics, and rollback. |
