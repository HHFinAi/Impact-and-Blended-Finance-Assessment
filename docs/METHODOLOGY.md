# Methodology and model boundaries

Reuses the conceptual structure of the Sovereign and Social-Impact Finance Agent, without replacing sovereign debt analysis. A mobilisation ratio is not proof of additionality. Benefit estimates are scenarios unless causal evidence is supplied.

## Analytical outputs
- Theory of change and counterfactual
- Investor contribution and additionality dossier
- Concessionality and loss-allocation model
- Financial return and outcome evidence kept separate

## Calculation library
The implementation is in `sf_agent/analytics.py`; generic helpers are in `sf_agent/maths.py`. Every exposed operation has argument-unit and result-unit metadata and is callable with `python -m sf_agent calc`. Arguments are not sourced automatically. See the operation inventory below, the worked example and domain regression tests.

### Impact and financing calculations
`loss_waterfall` allocates a supplied total funded loss sequentially across junior, mezzanine and senior capital; losses cannot exceed total funded capital. Unfunded guarantees, recovery timing, interest, currency and triggers need separate contractual models. Risk transfer does not eliminate loss.

`grant_equivalent` is disbursement minus discounted annual contractual repayments using a supplied market rate. This is an economic subsidy illustration, not the official OECD ODA grant-equivalent formula or a causal-impact measure. `mobilisation_ratio` divides supplied incremental commercial capital by development capital and does not prove either incrementality or attribution.

`additional_outcomes` applies explicit displacement and persistence adjustments to a signed observed-minus-counterfactual change. Definitions must not overlap or double count; this deliberately simple multiplicative scenario is not a statistical treatment-effect estimator. Negative values are retained, but applying the same multipliers to negative outcomes may understate harms: document harms separately and do not rely on this helper as a safeguards assessment. `cost_per_additional_outcome` requires a positive additional-outcome denominator; zero/negative effects cannot be presented as positive cost-effectiveness.


## Evidence status
Causal and legal interpretations remain human judgments. The software is not a complete implementation or certification of the referenced standards. Read the exact applicable original documents; the dated source register gives the verification scope. Proposed changes and future validation dates must not be applied retrospectively or represented as current law.
