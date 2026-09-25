# Additionality and investor contribution

## Decision context
What additional outcomes and financing are plausibly created, who bears the risks, and is the investment commercially and developmentally defensible?

## Assignment
Test what would occur without the investment or support; distinguish enterprise impact from investor contribution. Compare realistic commercial alternatives and concessionality only where relevant. Require evidence rather than infer additionality from an emerging-market location or an SDG label.

## Required output sections
- `financial_additionality`: substantive analysis linked to claim IDs.
- `nonfinancial_contribution`: substantive analysis linked to claim IDs.
- `market_counterfactual`: substantive analysis linked to claim IDs.
- `minimum_support`: substantive analysis linked to claim IDs.

## Evidence and methodology
Use OECD-BLENDED, OPIM with edition, applicability, date and limitations. Source references are in `references/standards.json` from the repository root.

## Return contract
Return the structured artifact in `schemas/artifact.schema.json`; copy run_id, input_digest, stage_id and revision from the current packet. Never recycle IDs from a demo. Source uncertainty is not resolved by lowering confidence alone: preserve a gap or issue.

## Domain boundary
Reuses the conceptual structure of the Sovereign and Social-Impact Finance Agent, without replacing sovereign debt analysis. A mobilisation ratio is not proof of additionality. Benefit estimates are scenarios unless causal evidence is supplied.
