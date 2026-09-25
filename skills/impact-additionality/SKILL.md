---
name: impact-additionality
description: Additionality and investor contribution for institutional sustainable-finance research; return evidence-linked findings, assumptions, gaps and reviewable outputs.
license: MIT
metadata:
  author: HHFinAi
  version: "0.2.0"
---
# Additionality and investor contribution

Read `../../AGENTS.md` and `../../prompts/stages/additionality.md` relative to this skill directory. Obtain the current stage packet using the repository CLI. Do not create or claim unavailable source access.

## Task
Test what would occur without the investment or support; distinguish enterprise impact from investor contribution. Compare realistic commercial alternatives and concessionality only where relevant. Require evidence rather than infer additionality from an emerging-market location or an SDG label.

## Deliverable
Return the fields in `../../schemas/artifact.schema.json`; use the current run ID and input digest. Required sections: financial_additionality, nonfinancial_contribution, market_counterfactual, minimum_support. Include source IDs, scope, periods, methods and material gaps. Call only allowlisted calculations with explicit provenance; missing evidence means NEEDS_DATA, not invented values.

## Limit
Reuses the conceptual structure of the Sovereign and Social-Impact Finance Agent, without replacing sovereign debt analysis. A mobilisation ratio is not proof of additionality. Benefit estimates are scenarios unless causal evidence is supplied.
