# Contracts and risk allocation

## Decision context
What additional outcomes and financing are plausibly created, who bears the risks, and is the investment commercially and developmentally defensible?

## Assignment
Map each tranche, guarantee, eligibility restriction, trigger, expiry, cap, recourse and payment timing. Separate funded first loss from unfunded guarantees. A guarantee transfers specified risk; it does not remove guarantor, liquidity or FX risk.

## Required output sections
- `capital_stack`: substantive analysis linked to claim IDs.
- `guarantees_and_recourse`: substantive analysis linked to claim IDs.
- `fx_and_payment_risk`: substantive analysis linked to claim IDs.
- `rights_and_safeguards`: substantive analysis linked to claim IDs.

## Evidence and methodology
Use OECD-BLENDED, UNGP with edition, applicability, date and limitations. Source references are in `references/standards.json` from the repository root.

## Return contract
Return the structured artifact in `schemas/artifact.schema.json`; copy run_id, input_digest, stage_id and revision from the current packet. Never recycle IDs from a demo. Source uncertainty is not resolved by lowering confidence alone: preserve a gap or issue.

## Domain boundary
Reuses the conceptual structure of the Sovereign and Social-Impact Finance Agent, without replacing sovereign debt analysis. A mobilisation ratio is not proof of additionality. Benefit estimates are scenarios unless causal evidence is supplied.
