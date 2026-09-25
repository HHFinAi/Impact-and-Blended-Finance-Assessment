---
name: impact-valuation
description: Financial and development economics for institutional sustainable-finance research; return evidence-linked findings, assumptions, gaps and reviewable outputs.
license: MIT
metadata:
  author: HHFinAi
  version: "0.2.0"
---
# Financial and development economics

Read `../../AGENTS.md` and `../../prompts/stages/valuation.md` relative to this skill directory. Obtain the current stage packet using the repository CLI. Do not create or claim unavailable source access.

## Task
Compute bounded loss allocation, grant-equivalent subsidy or outcome-sensitivity arithmetic. Do not equate grant-equivalent with a donation or causal impact. Keep payer affordability, investor return and outcome cost-effectiveness in separate exhibits.

## Deliverable
Return the fields in `../../schemas/artifact.schema.json`; use the current run ID and input digest. Required sections: grant_equivalent, loss_waterfall, mobilisation_denominator, outcome_sensitivity. Include source IDs, scope, periods, methods and material gaps. Call only allowlisted calculations with explicit provenance; missing evidence means NEEDS_DATA, not invented values.

## Limit
Reuses the conceptual structure of the Sovereign and Social-Impact Finance Agent, without replacing sovereign debt analysis. A mobilisation ratio is not proof of additionality. Benefit estimates are scenarios unless causal evidence is supplied.
