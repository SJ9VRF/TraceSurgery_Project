# Style source note

This arXiv package uses a local NeurIPS 2026 preprint-compatible style file that follows the 2026 official page geometry, title layout, font sizing, and `preprint` footer behavior documented in the official NeurIPS 2026 author kit and handbook.

The runtime used to build this artifact could read the official instructions but could not directly download the official ZIP from `media.neurips.cc`. Therefore this included `.sty` is **not claimed to be byte-identical** to the official distribution.

For an actual NeurIPS conference submission, replace `neurips_2026.sty` with the official 2026 style file from:
https://neurips.cc/Conferences/2026/CallForPapers

For arXiv, keep `\usepackage[preprint]{neurips_2026}` and do not use the `final` option unless the paper is accepted.
