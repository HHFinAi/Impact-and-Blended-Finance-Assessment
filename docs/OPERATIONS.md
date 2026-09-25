# Executable operation catalogue

Every operation requires supplied assumptions/provenance. No market or issuer data are inferred.

## `additional_outcomes`
```python
additional_outcomes(observed_outcomes: 'float', counterfactual_outcomes: 'float', displacement_fraction: 'float', persistence_fraction: 'float') -> 'dict'
```
See source code and domain methodology for assumptions.

Input units: `{"observed_outcomes": "$outcome", "counterfactual_outcomes": "$outcome", "displacement_fraction": "decimal", "persistence_fraction": "decimal"}`. Output unit/type: `additional_outcomes_scenario`.

## `cost_per_additional_outcome`
```python
cost_per_additional_outcome(total_cost: 'float', additional_outcomes: 'float') -> 'float'
```
See source code and domain methodology for assumptions.

Input units: `{"total_cost": "$money", "additional_outcomes": "$outcome"}`. Output unit/type: `money_per_outcome`.

## `dscr`
```python
dscr(cash_available: 'float', debt_service: 'float') -> 'float'
```
See source code and domain methodology for assumptions.

Input units: `{"cash_available": "$money", "debt_service": "$money"}`. Output unit/type: `multiple`.

## `grant_equivalent`
```python
grant_equivalent(disbursement: 'float', annual_repayments: 'list[float]', market_discount_rate: 'float') -> 'dict'
```
See source code and domain methodology for assumptions.

Input units: `{"disbursement": "$money", "annual_repayments": "$money", "market_discount_rate": "decimal"}`. Output unit/type: `grant_equivalent_scenario`.

## `holding_period_return`
```python
holding_period_return(initial_dirty_price: 'float', exit_dirty_price: 'float', cash_income: 'float', funding_cost: 'float', transaction_cost: 'float') -> 'float'
```
See source code and domain methodology for assumptions.

Input units: `{"initial_dirty_price": "$money", "exit_dirty_price": "$money", "cash_income": "$money", "funding_cost": "$money", "transaction_cost": "$money"}`. Output unit/type: `decimal_return`.

## `loss_waterfall`
```python
loss_waterfall(total_loss: 'float', junior_capital: 'float', mezzanine_capital: 'float', senior_capital: 'float') -> 'dict'
```
See source code and domain methodology for assumptions.

Input units: `{"total_loss": "$money", "junior_capital": "$money", "mezzanine_capital": "$money", "senior_capital": "$money"}`. Output unit/type: `loss_allocation`.

## `mobilisation_ratio`
```python
mobilisation_ratio(incremental_commercial_finance: 'float', development_finance: 'float') -> 'dict'
```
See source code and domain methodology for assumptions.

Input units: `{"incremental_commercial_finance": "$money", "development_finance": "$money"}`. Output unit/type: `mobilisation_ratio`.

## `npv`
```python
npv(cashflows: 'list[float]', annual_discount: 'float') -> 'float'
```
Periodic NPV; cashflows[0] is at time zero, then annual periods.

Input units: `{"cashflows": "$money", "annual_discount": "decimal"}`. Output unit/type: `$money`.

## `scale`
```python
scale(value: 'float', factor: 'float') -> 'float'
```
Explicit arithmetic conversion; external unit semantics need human review.

Input units: `{"value": "$input_unit", "factor": "conversion_factor"}`. Output unit/type: `$output_unit`.
