# TraceSurgery flagship microsite

Author: **Aura Yavary**

This folder is a static, deployable project microsite for TraceSurgery. Open `index.html` locally or serve the directory with any static host.

## What is verified on the page
- Deterministic local counterfactual demo from `runs/demo_5min.json`.
- 48/48 release regression tests, 92.75% package statement coverage, and 500/500 local validation tasks oracle-valid as recorded in the v1.0.3 release artifacts bundled here.
- Two replay-faithful control branches and three outcome-changing interventions in the deterministic demo.

These are **engineering/local-demo facts**, not frontier-model benchmark results.

## What intentionally remains pending
Cross-model task success, recovery, latency, cost, scaling curves, human annotation agreement, and SOTA comparisons require the external study described in `docs/EXTERNAL_STUDY_PLAN.md`.

## Static assets
- `assets/tracesurgery-demo.mp4` / `.webm`: deterministic local demo video.
- `assets/demo-poster.png`: video poster.
- `assets/og-tracesurgery.png`: social preview asset.
- `assets/favicon.svg`: project icon.

No external JavaScript, CSS, fonts, trackers, or analytics are required.

## Evidence Layer

Site release 1.4.0 adds `evidence.html` plus the raw `artifacts/` tree: experiment journal, failed experiments, decision log, real local eval tables, unexpected findings, qualitative cases, ablation JSON, and a Git bundle with genuine incremental commits from the imported v1.0.1 baseline. No historical commits are reconstructed.
