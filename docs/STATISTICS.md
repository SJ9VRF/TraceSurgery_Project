# Statistical Analysis Protocol

TraceSurgery treats each task-trial pair as an observation while respecting repeated trials on the same task.

## Primary reporting

For task success and other rates, report mean plus 95% confidence interval. The reference implementation provides fixed-seed nonparametric bootstrap intervals for simple aggregation. Paper analysis should additionally bootstrap at the **task level** when multiple trials per task are present, so repeated stochastic trials do not artificially narrow uncertainty.

## Paired model comparisons

When two agents are run on the same task/seed pairs:

- report paired success differences with task-level bootstrap confidence intervals;
- use McNemar's test for paired binary success as a secondary significance test;
- report effect sizes, not p-values alone;
- correct for multiple comparisons when testing many model pairs or many taxonomy categories.

## Recovery analyses

For recoverable failures, report:

- recovery probability by failure family;
- recovery probability vs. detection delay;
- recovery steps/cost conditional on recovery;
- survival-style curves for remaining recoverability over steps since failure where annotations support a recovery window;
- stratification by horizon/statefulness so easy task families do not dominate aggregates.

## Annotation reliability

Report agreement separately for:

- failure present/absent;
- top-level failure family;
- root-cause flag;
- recoverability level.

Use Cohen's kappa for two annotators or Fleiss' kappa for more than two, with raw agreement alongside kappa. Recovery-window endpoints should use absolute-difference or tolerance-based agreement rather than forcing a categorical statistic.

## Missing/ambiguous trials

Do not silently drop environment crashes, grader ambiguity, or invalid resets. Give them explicit statuses and report their counts. Separate benchmark-infrastructure failures from agent failures.
