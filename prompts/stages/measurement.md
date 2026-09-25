# Measurement and responsible exit

## Decision context
What additional outcomes and financing are plausibly created, who bears the risks, and is the investment commercially and developmentally defensible?

## Assignment
Specify independent verification, baseline integrity, attrition, beneficiary consent, uncertainty and adverse outcomes. Show who pays for measurement and how disagreement is resolved. Document impact consequences of exit.

## Required output sections
- `verification_plan`: substantive analysis linked to claim IDs.
- `data_collection_rights`: substantive analysis linked to claim IDs.
- `learning_and_adaptation`: substantive analysis linked to claim IDs.
- `responsible_exit`: substantive analysis linked to claim IDs.

## Evidence and methodology
Use OPIM with edition, applicability, date and limitations. Source references are in `references/standards.json` from the repository root.

## Return contract
Return the structured artifact in `schemas/artifact.schema.json`; copy run_id, input_digest, stage_id and revision from the current packet. Never recycle IDs from a demo. Source uncertainty is not resolved by lowering confidence alone: preserve a gap or issue.

## Domain boundary
Reuses the conceptual structure of the Sovereign and Social-Impact Finance Agent, without replacing sovereign debt analysis. A mobilisation ratio is not proof of additionality. Benefit estimates are scenarios unless causal evidence is supplied.
