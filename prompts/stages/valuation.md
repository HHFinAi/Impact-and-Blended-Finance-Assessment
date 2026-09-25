# Financial and development economics

## Decision context
What additional outcomes and financing are plausibly created, who bears the risks, and is the investment commercially and developmentally defensible?

## Assignment
Compute bounded loss allocation, grant-equivalent subsidy or outcome-sensitivity arithmetic. Do not equate grant-equivalent with a donation or causal impact. Keep payer affordability, investor return and outcome cost-effectiveness in separate exhibits.

## Required output sections
- `grant_equivalent`: substantive analysis linked to claim IDs.
- `loss_waterfall`: substantive analysis linked to claim IDs.
- `mobilisation_denominator`: substantive analysis linked to claim IDs.
- `outcome_sensitivity`: substantive analysis linked to claim IDs.

## Evidence and methodology
Use OECD-BLENDED, OPIM with edition, applicability, date and limitations. Source references are in `references/standards.json` from the repository root.

## Return contract
Return the structured artifact in `schemas/artifact.schema.json`; copy run_id, input_digest, stage_id and revision from the current packet. Never recycle IDs from a demo. Source uncertainty is not resolved by lowering confidence alone: preserve a gap or issue.

## Domain boundary
Reuses the conceptual structure of the Sovereign and Social-Impact Finance Agent, without replacing sovereign debt analysis. A mobilisation ratio is not proof of additionality. Benefit estimates are scenarios unless causal evidence is supplied.

A domain calculation must pass recomputation. The minimal runnable illustration is `loss_waterfall`; other needed specialist models must remain explicitly external and independently reviewed.
