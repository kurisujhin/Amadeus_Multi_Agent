---
name: workflow-design-search-ranking-recsys
description: Use with multi-agent-workflow-designer when designing workflows for search, retrieval, ranking, recommendation, feeds, ads ranking, personalization, marketplace exposure, reranking, candidate generation, or relevance evaluation. Emphasize user intent, offline-online metric alignment, bias, diversity, ecosystem effects, serving constraints, and experiments.
---

# Workflow Design: Search/Ranking/Recsys

This domain subskill supplies retrieval, ranking, recommendation, and exposure-allocation deltas to `multi-agent-workflow-designer`. It does not replace the parent workflow.

## Trigger

Use as the primary domain when ordering, retrieval, or exposure validity dominates the supported action in search relevance, candidate generation, ranking, feeds, recommendation, ads, personalization, reranking, or marketplace matching. Keep Product/Business primary for a GMV-led build or business decision, and keep Policy/Governance primary when the action is eligibility or denial rather than ordering. Record the primary-route rationale and justify any exception beyond two borrowed lenses.

## Parent Contract

- The parent owns real-subagent creation, runtime topology, ledgers, observer/restart behavior, permits, mutation ownership, synthesis, and final acceptance.
- Review perspectives below are competencies, never real or virtual agents. The parent maps required perspectives to real runtime owners and records their IDs.
- Each gate record needs `gate_id`, `action_stage`, `proof_phase=entry|result`, `applicability=applicable|not_applicable|unresolved`, and `applicability_evidence_refs`. Only `applicable` gates receive `decision=pass|fail|escalate`, with evidence and blocked commitments; `not_applicable` needs positive scope evidence and a reopen trigger, while `unresolved` blocks.
- Source-dependent claims require authority, logging/judgment policy, `observed_at`, effective version/date when available, population and stage applicability, and retrieval status. Missing or stale high-impact facts remain unknown.
- Unknowns that could change intent scope, candidate eligibility, labels, objective, exploration, serving, threshold, owner, experiment, schedule, or rollout cannot authorize execution or be invented.

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

## V4 Runtime Handoff

Return marginal deltas to v4. Barriers are stage/label closure, locked offline evaluation, pre-allocation review, each ramp, and fallback validation. Emit parent feedback for stage-attribution mismatch, label/log-policy drift, exposure/diversity/fairness guardrail excursion, interference, serving/freshness degradation, or rollback failure. Include direct evidence, safe fallback, and affected gates/permits. Observer continuation and independent causal/result review remain separate. An unexpected reranker, objective, feature, or exploration idea is only an `InsightCandidate`; test the cheapest stage-correct falsifier against bias/ecosystem rivals and untouched confirmation. Offline lift cannot authorize exposure or revise counter-metrics post hoc.

## Domain Gate Packet

```text
DomainGatePacket:
  parent_contract_version: v4
  packet_domain: Search/Ranking/Recsys
  routing_role: primary|borrowed
  primary_domain: set by parent
  route_reason: dominant validity/risk or marginal domain delta
  marginal_gate_delta: [question, gate, proof, trigger, or protected action changed]
  omit_or_exception_reason: [plausible lens omitted or default-two exception]
  ledger_additions: [field=value ...]
  knowledge_sources: [source, authority, policy_or_log_version, observed_at, applicability, status]
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
| Compare two rerankers on a frozen judged query set. | Use the offline simplification only after bounding the claim to that set; retain scope, label, metric, uncertainty, and stage-attribution evidence. |
| Improve cold-start recommendations on a homepage. | Require exposure/feedback analysis, new-user and sparse-item slices, diversity, fallback, serving, and online experiment readiness. |
| Increase marketplace GMV with personalized ranking. | Keep Product/Business primary and Search borrowed; reject GMV-only optimization until buyer, seller, concentration, trust, margin, retention, and experiment counter-metrics are owned. |
| Rank global gig workers for high-value opportunities. | Keep Search primary only while the action is ordering/exposure; reroute Policy primary for eligibility/denial. Record the route rationale and any exception beyond two lenses, then block rollout until fairness, feedback bias, explanation/appeal, fraud, jurisdiction, serving, and rollback evidence pass. |

## Runtime Enforcement

The parent must evaluate each applicable gate as `pass|fail|escalate` against named evidence refs; prose that merely mentions a concern is not proof. Every `fail|escalate` record must list the protected action it blocks, the owner of the missing evidence, and the reopen trigger. `N/A` requires positive applicability evidence and a residual-limit statement. Do not infer user or marketplace value from offline ranking metrics without stage attribution, exposure effects, and guardrails.

## Self-Improvement Hook

After a task, emit a `DomainSkillUpdateCandidate` only when evidence shows a recurring missing trigger, gate, reviewer perspective, or failure mode. Include task evidence and one failing-then-passing behavior test. Do not mutate the installed skill unless the user requested or approved improvement.
