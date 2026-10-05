# Paper-Scale Evaluation Protocol

## Freeze before evaluation
Freeze task definitions, held-out split, grader versions, prompt/agent configurations, ontology version, primary metrics, exclusion rules and bootstrap procedure before final model runs.

## Trial protocol
Run at least five trials per task/configuration. Preserve task as the statistical unit. Record exact model revision, provider parameters, prompt hash, environment image/version, seed, wall-clock time, token accounting and grader version.

## Primary endpoints
1. Task Success Rate
2. Recovery Rate conditional on recoverable failure
3. Catastrophic Action Rate
4. Failure Detection Latency
5. Error Propagation Depth

## Secondary endpoints
Cost/success, latency/success, first-failure position, cascade size, recovery cost, recovery-window length, state-divergence duration and point-of-no-return position.

## Human calibration
Double-annotate a preregistered gold sample. Report agreement before adjudication, adjudication protocol, and model-assisted annotation accuracy against gold.

## Reporting
Report macro and category-level results with uncertainty. Include model/configuration failures, grader disagreements, safety regressions, and perturbation-specific breakdowns. Do not cherry-pick representative trajectories.
