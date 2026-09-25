# Worked example — Impact and Blended-Finance Assessment Agent

**SYNTHETIC / RESEARCH_ONLY. All company, portfolio, instrument and outcome values are fictional. No capital should be deployed from this example.**

## Investment-relevant observation
A funded structure has junior/mezzanine/senior capital of 10/20/70 million. A 15 million loss consumes **10 million junior and 5 million mezzanine capital**, leaving senior capital untouched under the stated sequential-loss assumption.

## Reproduce the arithmetic
From the repository root:
```bash
python -m sf_agent calc --operation loss_waterfall --arguments examples/calculation-arguments.json
```

### Inputs
```json
{
  "total_loss": 15000000,
  "junior_capital": 10000000,
  "mezzanine_capital": 20000000,
  "senior_capital": 70000000
}
```

### Recomputed result
```json
{
  "junior_loss": 10000000.0,
  "mezzanine_loss": 5000000.0,
  "senior_loss": 0.0,
  "total_allocated_loss": 15000000.0,
  "recoveries_after_loss": [
    0.0,
    15000000.0,
    70000000.0
  ]
}
```

## What the result does not establish
This is loss redistribution, not loss elimination. Check waterfall contracts, guarantee caps, FX, liquidity, recovery timing and counterparty credit. Additionality and beneficiary outcomes need a separate counterfactual and verification plan.

## Diligence handoff
Fictional blended structure: first-loss protection redistributes losses; additionality and beneficiary outcomes still need evidence.

Register source-backed inputs, contrary evidence, material data gaps and the investment constraints before replacing this illustrative result with actual research. Unit, boundary, timing, attribution and legal judgments are not supplied by arithmetic alone. No human research approval is recorded for this example.
