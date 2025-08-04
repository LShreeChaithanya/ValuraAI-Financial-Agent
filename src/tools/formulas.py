# app/agent/calculations.py
import math
from langchain_core.tools import tool

@tool
def future_value(pv: float, r: float, n: int) -> float:
    """Calculate Future Value: FV = PV * (1 + r)^n"""
    return pv * (1 + r) ** n

@tool
def present_value(fv: float, r: float, n: int) -> float:
    """Calculate Present Value: PV = FV / (1 + r)^n"""
    return fv / (1 + r) ** n
@tool
def fv_annuity(pmt: float, r: float, n: int) -> float:
    """Calculate Future Value of Annuity: FV = PMT * [(1 + r)^n - 1] / r"""
    return pmt * ((1 + r) ** n - 1) / r

@tool
def pv_annuity(pmt: float, r: float, n: int) -> float:
    """Calculate Present Value of Annuity: PV = PMT * [1 - (1 + r)^(-n)] / r"""
    return pmt * (1 - (1 + r) ** (-n)) / r
@tool
def nper(rate: float, pmt: float, pv: float, fv: float) -> float:
    """Calculate Number of Periods (Excel-style NPER)"""
    if pmt == 0:
        return math.log(fv / pv) / math.log(1 + rate)
    return math.log((fv * rate + pmt) / (pv * rate + pmt)) / math.log(1 + rate)

@tool
def rule_of_72(rate: float) -> float:
    """Calculate years to double investment: Years = 72 / rate%"""
    return 72 / (rate * 100)

@tool
def explain_calculation(calc_type: str, **kwargs) -> str:
    """Explain the calculation with formula and steps"""
    if calc_type == "fv":
        pv, r, n = kwargs["pv"], kwargs["r"], kwargs["n"]
        result = future_value(pv, r, n)
        return f"Future Value: FV = {pv} * (1 + {r})^{n} = {result:.2f}"
    # Add explanations for other calculations similarly
    return "Explanation not implemented for this calculation."