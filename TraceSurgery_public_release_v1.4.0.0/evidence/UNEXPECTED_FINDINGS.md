# Unexpected findings

These are observations from executed local investigations, not post-hoc model-performance stories.

## U-001 - The "right" repair family changes after a single state transition

We initially might expect a wrong action to remain an action-level problem throughout the trace. It does not. At checkpoint 0, correcting the action or replacing the suffix recovers. At checkpoint 1, after the wrong value is committed, those interventions fail and state repair succeeds.

**Why this matters:** recoverability is temporal. A single root-cause label loses information about *when* a repair family remains sufficient.

## U-002 - Correct state is not enough if the future policy will corrupt it again

The checkpoint-0 state patch restores a valid pre-state but still fails because the recorded next action rewrites the wrong value.

**Why this matters:** "repair state" and "repair policy" are not interchangeable, even in a two-action toy trace.

## U-003 - A valid alternative continuation is not automatically a recovery policy

Suffix replanning at checkpoint 1 fails because the alternative continuation does not contain an operation that repairs the already-corrupted world state.

**Why this matters:** evaluating only whether a new plan differs from the failed plan can overstate recoverability. The new suffix must be sufficient relative to the current state.

## U-004 - Stronger evidence gates improved the project more than larger local headline numbers

The 500-task suite passes cleanly, but the project deliberately does not turn that into a performance headline. The most consequential maturity changes were replay admissibility, provenance verification, fail-closed reporting, and explicit separation of privileged oracle surgery from agent-realizable recovery.

**Why this matters:** for causal agent evaluation, evidence hygiene is part of the method, not release polish.
