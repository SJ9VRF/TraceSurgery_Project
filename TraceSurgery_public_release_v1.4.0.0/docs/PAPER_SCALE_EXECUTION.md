# Paper-Scale Execution Plan

The software is ready for external model/environment execution, but a conference-quality empirical release still requires data that cannot be manufactured offline.

## Stage 1 — environment-backed pilot

- 30–50 realistic long-horizon tasks from one browser/desktop adapter.
- 3–5 trials per task.
- direct agent, retry/reflection baseline, and explicit-verification baseline.
- manual transcript review of every failure.
- revise ontology only during this stage.

**Exit criteria:** grader false-positive/false-negative issues are rare and documented; reset reliability is high; taxonomy definitions are stable enough to freeze.

## Stage 2 — benchmark build

Target a diverse suite with at least 150 tasks for the first scientific release. Expand toward 500 only if task quality and verifier reliability remain high. Prefer fewer high-quality, state-verifiable workflows over hundreds of shallow synthetic prompts.

Each task must have:

- authentic or controlled input artifacts;
- unambiguous success criteria;
- state-based verifier;
- safety constraints;
- scenario-family identifier for split control;
- expected challenge phenomena;
- at least one manually verified valid solution path;
- provenance and license information.

## Stage 3 — failure annotation

Create a gold subset spanning models, outcomes, categories, and perturbations. Two independent annotators label failure presence, failure family, root cause, recoverability, recovery window, and evidence. Adjudicate disagreements before using model-assisted annotation for the remaining corpus.

## Stage 4 — main model matrix

At minimum compare:

- direct/reactive agent;
- retry baseline;
- reflection baseline;
- memory baseline;
- explicit verification baseline;
- Phoenix/recovery method when available;
- oracle detection/recovery conditions where implementable.

Use identical environment/task versions, budgets, and seeds when comparisons are meant to be paired.

## Stage 5 — controlled interventions

Run matched natural and perturbed conditions. Perturbation families should include session/state disruption, UI interruption, stale/hidden state, missing resources, and corrupted intermediate artifacts. Do not count the intervention itself as an agent failure.

## Stage 6 — analysis/release

Produce:

- task success and partial outcomes;
- failure-family distribution;
- root-vs-terminal mismatch frequency;
- propagation depth/cascade size;
- recoverability and recovery rate;
- failure detection latency;
- recovery efficiency;
- safety events;
- cost and wall-clock latency;
- task-level confidence intervals;
- negative results and grader/environment failure counts.

Freeze a versioned dataset, code commit, environment image/version, model identifiers, configs, and checksums before paper submission.
