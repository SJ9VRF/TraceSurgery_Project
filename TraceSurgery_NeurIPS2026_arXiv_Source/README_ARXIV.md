# TraceSurgery — NeurIPS 2026-style arXiv preprint

**Title:** TraceSurgery: Replay-Controlled Counterfactual Evaluation of Failure Causality in Computer-Use Agents  
**Author:** Aura Yavary  
**Affiliation:** University of California, Davis

## What this package is
This is the non-anonymous preprint version intended for arXiv-style public posting. It uses NeurIPS 2026 preprint semantics (`preprint`, not `final`) and a 9-page PDF including references/appendix material.

The paper deliberately distinguishes three evidence levels:
1. implemented framework and software validation;
2. an executed deterministic local case study that tests branch/replay semantics;
3. a preregistered external frontier-model study that is **not yet reported**.

No frontier-model performance, OSWorld improvement, human-annotation agreement, or SOTA claim is fabricated.

## Files
- `main.tex` — paper source
- `references.bib` — verified bibliography
- `main.bbl` — prebuilt bibliography for robust arXiv compilation
- `neurips_2026.sty` — local preprint-compatible style implementation; see `STYLE_SOURCE_NOTE.md`
- `STYLE_SOURCE_NOTE.md` — provenance and conference-submission caveat
- `main.pdf` — compiled preprint

## arXiv upload
Upload the source files (including `main.bbl`) or the compiled PDF. For source upload, keep the `preprint` option and non-anonymous author information.

## Important conference-submission distinction
This package is appropriate as a public preprint. It is **not** an anonymous NeurIPS submission package. For any future NeurIPS submission:
- use the official style file for that submission year;
- use anonymous submission mode rather than `preprint`;
- follow that year's exact page limit and official checklist;
- remove identifying information and public-link leakage as required by the venue.

The official NeurIPS 2026 style ZIP could not be fetched directly inside the build runtime, so the included style is not claimed to be byte-identical to the official `.sty`. See `STYLE_SOURCE_NOTE.md`.
