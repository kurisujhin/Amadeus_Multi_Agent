---
name: workflow-design-product-business-decision
description: Use with multi-agent-workflow-designer when designing workflows for product/model fit, business use cases, feature strategy, decision analysis, launch/build/buy/price/invest recommendations, market entry, GMV/conversion/retention goals, or any model/feature whose success depends on user scenario, adoption, ROI, or decision quality. Emphasize target users, scenarios, supported action, metric alignment, counter-metrics, evidence standard, and recommendation.
---

# Workflow Design: Product/Business Decision

This domain subskill supplies product, business, and decision-quality deltas to `multi-agent-workflow-designer`. It prevents implementation, experiments, or research from being mistaken for use-case success.

## Trigger

Use as the primary domain when product/model fit, adoption, economics, options, or recommendation quality is the dominant risk: build/buy/launch/price/invest/enter/pivot/stop decisions; business features or models; and GMV, conversion, retention, support, sales, marketplace health, quality, or adoption goals. Product vocabulary alone is not enough. Use as a borrowed lens whenever another domain's output matters only through a stakeholder action or owner workflow.

## Parent Contract

- The parent owns real-subagent creation, runtime DAG and budgets, ledgers, execution feedback, observer/reviewer separation, permits, protected-action dispatch, mutation ownership, insight validation, synthesis, and final acceptance.
- Review perspectives below are competencies, never real or virtual agents. The parent maps them to real runtime owners.
- Each gate record needs `gate_id`, `action_stage`, `proof_phase=entry|result`, `applicability=applicable|not_applicable|unresolved`, and `applicability_evidence_refs`. Only `applicable` gates receive `decision=pass|fail|escalate`, with evidence and blocked commitments; `not_applicable` needs positive scope evidence and a reopen trigger, while `unresolved` blocks.
- High-impact business claims need source authority, `observed_at`, effective version/window, segment/geography applicability, conflicts, confidence, and `valid_until` or refresh trigger.
- Unknown objective, segment, scenario, action, owner/capacity, economics, threshold, cohort, geography, risk tolerance, counter-metric, schedule, or scope cannot authorize a commitment or be invented. A bounded assumption may authorize only a reversible falsification probe.

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
| `PBD-G3` MetricChain | Evidence links intervention/output to owner action, user outcome, product/business metrics, and counter-metrics without hiding causal assumptions. | `MetricChainRecord` with scenario, action/response, outcomes, metrics, assumptions, instrumentation, threshold source, uncertainty, and evidence refs. |
| `PBD-G4` EconomicsAdoption | Volume, unit value, lifecycle cost, sensitivity, break-even, owner capacity, UX/training change, adoption, and fallback support the claim. | `EconomicsAdoptionCapacityRecord` with sourced inputs, sensitivity cases, capacity evidence, workflow changes, adoption/measurement path, fallback, and owner approvals. |
| `PBD-G5` Reversibility | Decision rights, staged exposure, rollback/exit, kill triggers, and trigger authority match commitment risk. | Parent `DecisionLedger` plus `ReversibilityPlan` with one-way/two-way classification, maximum exposure, rollback/exit, kill criteria, authority, and evidence refs. |
| `PBD-G6` CounterMetricHarm | Every material stakeholder failure has a sourced counter-metric/limit, owner, escalation, and stop action. | `CounterMetricGuardrailMatrix` with stakeholder, failure mode, metric, limit/source, window, monitor owner, override/escalation, and stop action. |
| `PBD-G7` Recommendation | The recommendation compares options against authorized criteria, contrary evidence, uncertainty, sensitivities, confidence, and change conditions. | `RecommendationEvidenceMap` plus parent `DecisionLedger` with priority source, option results, supporting/contrary evidence, claim confidence, and evidence that would change it. |
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

## V4 Runtime Handoff

Return marginal deltas to v4. Barriers are decision-frame closure, pre-prototype spend, pre-experiment, and pre-recommendation. Emit parent feedback for owner/action/capacity contradiction, source expiry, economic sensitivity crossing a decision boundary, counter-metric breach, adoption failure, or newly affected stakeholder. Link direct evidence, safe stop, and reopen conditions. Spontaneous alternatives are `InsightCandidate`s, not recommendations; freeze the no-build baseline, observable consequence, cheapest customer/workflow/economic falsifier, counter-metrics, confirmation, and contamination. Novelty cannot invent willingness, capacity, thresholds, owners, or authority.

## Domain Gate Packet

```text
DomainGatePacket:
  parent_contract_version: v4
  packet_domain: Product/Business Decision
  routing_role: primary|borrowed
  primary_domain: set by parent
  route_reason: dominant validity/risk or marginal domain delta
  marginal_gate_delta: [question, gate, proof, trigger, or protected action changed]
  omit_or_exception_reason: [plausible lens omitted or default-two exception]
  ledger_additions: [field=value ...]
  knowledge_sources: [source, authority, effective_window, observed_at, segment_geography, conflicts, valid_until, status]
  freshness_required: [claim -> freshness or change trigger]
  retrieval_status: complete|partial|blocked
  required_questions: [direction-changing unknown -> authorized owner]
  reviewers: [perspective -> real runtime owner assigned by parent]
  domain_gates: [gate_id, action_stage, proof_phase, applicability, applicability_evidence_refs, decision, evidence_required, evidence_refs, open_gap_ids, blocked_commitments, required_change, reopen_or_invalidation_trigger]
  shared_evidence_refs: [artifact -> consuming domain gates]
  runtime_handoff: [semantic_barriers, anomaly_triggers, max_unchecked_interval_or_NA, direct_evidence_refs, safe_stop_state, observer_authority, affected_gate_proof_permit_descendants]
  insight_constraints: [protected_invariants, cheapest_falsifier, confirmation_boundary, contamination]
  handoff_status: ready|partial|blocked
  validation_artifacts: [stable artifact refs]
  borrowed_lenses: [skill -> reason]
  stop_conditions: [concrete stop, invalidation, or escalation trigger]
  simplification_triggers: [gate -> applicability evidence and residual limits]
```

## Behavior Tests

| Task | Expected behavior |
| --- | --- |
| Add bulk export for twelve internal account managers. | Retrieve usage/support evidence, compare manual/no-build, verify owner workflow and data harm, and permit at most a bounded prototype until action and policy facts close. |
| Build churn prediction and a retention workflow. | Route tabular ML; require valid labels, intervention capacity, causal limits, alternatives, economics, and counter-metrics. AUC alone cannot permit training or experimentation. |
| Decide whether to launch in Brazil next year. | Require current market evidence, internal economics, build/partner/no-build options, sensitivities, reversibility, and kill criteria; unknown budget, decision rights, risk tolerance, or timing blocks recommendation. |
| Launch an AI refund copilot across US and EU markets. | Keep LLM/NLP primary, borrow Policy/Governance and Product/Business, and add Security/Privacy when customer data is accessed. Require jurisdictional rules, audit/override/appeal, owner capacity, economics, counter-metrics, and rollback before sensitive access, experiment, rollout, or final recommendation. |

## Runtime Enforcement

The parent must evaluate each applicable gate as `pass|fail|escalate` against named evidence refs; prose that merely mentions a concern is not proof. Every `fail|escalate` record must list the protected action it blocks, the owner of the missing evidence, and the reopen trigger. `N/A` requires positive applicability evidence and a residual-limit statement. Do not authorize a build, launch, pricing, investment, or model commitment without a `DecisionRuleRecord` stating criteria priority/weights, hurdle, risk tolerance, tie/defer rule, and authorizer. `MetricChainRecord` must state the estimand, comparison/attribution design, confounders, observation window, and invalidation conditions; pre/post correlation cannot support a causal success claim. `EconomicModelRecord` must include fixed and variable cost, cash timing, downside, cannibalization, cost of delay, and scarce-capacity opportunity cost. Adoption evidence must distinguish awareness, activation, repeated use, workflow completion, and retained use. Counter-metric limits must identify measurement lag, slice coverage, noise basis, alert versus hard-stop semantics, and an authority that can actually stop exposure.

## Self-Improvement Hook

After a task, emit a `DomainSkillUpdateCandidate` only when evidence shows a recurring missing trigger, gate, perspective, metric trap, or failure mode. Include task evidence and one failing-then-passing behavior test. Do not mutate the installed skill unless the user requested or approved improvement.
