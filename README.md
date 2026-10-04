# TraceSurgery

**Counterfactual Interventions for Failure Causality and Recoverability in Computer-Use Agents**

**Aura Yavary**

TraceSurgery is a research framework for asking a stricter question than ordinary agent debugging:

> If we surgically changed one action, one state, or the remaining policy at a specific point in a failed computer-use trajectory, would the task outcome actually change?

Most agent benchmarks score final success. Failure-analysis systems localize likely bad steps from traces. Recovery systems attempt to repair a run. TraceSurgery instead treats a failed trajectory as an object for **executed counterfactual experiments**. It checkpoints the environment, branches the trajectory, applies minimal interventions, replays the continuation, and re-grades the resulting world state with the same outcome oracle.

The intended scientific output is not another error taxonomy. It is a **causal recovery surface** over intervention time and intervention type.

## 60-second technical review

If you are evaluating the artifact rather than reading the paper end to end:

1. Read `docs/HIRING_MANAGER_BRIEF.md` for the research claim and evidence boundary.
2. Inspect `tracesurgery/counterfactual.py` for the checkpoint/branch/replay machinery.
3. Run `python scripts/verify_release.py` for tests, >=90% coverage, release audit, 500-task oracle validation, and wheel build.
4. Read `docs/REVIEWER_RED_TEAM.md` and `docs/VALIDITY_THREATS.md` for failure modes the project explicitly does not hide.
5. Read `docs/SCHEMA_COMPATIBILITY.md` if integrating external runs.

TraceSurgery 1.0 is a **stable research artifact**, not a claim that the frontier-model experiment is complete. See `docs/V1_RELEASE_NOTES.md`.


## Five-minute demo

For the fastest end-to-end check, run:

```bash
python scripts/demo_5min.py --output runs/demo_5min.json
```

The demo verifies replay controls and an outcome-changing intervention on the bundled deterministic task. It is software-validation evidence only. See [`docs/5_MINUTE_DEMO.md`](docs/5_MINUTE_DEMO.md).

## Reproduce before you believe

```bash
python -m pip install -e ".[dev]"
tracesurgery --version
tracesurgery doctor
python scripts/verify_release.py
```

Normal experiment runs emit a `manifest.json` with suite hash and runtime provenance. See `docs/RESEARCHER_QUICKSTART.md` and `docs/PUBLIC_CLAIMS.md`. The public-claims policy explicitly separates implemented local evidence from external frontier-model hypotheses.

## Why this project changed direction

The original project name and framing, RecoveryBench, were retired after a September 2026 related-work audit. That name already collides with existing recovery benchmarks, and several originally planned contributions - failure taxonomies, root-cause localization, controlled fault injection, and repair - now have strong direct precedents.

TraceSurgery therefore narrows the claim to a harder and more falsifiable gap: **intervention-validated causal mechanics of failure in stateful computer-use agents**.

See [`docs/NOVELTY_AUDIT_2026-09.md`](docs/NOVELTY_AUDIT_2026-09.md) for the explicit overlap analysis and claim boundaries.

## Core object: the causal recovery surface

For a failed trajectory `tau` and intervention family `I`, TraceSurgery estimates:

```text
R(t, I) = task success after intervening at step t with intervention I
```

The reference implementation supports three evaluator-side surgeries plus replay-fidelity gating:

- `no_intervention`: replay the same checkpoint and suffix to verify that the branch substrate is causally usable.
- `action_patch`: replace exactly one recorded action with a validated reference action.
- `state_patch`: restore the evaluator's reference pre-state at one checkpoint while preserving the failed continuation.
- `suffix_replan`: preserve the failed state at the intervention point but replace the remaining continuation with a validated reference suffix.

These interventions answer different questions:

```text
action patch succeeds      -> this decision was causally critical
state patch succeeds       -> accumulated world-state corruption was sufficient to explain failure
suffix replan succeeds     -> the current state remained salvageable with a better policy
none succeed               -> failure is outside the tested repair family or already irreversible
```

From the executed branch matrix we can compute auditable quantities such as:

- **Intervention Outcome Gain** - change in task success caused by one surgery.
- **Replay Fidelity** - whether an unmodified branch reproduces the source final state at that checkpoint.
- **Diagnosis Faithfulness** - whether a debugger's preregistered repair claim has executed outcome effect.
- **Bounded Repair-Set Upper Bound** - minimum-cardinality oracle action-patch sets within a declared search domain; not claimed as novel.
- **Last Recoverable Checkpoint** - latest tested step from which a specified surgery still succeeds.
- **Recovery AUC** - area under the discrete recovery curve across tested checkpoints.
- **Intervention-Type Decomposition** - whether repair requires changing action, environment state, or future policy.
- **Irreversibility Frontier** - where previously successful repair families cease to recover the task.

## External-study result pipeline

The v1.0 research pipeline is fail-closed: multi-worker study cells are atomically claimed, completed runs are converted to provenance-bearing evidence records, manifest hashes can be recomputed from disk, and paper-ready summaries are generated only after the scientific-evidence audit passes. See `docs/SCIENTIFIC_RESULT_PIPELINE.md`.

## Evidence boundary

This repository deliberately separates three levels of evidence.

### 1. Implemented research machinery

The following are real and executable now:

- provider-neutral agent and environment contracts;
- exact pre-/post-action observations;
- privileged evaluator checkpoints separated from agent-visible state;
- deterministic state and safety grading;
- counterfactual checkpoint/restore/replay engine;
- per-checkpoint no-intervention replay controls and causal-admissibility gates;
- stable checkpoint/continuation/final-state provenance hashes;
- action, state, and suffix interventions;
- executable diagnosis-faithfulness evaluation;
- bounded oracle repair-set search for causal upper bounds;
- recovery-surface computation;
- hierarchical failure-event schema;
- explicit exogenous intervention events;
- seeded perturbation library;
- task-clustered statistics;
- annotation tools, paper protocol, dataset/release metadata, website, CI, and tests.

### 2. Local software-validation evidence

The repository includes 500 procedurally generated deterministic tasks across browser-like, document, spreadsheet, email-like, filesystem, and multi-app workflows. They validate reset/setup/grading/contracts and are **not** a frontier-agent benchmark result.

### 3. Scientific claims not yet earned

The repository does **not** claim frontier-model SOTA. That requires real model runs in realistic browser/desktop environments, repeated trials, matched baselines, human calibration, and preregistered statistical analysis. No model improvement number is fabricated in this release.


## Evidence layer

The polished overview is intentionally not the whole story. The inspectable research-process layer is in [`docs/evidence/EVIDENCE_LAYER.md`](docs/evidence/EVIDENCE_LAYER.md). It includes executed experiment logs, negative intervention results, decision records, real local eval tables, unexpected findings, raw branch artifacts, and the explicit Git-history boundary.

Start here:

- [`Experiment Journal`](artifacts/experiment_logs/EXPERIMENT_JOURNAL.md)
- [`What did not work`](docs/evidence/FAILED_EXPERIMENTS.md)
- [`Decision Log`](docs/evidence/DECISION_LOG.md)
- [`Real eval tables`](docs/evidence/EVAL_TABLES.md)
- [`Unexpected findings`](docs/evidence/UNEXPECTED_FINDINGS.md)
- [`Raw artifacts`](artifacts/README.md)

No external frontier-model result is fabricated to make this layer look fuller than it is.

## Quick start

```bash
python -m pip install -e .
pytest

# Validate the local 500-task software suite.
tracesurgery validate-suite \
  --suite tasks/suites/validation_500.yaml \
  --oracle-run

# Execute a known failed trajectory and sweep counterfactual repairs.
tracesurgery surgery \
  --task tasks/samples/spreadsheet_formula.yaml \
  --output runs/surgery_demo.json
```

The expected local demo contains one deliberately corrupted spreadsheet action. The unmodified replay first verifies checkpoint fidelity. A one-action surgery at the corrupted step flips the task outcome, while irrelevant action patches do not. A later state patch also restores success. This is a software semantics test, not a scientific model result.

## Paper-scale experiment

The publishable benchmark should use real computer-use tasks with deterministic or checkpointable state and at least the following arms:

```text
Natural execution
    |
    +-- failed trajectory tau
           |
           +-- no intervention control
           +-- action patch at t
           +-- observation refresh at t
           +-- state patch at t
           +-- memory/belief patch at t
           +-- local replan at t
           +-- rollback + replan at t
           +-- oracle suffix upper bound
```

The scientific unit is a **task-level paired branch family**, not an individual branch. Confidence intervals and model comparisons must therefore cluster/resample by task. A branch is excluded from causal summaries if its no-intervention replay does not reproduce the source under the preregistered state-equivalence policy.

## Required baselines

A paper release must compare against strong adjacent approaches rather than weak handcrafted baselines:

- trace-only root-cause localization;
- CUADebug-style diagnosis + re-execution;
- retry/reflection/replan recovery;
- verifier-guided recovery;
- fault-injection robustness evaluation;
- oracle critical-step and oracle checkpoint upper bounds.

The goal is not to claim better debugging accuracy. The goal is to test whether **trace diagnosis agrees with replay-controlled intervention effect**, and whether models differ in the *shape* of their recoverability frontier even when final success rates look similar. Recent 2026 work already covers GUI recovery benchmarks, recovery-data synthesis, generic counterfactual repair, and minimal repair-family recovery; TraceSurgery explicitly does not claim those primitives as individually new.

## Repository map

```text
tracesurgery/
├── tracesurgery/
│   ├── counterfactual.py      # checkpointed branch-and-replay engine
│   ├── agents/
│   ├── core/
│   ├── environments/
│   ├── failures/
│   ├── graders/
│   ├── metrics/
│   ├── perturbations/
│   └── runners/
├── tasks/
│   ├── samples/
│   ├── suites/
│   └── validation_500/       # software validation only
├── docs/                    # novelty, validity, preregistration, reproducibility
├── paper/
├── annotation_tool/
├── website/
├── tests/
└── runs/
```

## What would make this a strong research result

The highest-signal paper is not "we made another benchmark." It is a result such as:

- trace-only debuggers frequently identify plausible steps that are **not causally sufficient** when patched;
- some models fail at similar rates but have substantially different recovery surfaces;
- state restoration helps where action repair does not, isolating state corruption from policy error;
- recoverability decays sharply after a measurable frontier on long-horizon multi-app tasks;
- failure categories predict *which intervention family* is sufficient, not merely where the error occurred.

Those are hypotheses until the real experiment is run.

## Research integrity gates

Before any headline causal result is reported:

1. the checkpoint must pass no-intervention replay fidelity;
2. the intervention family must be declared semantically valid for the task;
3. the same grader must score source and branch outcomes;
4. evaluator-only state must remain hidden from the agent;
5. branches from the same source task are treated as correlated;
6. failed repairs and negative results are retained.

See `docs/REPRODUCIBILITY.md` and `docs/PREREGISTRATION.md`.

For a two-minute technical read, see `docs/HIRING_MANAGER_BRIEF.md`; for adversarial review, see `docs/REVIEWER_GUIDE.md`; for matched external comparisons, see `docs/BASELINE_CONTRACT.md`.

## Release principle

**No causal claim without an executed intervention. No SOTA claim without a matched experiment. No benchmark result without stored traces and task-level uncertainty.**

## External-study execution (v1.0)

The repository now separates framework validation from scientific execution mechanically, not only in prose.

```bash
tracesurgery study-init --config configs/external_study.example.yaml --output runs/external_pilot
tracesurgery study-status --ledger runs/external_pilot/ledger.jsonl
tracesurgery evidence-audit --records runs/external_pilot/evidence.jsonl
```

`study-init` creates a deterministic resumable run matrix across task/model/environment/seed/repetition cells. `evidence-audit` rejects local validation and synthetic-demo records from performance-claim eligibility and requires external provenance plus a frozen grader revision. See `docs/EXTERNAL_EXECUTION_HANDOFF.md`. The core package intentionally does not pretend to bundle proprietary model clients or a realistic desktop benchmark that was not executed here.
