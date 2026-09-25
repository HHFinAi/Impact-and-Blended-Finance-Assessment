---
name: impact-blended-finance-agent
description: What additional outcomes and financing are plausibly created, who bears the risks, and is the investment commercially and developmentally defensible? Institutional buy-side research workflow with auditable evidence, calculations and human review; no autonomous trading.
license: MIT
metadata:
  author: HHFinAi
  version: "0.2.0"
---
# Impact and Blended-Finance Assessment Agent

Use for impact and blended finance under a specified investment mandate. Read `AGENTS.md`, then select a route from `agent.json`. Follow `WORKFLOW.md` and the CLI research loop. Copy the entire repository, not just this file: scripts, prompts, schemas and references are required.

A compatible filesystem-enabled agent host may discover this skill; activation has not been certified for specific products. Text-only use applies the methodology manually and does not enforce the Python controls.

Reuses the conceptual structure of the Sovereign and Social-Impact Finance Agent, without replacing sovereign debt analysis. A mobilisation ratio is not proof of additionality. Benefit estimates are scenarios unless causal evidence is supplied.

Do not run a synthetic fixture as live research. Start with `examples/research-request-template.json`, replace every placeholder and register permitted evidence. Inspect `docs/INSTITUTIONAL_QUALITY.md` and `docs/AUDIT.md` before relying on outputs.
