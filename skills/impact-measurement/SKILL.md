---
name: impact-measurement
description: Measurement and responsible exit for institutional sustainable-finance research; return evidence-linked findings, assumptions, gaps and reviewable outputs.
license: MIT
metadata:
  author: HHFinAi
  version: "0.2.0"
---
# Measurement and responsible exit

Read `../../AGENTS.md` and `../../prompts/stages/measurement.md` relative to this skill directory. Obtain the current stage packet using the repository CLI. Do not create or claim unavailable source access.

## Task
Specify independent verification, baseline integrity, attrition, beneficiary consent, uncertainty and adverse outcomes. Show who pays for measurement and how disagreement is resolved. Document impact consequences of exit.

## Deliverable
Return the fields in `../../schemas/artifact.schema.json`; use the current run ID and input digest. Required sections: verification_plan, data_collection_rights, learning_and_adaptation, responsible_exit. Include source IDs, scope, periods, methods and material gaps. Call only allowlisted calculations with explicit provenance; missing evidence means NEEDS_DATA, not invented values.

## Limit
Reuses the conceptual structure of the Sovereign and Social-Impact Finance Agent, without replacing sovereign debt analysis. A mobilisation ratio is not proof of additionality. Benefit estimates are scenarios unless causal evidence is supplied.
