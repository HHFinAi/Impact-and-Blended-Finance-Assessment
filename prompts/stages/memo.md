# Investment committee and accountable review

## Decision context
What additional outcomes and financing are plausibly created, who bears the risks, and is the investment commercially and developmentally defensible?

## Assignment
Integrate findings without changing their qualification. Separate facts, inferences, assumptions and calculations; cite evidence IDs and dates. Preserve unknown conclusions. Complete the domain-assessment declarations, register unresolved material issues, and submit for human research review. Do not certify legal compliance or investment performance.

## Required output sections
- `investment_question_and_answer`: substantive analysis linked to claim IDs.
- `financial_vs_sustainability_conclusions`: substantive analysis linked to claim IDs.
- `evidence_and_calculations`: substantive analysis linked to claim IDs.
- `decision_conditions_and_limits`: substantive analysis linked to claim IDs.

## Evidence and methodology
Use the mandate and registered primary evidence with edition, applicability, date and limitations. Source references are in `references/standards.json` from the repository root.

## Return contract
Return the structured artifact in `schemas/artifact.schema.json`; copy run_id, input_digest, stage_id and revision from the current packet. Never recycle IDs from a demo. Source uncertainty is not resolved by lowering confidence alone: preserve a gap or issue.

## Domain boundary
Reuses the conceptual structure of the Sovereign and Social-Impact Finance Agent, without replacing sovereign debt analysis. A mobilisation ratio is not proof of additionality. Benefit estimates are scenarios unless causal evidence is supplied.

Required typed domain-assessment fields (declarations, not automated truth verification):
```json
{
  "enterprise_vs_investor_impact_separate": [
    true
  ],
  "counterfactual_status": [
    "supported",
    "assumed",
    "unknown"
  ],
  "mobilisation_is_causal_proof": [
    false
  ],
  "guarantee_removes_all_risk": [
    false
  ],
  "negative_impacts_considered": [
    true
  ]
}
```
