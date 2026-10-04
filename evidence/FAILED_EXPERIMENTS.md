# What did not work

This page records negative results and invalidated assumptions that materially changed TraceSurgery. It deliberately mixes **local causal experiments** and **research-engineering validity failures**, but labels them separately. None of the entries below is presented as a frontier-model performance result.

## F-001 - State repair too early did not survive the recorded bad action

**Type:** local causal experiment  
**Hypothesis:** restoring the correct state at checkpoint 0 may be enough to recover the task.  
**What happened:** `state_patch` at checkpoint 0 still failed. The original next action wrote `spreadsheet.summary = 41` again.  
**Why it failed:** the future policy/action, not the current state, was still corrupting.  
**Change made:** recovery is represented as a checkpoint-indexed intervention surface rather than a single global repair label.  
**Evidence:** `runs/demo_5min.json`, `artifacts/ablations/step0_state_patch.json`.

## F-002 - Patching the terminal action after corruption did not repair persistent state

**Type:** local causal experiment  
**Hypothesis:** changing the remaining action at checkpoint 1 may recover the task.  
**What happened:** the action patch changed the terminal `finish` action but the task still failed.  
**Why it failed:** the wrong value was already stored in the spreadsheet state.  
**Change made:** action-level repair and state-level repair remain separate intervention families.  
**Evidence:** `artifacts/ablations/step1_action_patch.json`.

## F-003 - Suffix replanning after corruption did not automatically undo the bad state

**Type:** local causal experiment  
**Hypothesis:** replacing the remaining suffix after checkpoint 1 may recover the task.  
**What happened:** suffix replanning failed at checkpoint 1.  
**Why it failed:** the alternative suffix did not include a state-repairing operation; changing continuation alone was insufficient once the environment state was wrong.  
**Change made:** recovery analyses distinguish policy repair from explicit world-state repair.  
**Evidence:** `artifacts/ablations/step1_suffix_replan.json`.

## F-004 - "RecoveryBench" was not a defensible identity for the project

**Type:** novelty / framing failure  
**Initial assumption:** a recovery-centric benchmark framing and the name RecoveryBench were sufficiently distinct.  
**What changed:** the novelty audit found substantial adjacency and naming collision risk with existing recovery/debugging work.  
**Change made:** the project was renamed **TraceSurgery** and narrowed to replay-controlled, checkpoint-indexed causal interventions and intervention-faithfulness.  
**Evidence:** `docs/NOVELTY_AUDIT_2026-09.md`, `CHANGELOG.md` (v0.4.0).

## F-005 - Counterfactual recovery without replay fidelity was too weak for causal language

**Type:** validity-design failure  
**Initial assumption:** an intervention branch that succeeds can be compared directly with the observed failure.  
**Problem:** in a nondeterministic environment, branch success could come from replay drift rather than the intervention.  
**Change made:** v0.5.0 made same-checkpoint no-intervention replay a mandatory admissibility control, with checkpoint/continuation/final-state hashes.  
**Evidence:** `CHANGELOG.md` (v0.5.0), `docs/COUNTERFACTUAL_PROTOCOL.md`.

## F-006 - Merely storing a manifest hash field was insufficient provenance

**Type:** research-engineering failure  
**Problem:** a populated `manifest_sha256` field is not evidence that the referenced bytes were actually checked.  
**Change made:** evidence audit now resolves the manifest on disk and recomputes SHA-256 before claim eligibility.  
**Evidence:** `CHANGELOG.md` (v0.9.0), `tracesurgery/evidence.py`.

## F-007 - Generated build trees inside the source archive created ambiguity

**Type:** release-engineering failure  
**Problem:** an earlier public-release pass still carried generated `build/` source duplicates.  
**Why it mattered:** a reviewer should not have to guess which copy is canonical.  
**Change made:** v1.0.1 removes generated build/dist/egg-info artifacts and audits for their reappearance.  
**Evidence:** `CHANGELOG.md` (v1.0.1), `tracesurgery/release_audit.py`.

## What is intentionally *not* on this page

There are no fabricated statements such as "more synthetic data hurt performance" or "curriculum caused a 3-point regression" because those model-training experiments have not been executed for TraceSurgery. When the external study is run, negative model results should be appended here with immutable run IDs and raw evidence paths.
