---
name: impact-structure
description: Contracts and risk allocation for institutional sustainable-finance research; return evidence-linked findings, assumptions, gaps and reviewable outputs.
license: MIT
metadata:
  author: HHFinAi
  version: "0.2.0"
---
# Contracts and risk allocation

Read `../../AGENTS.md` and `../../prompts/stages/structure.md` relative to this skill directory. Obtain the current stage packet using the repository CLI. Do not create or claim unavailable source access.

## Task
Map each tranche, guarantee, eligibility restriction, trigger, expiry, cap, recourse and payment timing. Separate funded first loss from unfunded guarantees. A guarantee transfers specified risk; it does not remove guarantor, liquidity or FX risk.

## Deliverable
Return the fields in `../../schemas/artifact.schema.json`; use the current run ID and input digest. Required sections: capital_stack, guarantees_and_recourse, fx_and_payment_risk, rights_and_safeguards. Include source IDs, scope, periods, methods and material gaps. Call only allowlisted calculations with explicit provenance; missing evidence means NEEDS_DATA, not invented values.

## Limit
Reuses the conceptual structure of the Sovereign and Social-Impact Finance Agent, without replacing sovereign debt analysis. A mobilisation ratio is not proof of additionality. Benefit estimates are scenarios unless causal evidence is supplied.
