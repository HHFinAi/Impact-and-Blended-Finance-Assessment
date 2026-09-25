"""Original HHFinAi domain arithmetic tests; all numbers are synthetic."""
import copy, math, random, unittest
from sf_agent.analytics import *
from sf_agent.validation import DataError

class Impact(unittest.TestCase):
    def test_waterfall(self):
        r=loss_waterfall(15,10,20,70);self.assertEqual(r['junior_loss'],10);self.assertEqual(r['mezzanine_loss'],5);self.assertEqual(r['senior_loss'],0)
    def test_loss_reconciles(self):
        for loss in range(101):
            r=loss_waterfall(loss,10,20,70);self.assertEqual(r['total_allocated_loss'],loss);self.assertEqual(sum(r['recoveries_after_loss']),100-loss)
    def test_overloss_rejected(self):
        with self.assertRaises(DataError):loss_waterfall(101,10,20,70)
    def test_zero_loss(self):self.assertEqual(loss_waterfall(0,10,20,70)['total_allocated_loss'],0)
    def test_grant_equivalent_market_terms_zero(self):self.assertAlmostEqual(grant_equivalent(100,[110],.1)['grant_equivalent_amount'],0)
    def test_grant_equivalent_full(self):self.assertEqual(grant_equivalent(100,[0],.1)['grant_equivalent_fraction'],1)
    def test_negative_repayment_rejected(self):
        with self.assertRaises(DataError):grant_equivalent(100,[-10],.1)
    def test_mobilisation_ratio(self):self.assertEqual(mobilisation_ratio(300,100)['commercial_per_development'],3)
    def test_mobilisation_not_causal(self):self.assertIs(mobilisation_ratio(300,100)['causal_additionality_proven'],False)
    def test_adjusted_outcomes(self):self.assertAlmostEqual(additional_outcomes(100,40,.1,.5)['adjusted_incremental'],27)
    def test_negative_outcome_not_floored(self):self.assertLess(additional_outcomes(20,40,0,1)['adjusted_incremental'],0)
    def test_invalid_displacement(self):
        with self.assertRaises(DataError):additional_outcomes(100,40,1.1,1)
    def test_cost_effectiveness(self):self.assertEqual(cost_per_additional_outcome(100,20),5)
    def test_zero_additionality_cost_not_computed(self):
        with self.assertRaises(DataError):cost_per_additional_outcome(100,0)

if __name__=='__main__':unittest.main()
