# Novelty audit - September 25, 2026

Author: **Aura Yavary**

## Decision

The original **RecoveryBench** framing is retired. It is neither a unique name nor a sufficiently differentiated late-2026 research contribution.

The redesigned project is:

**TraceSurgery: Counterfactual Interventions for Failure Causality and Recoverability in Computer-Use Agents**

A fresh exact-name web search on September 25, 2026 found no directly colliding AI-agent benchmark named `TraceSurgery`. This is a working research name, not a trademark clearance.

## Closest work and what it already owns

| Work | What it already covers | Consequence for TraceSurgery |
|---|---|---|
| Letta Recovery-Bench | recovery from prior mistakes/corrupted trajectories | do not use RecoveryBench name; recovery alone is not novel |
| AgentErrorBench / AgentDebug | failure taxonomy, annotated traces, debugging feedback | taxonomy + diagnosis cannot be the main claim |
| AgentRx | critical-step localization | critical-step localization alone is incremental |
| CUADebug (2026) | CUA-specific error taxonomy, human-annotated OSWorld failures, root-cause localization, corrective strategy, re-execution | direct overlap with the original diagnosis/repair plan |
| GUI-RobustEval / RoTS (2026) | 1,216 executable GUI recovery cases plus large-scale recovery-oriented trajectory synthesis | GUI recovery evaluation and recovery-data synthesis are already active, strong baselines |
| VeriGUI / action-effect verification | controlled GUI failures and action-effect/recovery verification | fault injection + recovery score is not sufficient novelty |
| CausalFlow (2026) | step-level counterfactual intervention, causal responsibility, minimal repair, learning-ready supervision | generic intervention-based causal repair is already occupied |
| MRFR / GCJR (Aug 2026) | inclusion-minimal repair-family recovery with counterfactual replay | minimum repair-set discovery itself cannot be claimed as new |
| OSWorld 2.0 | realistic long-horizon CUA workflows, hidden state, safety-sensitive execution | task realism and long horizon are substrates, not the contribution |
| GUI-CC (Aug 2026) | contextual consistency of GUI world-model environments | simulation fidelity must be audited when world-model environments are used |

## Defensible gap

TraceSurgery should make a narrow, falsifiable claim around the **joint experimental design**, not around any primitive in isolation:

1. **Computer-use-specific intervention decomposition** that contrasts action repair, observable-state refresh, evaluator world-state restoration, internal belief/memory correction when exposed, and future-policy replacement.
2. **Checkpoint-indexed recovery surfaces** over the trajectory rather than one critical step or one recovery score.
3. **Replay-fidelity-gated causal evidence**: an intervention at checkpoint `t` is not used for causal estimation unless a no-intervention replay from that same checkpoint reproduces the source outcome/state under a preregistered equivalence policy.
4. **Executed diagnosis faithfulness**: a debugger's root-cause claim is evaluated by whether its declared repair has measured outcome effect, not by label agreement alone.
5. **Irreversibility / last-recoverable-checkpoint analysis** on stateful multi-application workflows.
6. **Cross-model failure geometry**: models with similar final success may differ in which intervention family rescues them and how quickly recoverability decays.
7. **Paired task-level inference** that treats counterfactual branches as correlated experimental descendants of one source trajectory.

This is narrower than the original benchmark pitch and therefore more credible.

## Falsifiable research questions

- RQ1: How often do trace-only root-cause labels point to a checkpoint where the preregistered repair actually changes the final outcome?
- RQ2: Among recoverable CUA failures, what fraction require action repair, world-state restoration, belief/memory correction, or policy replacement?
- RQ3: How does recoverability change as intervention is delayed?
- RQ4: Conditional on similar baseline task success, do models have different recovery-surface shapes?
- RQ5: Which failure mechanisms cross an irreversibility frontier fastest?
- RQ6: Does belief/world-state divergence predict the intervention family required for recovery?
- RQ7: How often do apparent intervention effects disappear when checkpoints with poor replay fidelity are excluded?

## Reviewer-proof claim language

Safe before frontier experiments:

> We present an executable framework for replay-controlled, intervention-based analysis of computer-use failures and define checkpoint-indexed recovery surfaces that separate action, state, and continuation effects.

Requires real experiments and another final literature sweep:

> TraceSurgery is the first ...

Do not use that sentence in the current release.

Unsafe today:

- `state of the art`;
- `best benchmark`;
- `first causal benchmark` without a carefully verified qualifier;
- model rankings;
- percentage improvements not backed by stored real-model runs.

## Naming audit

Rejected: `RecoveryBench`, `RIFT`, `FaultLine`, `Breakpoint` because of existing collisions or heavy prior use.

Selected working name: **TraceSurgery**.
