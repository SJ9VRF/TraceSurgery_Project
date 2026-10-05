# TraceSurgery — 90-second video storyboard

**Status:** storyboard ready; a polished results video is intentionally not published until the external study produces real model trajectories.

1. **0–10 s — Hook**: "A debugger can tell you which step looks wrong. But did that step actually cause the failure?" Show one failed trajectory.
2. **10–25 s — Control**: Freeze at checkpoint t. Replay the exact state and suffix with no intervention. If the failure does not reproduce, the checkpoint is rejected for causal use.
3. **25–50 s — Surgery**: Branch action patch, state patch, and suffix replan. Animate success/failure cells filling the recovery surface.
4. **50–65 s — Mechanism**: Show the spreadsheet demo: 41 vs 42. Action repair works before the bad write; state repair works after it.
5. **65–80 s — What it measures**: Diagnosis faithfulness, last recoverable checkpoint, recovery AUC, irreversibility frontier.
6. **80–90 s — Evidence boundary**: "Local artifact validated. Frontier study pending. No causal claim without replay; no SOTA claim without matched experiments."
