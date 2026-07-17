---
name: workflow-design-speech-audio
description: Use with multi-agent-workflow-designer when designing workflows for ASR, TTS, voice agents, diarization, speaker analysis, audio classification, call analysis, meeting intelligence, or real-time audio systems. Emphasize acoustic conditions, accent/language coverage, consent, latency, transcription semantics, and human correction loops.
---

# Workflow Design: Speech/Audio

This domain subskill supplies speech/audio deltas to `multi-agent-workflow-designer`. It does not replace the parent workflow.

## Trigger

Use as the primary domain for ASR, TTS, voice agents, diarization, speaker verification/identification, call analysis, meeting intelligence, audio classification, emotion/distress inference, voice conversion, or streaming audio. Use as a borrowed lens when acoustic conditions, latency/turn-taking, accent coverage, voice identity, or recording consent dominates risk.

## Native V5 Parent Boundary

Emit marginal domain semantics only; the v5 parent owns workflow and effects as defined in `../SNAPSHOT.md`. This skill never issues permits, creates agents, chooses commit mode, resumes pauses, authorizes effects, or mutates canonical state.

## Domain Ledger Additions

- Supported action, users/affected parties, semantic failure costs, and owner workflow.
- Languages, dialects, accents, code-switching, styles, channels, devices, codecs, SNR/noise, echo, overlap, distance, and prevalence/criticality.
- Batch/streaming stack, endpointing, partial results, barge-in, network/load, latency, reconnect, fallback, handoff, and correction.
- Speaker attribution/identity purpose, enrollment, authentication threshold, synthetic/replay risk, and unknown-speaker behavior.
- Speakers/bystanders, notice or authority, biometric/PII classification, purpose, vendor transfer, secondary use, retention, deletion, and audit.
- TTS/voice provenance, rightsholder authorization, disclosure, permitted uses, revocation, misuse, and incident response.

## Domain Gates

| Gate | Pass condition | Required proof |
| --- | --- | --- |
| `SA-G1` AcousticCoverage | Representative independent evaluation covers decision-relevant languages, accents, styles, channels, devices, noise, echo, overlap, and rare/high-cost conditions. | `AudioCoverageSpec` plus `SliceEvaluationReport` with provenance/split, prevalence, counts, metrics/uncertainty, source-backed criteria, uncovered slices, and sampled failures. |
| `SA-G2` SemanticHarm | End-to-end evaluation measures critical entities, numbers, negation, commands, and downstream actions by severity and slice; WER/CER alone is insufficient. | `SemanticImpactMap` plus `EndToEndTaskEvaluation` with gold provenance, cascade tests, severity-weighted outcomes, confidence/abstention, criteria, and error propagation. |
| `SA-G3` SpeakerIntegrity | Diarization, speaker attribution, verification, or identification is valid for speaker counts, boundaries, overlap, attribution, unknown speakers, and adversarial audio. | `SpeakerIntegrityReport` with DER/JER components; for verification/identification add FAR/FRR calibration by slice and replay, spoof, injection, and synthetic-voice tests. Output-only synthesized identity and voice cloning are governed by `SA-G6`, not `SA-G3`. |
| `SA-G4` StreamingInteraction | Live systems satisfy endpointing, tail latency, partial stability, interruption, network degradation, repair, fallback, handoff, and task completion requirements. | `StreamingInteractionReport` with pinned stack/load/network, p50/p95/p99 latency, revisions, barge-in, echo/overlap, jitter/loss/reconnect, timeout, fallback, handoff, and outcome results. |
| `SA-G5` ConsentData | Recording and audio use are purpose- and jurisdiction-authorized for speakers and bystanders, with complete sensitive-data lifecycle controls. | `AudioDataGovernanceRecord` with flow map, notice/consent or authority, PII/biometric class, redaction, access, transfer, secondary use, retention/deletion, audit, and approvals. |
| `SA-G6` VoiceIdentityMisuse | TTS/voice conversion has verified provenance and authorization, disclosure, least privilege, misuse tests, revocation, takedown, and incident response. | `VoiceIdentityAuthorizationAndAbuseReport` with rightsholder scope, identity validation, permitted/prohibited uses, provenance/disclosure verification, controls, tests, revocation, and residual-risk owner. |
| `SA-G7` CorrectionHumanImpact | Confidence, correction, review, appeal/override, construct validity, operator capacity, audit, and rollback work end to end. | `CorrectionAndHumanImpactRunbook` plus `WorkflowSimulationReport` with editable units, correction propagation, capacity, emotion/scoring validity, group slices, traced cases, escalation, and rollback. |

## Safe Start And Protected Actions

Before an execution permit, safe start is limited to read-only source, manifest, config, metadata, and data-flow inventory; conditional test/threat design; and cost-capped offline probes on synthetic, licensed, or already-authorized sandbox audio. This includes bounded synthetic vendor-sandbox simulation with no customer-facing interaction or external call. Raw human audio is safe only when existing access and purpose authorization explicitly cover the probe.

Keep new recording/enrollment, private-audio export, third-party transfer/annotation, speaker identification, training/fine-tuning, voice cloning, production thresholds, external demos/calls, scoring/discipline/triage, experiments, retention changes, deployment, rollout, and final recommendations blocked until their action-stage gates pass. A bounded authorized offline evaluation/training step may receive a `validation` permit after entry gates pass; result reports remain due and external interaction, claims, and rollout stay blocked.

## Review Perspectives

- Acoustic, language/accent, and slice robustness.
- Semantic downstream validity and correction workflow.
- Streaming interaction and reliability.
- Speaker integrity, identity, provenance, and abuse.
- Consent, privacy, policy, safety, clinical/workforce, legal, or domain expertise as applicable.

## Borrowed Lenses

- `workflow-design-llm-nlp` when transcripts feed summarization, extraction, chat, or policy reasoning.
- `workflow-design-policy-governance` when audio affects rights, discipline, eligibility, safety, or appeals.
- `workflow-design-ops-forecasting-optimization` when audio triggers dispatch, triage, staffing, or physical action.
- `workflow-design-software-reliability` and `workflow-design-security-privacy` for streaming, observability, voice identity, data access, and recovery.
- `workflow-design-product-business-decision` for vendor selection, adoption, contact-center economics, and owner capacity.

## Simplification Rules

- Low-risk batch evaluation may combine proof artifacts and compatible perspectives, but every gate retains an applicability record and its evidence standard.
- `SA-G3` is `not_applicable` only with no diarization, attribution, verification, or identification. `SA-G4` is `not_applicable` only with no live or time-bounded behavior. `SA-G5` is `not_applicable` only with no human-derived or identifiable audio. `SA-G6` is `not_applicable` only with no synthesis or voice conversion.
- `SA-G7` is `not_applicable` only for strictly offline evaluation with no correction loop, people scoring, downstream decision, operator workflow, deployment, or product-quality claim.
- No simplification is allowed for identity/biometrics, real-person TTS, newly recorded audio, distress/emotion inference, people scoring, regulated action, live external interaction, or rollout.
- The parent alone decides whether perspectives share a runtime and whether a direct path is valid.

## Blocking Failure Modes

Return `fail|escalate` for the affected gate when acoustic slices, semantics, identity rights, consent, latency/fallback, downstream correction, or human impact are unresolved. The subskill reports findings; only the parent withholds or invalidates an execution permit.

## Native V5 Domain Delta

- `work_model_delta`: audio seconds/utterances/speakers/turns×locale/channel; decode/stream segments; semantic entities, DER/FAR/FRR, tail latency, revisions, consent coverage.
- `human_input_deltas`: locales, voice rights, recording purpose, harm thresholds, identity use, and human-handoff capacity.
- `action_delta`: protect recording/enrollment, identity inference, external calls, cloning, thresholds, and live voice rollout.
- `anomaly_delta`: unexpected bystander, uncovered locale/channel, critical entity/negation error, speaker swap, replay/synthetic signal, consent mismatch; distinguish acoustic, segmentation, diarization, semantic-cascade, channel, and synthetic rivals using aligned clips and speaker/semantic review.
- `change_impact_delta`: task/threshold/corpus/locale/channel/codec/voice/consent changes invalidate acoustic, semantic, speaker, streaming, governance, and human-impact evidence.
- `insight_constraints`: preserve consent, identity/voice rights, semantic harm limits, and handoff; use end-to-end semantic/identity falsification and untouched locale/channel confirmation across duration, concurrency, real-time factor, and tail slices.

## Native V5 Packet

Emit the complete `v5-domain-1` packet from the named domain sections with producer snapshot/fingerprint. The parent router and `../SNAPSHOT.md` own schema and authority rules. Reject unknown top-level fields; optional additions belong only in a namespaced `extensions` map.

## Behavior Tests

| Task | Expected behavior |
| --- | --- |
| Regression-test batch ASR on an approved internal corpus. | Apply acoustic, semantic, and consent gates; record proof-backed exclusions. Missing deployment channels or semantic criteria blocks a quality claim, not a bounded offline report. |
| Add diarization and action extraction to stored multilingual meetings. | Require overlap/speaker evidence, consent and speaker-naming rules, semantic error propagation, correction ownership, and human-impact review before launch. |
| Select a multilingual streaming voice agent to reduce contact-center cost. | Route product/business and LLM lenses; undefined intents, economics, counter-metrics, consent, locales, latency SLO, or handoff capacity blocks recommendation and customer experiments. Synthetic simulation remains safe. |
| Clone an executive's voice for global financial outreach. | Require signed scope, jurisdictions, disclosure, vendor use/retention, revocation, misuse and incident controls. Until closure, permit only a generic licensed-voice mock and threat model. |
