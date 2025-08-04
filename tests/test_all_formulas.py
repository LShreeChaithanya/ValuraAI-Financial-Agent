"""
test_all_formulas.py - Single comprehensive test file for all financial tools
Run with: pytest test_all_formulas.py -v
"""

import pytest
import math
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.tools.formulas import (
    future_value,
    present_value,
    rule_of_72,
    fv_annuity,
    pv_annuity,
    nper,
    explain_calculation
)


class TestAllFinancialFormulas:
    """Comprehensive test class for all financial formulas"""
    
    # ================================
    # FUTURE VALUE TESTS
    # ================================
    
    def test_future_value_basic(self):
        """Test basic future value calculation"""
        result = future_value.invoke({"pv": 1000, "r": 0.05, "n": 10})
        assert "1628.89" in result
        assert "Principal: $1000" in result
        assert "Rate: 5.0%" in result
    
    def test_future_value_high_rate(self):
        """Test future value with high interest rate"""
        result = future_value.invoke({"pv": 5000, "r": 0.12, "n": 5})
        assert "8811.71" in result
        assert "Rate: 12.0%" in result
    
    def test_future_value_zero_rate(self):
        """Test future value with zero interest"""
        result = future_value.invoke({"pv": 1000, "r": 0.0, "n": 5})
        assert "1000.00" in result
        assert "Rate: 0.0%" in result
    
    def test_future_value_long_term(self):
        """Test long-term investment"""
        result = future_value.invoke({"pv": 10000, "r": 0.07, "n": 30})
        assert "76122.55" in result
        assert "Periods: 30" in result
    
    # ================================
    # PRESENT VALUE TESTS
    # ================================
    
    def test_present_value_basic(self):
        """Test basic present value calculation"""
        result = present_value.invoke({"fv": 1628.89, "r": 0.05, "n": 10})
        assert "1000.00" in result
        assert "Future Value: $1628.89" in result
    
    def test_present_value_high_discount(self):
        """Test present value with high discount rate"""
        result = present_value.invoke({"fv": 10000, "r": 0.15, "n": 10})
        assert "2472.17" in result
        assert "Rate: 15.0%" in result
    
    def test_present_value_short_term(self):
        """Test short-term present value"""
        result = present_value.invoke({"fv": 1050, "r": 0.05, "n": 1})
        assert "1000.00" in result
        assert "Periods: 1" in result
    
    # ================================
    # RULE OF 72 TESTS
    # ================================
    
    def test_rule_of_72_standard(self):
        """Test Rule of 72 with standard rates"""
        result = rule_of_72.invoke({"r": 0.06})  # 6%
        assert "12.0 years" in result
        assert "6.0% interest" in result
    
    def test_rule_of_72_high_rate(self):
        """Test Rule of 72 with high rate"""
        result = rule_of_72.invoke({"r": 0.12})  # 12%
        assert "6.0 years" in result
        assert "12.0% interest" in result
    
    def test_rule_of_72_low_rate(self):
        """Test Rule of 72 with low rate"""
        result = rule_of_72.invoke({"r": 0.03})  # 3%
        assert "24.0 years" in result
        assert "3.0% interest" in result
    
    def test_rule_of_72_fractional(self):
        """Test Rule of 72 with fractional rate"""
        result = rule_of_72.invoke({"r": 0.075})  # 7.5%
        assert "9.6 years" in result
        assert "7.5% interest" in result
    
    def test_rule_of_72_zero_rate_error(self):
        """Test Rule of 72 with zero rate (should error)"""
        with pytest.raises(ZeroDivisionError):
            rule_of_72.invoke({"r": 0.0})
    
    # ================================
    # FUTURE VALUE ANNUITY TESTS
    # ================================
    
    def test_fv_annuity_basic(self):
        """Test basic FV annuity calculation"""
        result = fv_annuity.invoke({"pmt": 1000, "r": 0.05, "n": 10})
        assert "12577.89" in result
        assert "Payment: $1000" in result
        assert "Rate: 5.0%" in result
    
    def test_fv_annuity_monthly_savings(self):
        """Test monthly savings FV annuity"""
        result = fv_annuity.invoke({"pmt": 500, "r": 0.005, "n": 120})  # 10 years monthly
        assert "Payment: $500" in result
        assert "Rate: 0.5%" in result
        assert "Periods: 120" in result
    
    def test_fv_annuity_zero_rate(self):
        """Test FV annuity with zero interest"""
        result = fv_annuity.invoke({"pmt": 1000, "r": 0.0, "n": 10})
        assert "10000.00" in result  # Should be payment * periods
        assert "Rate: 0.0%" in result
    
    def test_fv_annuity_large_payment(self):
        """Test FV annuity with large payment"""
        result = fv_annuity.invoke({"pmt": 15000, "r": 0.005, "n": 624})
        assert "Payment: $15000" in result
        assert "Future Value of Annuity:" in result
    
    def test_fv_annuity_single_payment(self):
        """Test FV annuity with single payment"""
        result = fv_annuity.invoke({"pmt": 1000, "r": 0.05, "n": 1})
        assert "1000.00" in result
        assert "Periods: 1" in result
    
    # ================================
    # PRESENT VALUE ANNUITY TESTS
    # ================================
    
    def test_pv_annuity_basic(self):
        """Test basic PV annuity calculation"""
        result = pv_annuity.invoke({"pmt": 1000, "r": 0.05, "n": 10})
        assert "7721.73" in result
        assert "Payment: $1000" in result
        assert "Rate: 5.0%" in result
    
    def test_pv_annuity_mortgage(self):
        """Test mortgage-like PV annuity"""
        result = pv_annuity.invoke({"pmt": 2000, "r": 0.004167, "n": 360})  # 30-year mortgage
        assert "Payment: $2000" in result
        assert "Periods: 360" in result
    
    def test_pv_annuity_zero_rate(self):
        """Test PV annuity with zero interest"""
        result = pv_annuity.invoke({"pmt": 1000, "r": 0.0, "n": 10})
        assert "10000.00" in result  # Should be payment * periods
        assert "Rate: 0.0%" in result
    
    def test_pv_annuity_high_rate(self):
        """Test PV annuity with high interest rate"""
        result = pv_annuity.invoke({"pmt": 1000, "r": 0.15, "n": 5})
        assert "Present Value of Annuity:" in result
        assert "Rate: 15.0%" in result
    
    def test_pv_annuity_retirement(self):
        """Test retirement income PV annuity"""
        result = pv_annuity.invoke({"pmt": 3000, "r": 0.04, "n": 300})  # 25 years retirement
        assert "Payment: $3000" in result
        assert "Present Value of Annuity:" in result
    
    # ================================
    # NPER (NUMBER OF PERIODS) TESTS
    # ================================
    
    def test_nper_basic(self):
        """Test basic NPER calculation"""
        result = nper.invoke({"pv": 1000, "fv": 2000, "r": 0.07, "pmt": 0})
        assert "10.24" in result  # Should take about 10.24 periods to double
        assert "PV: $1000" in result
        assert "FV: $2000" in result
    
    def test_nper_with_payments(self):
        """Test NPER with regular payments"""
        result = nper.invoke({"pv": 0, "fv": 10000, "r": 0.05, "pmt": 500})
        assert "Number of Periods:" in result
        assert "Payment: $500" in result
        assert "Rate: 5.0%" in result
    
    def test_nper_retirement_scenario(self):
        """Test retirement savings NPER"""
        result = nper.invoke({"pv": 200000, "fv": 1000000, "r": 0.06, "pmt": 0})
        assert "Number of Periods:" in result
        assert "Rate: 6.0%" in result
        assert "PV: $200000" in result
    
    def test_nper_zero_rate(self):
        """Test NPER with zero interest rate"""
        result = nper.invoke({"pv": 1000, "fv": 5000, "r": 0.0, "pmt": 200})
        assert "20.00" in result  # (5000-1000)/200 = 20
        assert "Rate: 0.0%" in result
    
    def test_nper_savings_goal(self):
        """Test NPER for savings goal"""
        result = nper.invoke({"pv": 5000, "fv": 50000, "r": 0.08, "pmt": 1000})
        assert "Number of Periods:" in result
        assert "Payment: $1000" in result
    
    # ================================
    # EXPLAIN CALCULATION TESTS
    # ================================
    
    def test_explain_future_value(self):
        """Test explanation for future value"""
        result = explain_calculation.invoke({
            "calculation_type": "future_value",
            "parameters": {"pv": 1000, "r": 0.05, "n": 10}
        })
        assert "FV = PV × (1 + r)^n" in result
        assert "compound interest" in result
        assert "pv" in result.lower()
    
    def test_explain_present_value(self):
        """Test explanation for present value"""
        result = explain_calculation.invoke({
            "calculation_type": "present_value", 
            "parameters": {"fv": 1000, "r": 0.05, "n": 10}
        })
        assert "PV = FV ÷ (1 + r)^n" in result
        assert "discounts future money" in result
    
    def test_explain_rule_of_72(self):
        """Test explanation for Rule of 72"""
        result = explain_calculation.invoke({
            "calculation_type": "rule_of_72",
            "parameters": {"r": 0.06}
        })
        assert "Rule of 72" in result
        assert "doubling time" in result
        assert "72 ÷" in result
    
    def test_explain_fv_annuity(self):
        """Test explanation for FV annuity"""
        result = explain_calculation.invoke({
            "calculation_type": "fv_annuity",
            "parameters": {"pmt": 1000, "r": 0.05, "n": 10}
        })
        assert "Future Value of Annuity" in result
        assert "PMT ×" in result
        assert "((1 + r)^n - 1)" in result
    
    def test_explain_pv_annuity(self):
        """Test explanation for PV annuity"""
        result = explain_calculation.invoke({
            "calculation_type": "pv_annuity", 
            "parameters": {"pmt": 1000, "r": 0.05, "n": 10}
        })
        assert "Present Value of Annuity" in result
        assert "PMT ×" in result
        assert "(1 + r)^(-n)" in result
    
    def test_explain_nper(self):
        """Test explanation for NPER"""
        result = explain_calculation.invoke({
            "calculation_type": "nper",
            "parameters": {"pv": 1000, "fv": 2000, "r": 0.05}
        })
        assert "Number of Periods" in result
        assert "ln(FV/PV)" in result
        assert "ln(1 + r)" in result
    
    def test_explain_unknown_type(self):
        """Test explanation for unknown calculation type"""
        result = explain_calculation.invoke({
            "calculation_type": "unknown_calculation",
            "parameters": {"test": "value"}
        })
        assert "Explanation for unknown_calculation" in result
        assert "Parameters used:" in result
    
    # ================================
    # INTEGRATION TESTS
    # ================================
    
    def test_fv_pv_consistency(self):
        """Test that FV and PV calculations are inverse operations"""
        # Calculate FV
        fv_result = future_value.invoke({"pv": 1000, "r": 0.05, "n": 10})
        
        # Calculate PV using the result
        pv_result = present_value.invoke({"fv": 1628.89, "r": 0.05, "n": 10})
        
        # Should get back approximately $1000
        assert "1000.00" in pv_result
    
    def test_rule_72_vs_nper_accuracy(self):
        """Test Rule of 72 approximation vs actual NPER calculation"""
        # Rule of 72 for 6% should be 12 years
        rule72_result = rule_of_72.invoke({"r": 0.06})
        assert "12.0 years" in rule72_result
        
        # NPER for doubling should be close to 12
        nper_result = nper.invoke({"pv": 1000, "fv": 2000, "r": 0.06, "pmt": 0})
        # Should be approximately 11.9 years (Rule of 72 is an approximation)
        assert "11.9" in nper_result
    
    def test_annuity_consistency(self):
        """Test that annuity calculations work with same parameters"""
        params = {"pmt": 1000, "r": 0.05, "n": 10}
        
        # Both should complete without error
        fv_result = fv_annuity.invoke(params)
        pv_result = pv_annuity.invoke(params)
        
        assert "Future Value of Annuity:" in fv_result
        assert "Present Value of Annuity:" in pv_result
        assert "Payment: $1000" in fv_result
        assert "Payment: $1000" in pv_result
    
    # ================================
    # PARAMETRIZED TESTS
    # ================================
    
    @pytest.mark.parametrize("pv,r,n,expected_contains", [
        (1000, 0.05, 10, "1628.89"),
        (5000, 0.03, 5, "5796.37"),
        (10000, 0.08, 20, "46609.57"),
        (2500, 0.06, 15, "5991.48"),
    ])
    def test_future_value_multiple_scenarios(self, pv, r, n, expected_contains):
        """Test future value with multiple parameter combinations"""
        result = future_value.invoke({"pv": pv, "r": r, "n": n})
        assert expected_contains in result
        assert f"Principal: ${pv}" in result
        assert f"Rate: {r*100}%" in result
    
    @pytest.mark.parametrize("rate,expected_years", [
        (0.06, "12.0"),  # 6% -> 12 years
        (0.09, "8.0"),   # 9% -> 8 years
        (0.12, "6.0"),   # 12% -> 6 years
        (0.04, "18.0"),  # 4% -> 18 years
    ])
    def test_rule_of_72_multiple_rates(self, rate, expected_years):
        """Test Rule of 72 with multiple interest rates"""
        result = rule_of_72.invoke({"r": rate})
        assert f"{expected_years} years" in result
        assert f"{rate*100}% interest" in result
    
    # ================================
    # ERROR HANDLING TESTS
    # ================================
    
    def test_missing_parameters_error(self):
        """Test error handling for missing parameters"""
        with pytest.raises(Exception):
            future_value.invoke({"pv": 1000, "r": 0.05})  # Missing 'n'
        
        with pytest.raises(Exception):
            present_value.invoke({"fv": 1000})  # Missing 'r' and 'n'
    
    def test_invalid_parameter_types(self):
        """Test error handling for invalid parameter types"""
        with pytest.raises(Exception):
            future_value.invoke({"pv": "invalid", "r": 0.05, "n": 10})
        
        with pytest.raises(Exception):
            rule_of_72.invoke({"r": "not_a_number"})
    
    # ================================
    # EDGE CASES
    # ================================
    
    def test_very_large_numbers(self):
        """Test calculations with very large numbers"""
        result = future_value.invoke({"pv": 1000000, "r": 0.05, "n": 50})
        assert "Future Value:" in result
        assert "Principal: $1000000" in result
    
    def test_very_small_rates(self):
        """Test calculations with very small interest rates"""
        result = future_value.invoke({"pv": 1000, "r": 0.001, "n": 10})  # 0.1%
        assert "Future Value:" in result
        assert "Rate: 0.1%" in result
    
    def test_fractional_periods(self):
        """Test calculations with fractional periods"""
        result = future_value.invoke({"pv": 1000, "r": 0.05, "n": 5.5})
        assert "Future Value:" in result
        assert "Periods: 5.5" in result
    
    # ================================
    # PERFORMANCE TESTS
    # ================================
    
    @pytest.mark.performance
    def test_calculation_speed(self):
        """Test that calculations complete quickly"""
        import time
        
        start_time = time.time()
        
        # Run multiple calculations
        for i in range(100):
            future_value.invoke({"pv": 1000 + i, "r": 0.05, "n": 10})
            present_value.invoke({"fv": 2000 + i, "r": 0.05, "n": 10})
        
        elapsed_time = time.time() - start_time
        
        # Should complete 200 calculations in under 1 second
        assert elapsed_time < 1.0


# ================================
# UTILITY FUNCTIONS FOR TESTING
# ================================

def extract_dollar_amount(result_string):
    """Extract dollar amount from result string for numerical comparison"""
    import re
    match = re.search(r'\$(\d+(?:,\d{3})*\.\d{2})', result_string)
    if match:
        return float(match.group(1).replace(',', ''))
    return None



if __name__ == "__main__":
    
    pytest.main([__file__, "-v", "--tb=short"])