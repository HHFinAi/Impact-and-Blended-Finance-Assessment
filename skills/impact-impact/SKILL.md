---
name: impact-impact
description: Theory of change and beneficiaries for institutional sustainable-finance research; return evidence-linked findings, assumptions, gaps and reviewable outputs.
license: MIT
metadata:
  author: HHFinAi
  version: "0.2.0"
---
# Theory of change and beneficiaries

Read `../../AGENTS.md` and `../../prompts/stages/impact.md` relative to this skill directory. Obtain the current stage packet using the repository CLI. Do not create or claim unavailable source access.

## Task
Define who benefits, how much, for how long and compared with what. Separate outputs, outcomes and impacts. Include harms, displacement, leakage and persistence with non-overlapping definitions; retain confidence and alternative explanations.

## Deliverable
Return the fields in `../../schemas/artifact.schema.json`; use the current run ID and input digest. Required sections: problem_baseline, counterfactual, outcomes_vs_outputs, negative_effects. Include source IDs, scope, periods, methods and material gaps. Call only allowlisted calculations with explicit provenance; missing evidence means NEEDS_DATA, not invented values.

## Limit
Reuses the conceptual structure of the Sovereign and Social-Impact Finance Agent, without replacing sovereign debt analysis. A mobilisation ratio is not proof of additionality. Benefit estimates are scenarios unless causal evidence is supplied.
