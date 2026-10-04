# Annotation quality protocol

Use a frozen ontology and a hidden gold subset after pilot refinement. Two annotators independently label failure event, earliest causal failure, recoverability class, recovery-window bounds, and causal edges. Annotators must not see model identity in the blinded pass.

Report per-label prevalence, raw agreement, Cohen's kappa for categorical labels, boundary agreement for recovery windows, and adjudication rate. Low-prevalence labels should include prevalence-adjusted interpretation rather than relying on kappa alone. A third adjudicator resolves disagreements without seeing the paper hypothesis.

Automatic or LLM labels are candidates only until calibrated against the human gold subset. Report precision/recall/F1 by failure family and never silently overwrite human labels.
