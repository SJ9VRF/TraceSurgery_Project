# TraceSurgery Dataset Card

## Purpose
Study causal failure, propagation and recovery in long-horizon interactive agents.

## Unit of data
A task specification and one or more trial trajectories containing observations, actions, privileged state snapshots for grading, failure annotations, causal edges, recoverability labels, safety events and outcome metrics.

## Intended uses
Agent evaluation, reliability research, recovery-policy research, post-training curriculum construction and failure-analysis tooling.

## Out of scope
Ranking human users; evaluating unconsented production accounts; destructive actions on real data; claims of general intelligence or deployment safety from benchmark performance alone.

## Annotation
Gold trajectories are double-annotated and adjudicated. Scaled annotations may use automatic candidate extraction and model-assisted labeling, but benchmark releases should disclose the pipeline and human calibration quality.

## Privacy
Paper tasks should use synthetic or licensed fixtures. Avoid personal email, credentials, private files or production account traces.

## Known limitations
Benchmark environments approximate parts of real interactive software. A taxonomy can omit rare failures. Grader bugs can invalidate conclusions. Model behavior changes with prompting and versioning. Success on a benchmark does not establish deployment safety.
