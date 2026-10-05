# Why TraceSurgery is a high-signal research-engineering artifact

Author: **Aura Yavary**

This document is intentionally not resume copy. It is a reviewer-facing map from concrete repository evidence to the capabilities a strong agent/evals research engineer is expected to demonstrate.

## Signals the repository can legitimately show today

| Capability | Concrete evidence in this repository |
|---|---|
| Research taste | The original RecoveryBench concept was retired after a related-work audit found direct overlap. The project was narrowed to an experimentally falsifiable question. |
| Experimental rigor | Every causal branch is paired with a no-intervention replay control; branches from checkpoints that fail replay fidelity are excluded from causal summaries. |
| Evaluation design | State-based grading, safety checks, held-out task guidance, task linting, explicit evidence boundaries, and task-level clustered uncertainty. |
| Agent systems engineering | Provider-neutral agent/environment contracts, checkpoint/restore/replay, branch provenance hashes, deterministic fixtures, CLI, CI, tests. |
| Failure analysis | Failure/intervention separation, causal graph representation, belief-state mismatch instrumentation, diagnosis-faithfulness evaluation. |
| Scientific honesty | No frontier-model score, SOTA claim, or fabricated percentage appears in the release before real experiments exist. |
| Product/research judgment | The framework is designed to sit on top of established CUA environments rather than inventing another toy desktop benchmark. |

## Signals that are **not** earned yet

Do not present the following as completed work until the corresponding evidence exists:

- frontier-model comparative results;
- OSWorld 2.0 / BrowserGym paper-scale execution;
- matched reproduction of CUADebug, GUI-RobustEval/RoTS, or other strong baselines;
- independent human annotation agreement;
- a statistically supported claim that recovery geometry differs across frontier models;
- any claim of state-of-the-art performance.

## What makes the finished study compelling

The most useful final result is not a leaderboard. A stronger result would show that ordinary task success hides different failure mechanisms. For example, two agents may have similar completion rates while one mostly makes locally repairable decisions and another rapidly corrupts latent workflow state. That distinction matters for post-training data, verifier design, agent safety, and environment construction.

## Role alignment without keyword stuffing

The work naturally exercises the same primitives used in frontier agent research: environments, graders, long-horizon computer use, failure mining, evaluation reliability, replay, model-behavior analysis, post-training data selection, safety-sensitive actions, reproducibility, and experiment velocity. The repository should demonstrate those skills through executable evidence rather than naming employers throughout the artifact.
