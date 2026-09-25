"""Illustrative impact/blended-finance economics with explicit counterfactual limits."""
from __future__ import annotations
from .maths import COMMON_OPERATIONS, checked, fraction, number, operation, positive, require, series, npv

@operation({'total_loss':'$money','junior_capital':'$money','mezzanine_capital':'$money','senior_capital':'$money'},'loss_allocation')
def loss_waterfall(total_loss: float,junior_capital: float,mezzanine_capital: float,senior_capital: float) -> dict:
    caps=[checked(c,k,0) for c,k in [(junior_capital,'junior'),(mezzanine_capital,'mezzanine'),(senior_capital,'senior')]]
    loss=checked(total_loss,'total_loss',0,sum(caps));rem=loss;alloc=[]
    for cap in caps:take=min(rem,cap);alloc.append(take);rem-=take
    return {'junior_loss':alloc[0],'mezzanine_loss':alloc[1],'senior_loss':alloc[2],
            'total_allocated_loss':sum(alloc),'recoveries_after_loss':[c-l for c,l in zip(caps,alloc)]}

@operation({'disbursement':'$money','annual_repayments':'$money','market_discount_rate':'decimal'},'grant_equivalent_scenario')
def grant_equivalent(disbursement: float,annual_repayments: list[float],market_discount_rate: float) -> dict:
    d=positive(disbursement,'disbursement');cfs=series(annual_repayments,'annual_repayments')
    require(all(c>=0 for c in cfs),'repayments must be nonnegative');pv=npv([0]+cfs,market_discount_rate)
    return {'repayment_pv':pv,'grant_equivalent_amount':d-pv,'grant_equivalent_fraction':(d-pv)/d,
            'not_official_oda_grant_equivalent':True}

@operation({'incremental_commercial_finance':'$money','development_finance':'$money'},'mobilisation_ratio')
def mobilisation_ratio(incremental_commercial_finance: float,development_finance: float) -> dict:
    numerator=checked(incremental_commercial_finance,'incremental_commercial_finance',0);denominator=positive(development_finance,'development_finance')
    return {'commercial_per_development':numerator/denominator,'causal_additionality_proven':False}

@operation({'observed_outcomes':'$outcome','counterfactual_outcomes':'$outcome','displacement_fraction':'decimal','persistence_fraction':'decimal'},'additional_outcomes_scenario')
def additional_outcomes(observed_outcomes: float,counterfactual_outcomes: float,displacement_fraction: float,persistence_fraction: float) -> dict:
    observed=number(observed_outcomes,'observed_outcomes');counter=number(counterfactual_outcomes,'counterfactual_outcomes')
    displacement=fraction(displacement_fraction,'displacement_fraction');persistence=fraction(persistence_fraction,'persistence_fraction')
    delta=observed-counter
    return {'gross_incremental':delta,'adjusted_incremental':delta*(1-displacement)*persistence,
            'counterfactual_is_supplied_not_estimated':True}

@operation({'total_cost':'$money','additional_outcomes':'$outcome'},'money_per_outcome')
def cost_per_additional_outcome(total_cost: float,additional_outcomes: float) -> float:
    return checked(total_cost,'total_cost',0)/positive(additional_outcomes,'additional_outcomes')
OPERATIONS=dict(COMMON_OPERATIONS)
OPERATIONS.update({f.__name__:f for f in (loss_waterfall,grant_equivalent,mobilisation_ratio,additional_outcomes,cost_per_additional_outcome)})
