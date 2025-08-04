


# tools/formulas.py - Updated to match Gemini's parameter names

# tools/formulas.py - Updated to match Gemini's parameter names

from langchain_core.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class FutureValueInput(BaseModel):
    pv: float = Field(description="Present value (initial investment)")
    r: float = Field(description="Interest rate as decimal (e.g., 0.05 for 5%)")
    n: float = Field(description="Number of periods")

class FutureValueTool(BaseTool):
    name: str = "future_value"
    description: str = "Calculate future value of an investment using FV = PV * (1 + r)^n"
    args_schema: Type[BaseModel] = FutureValueInput

    def _run(self, pv: float, r: float, n: float) -> str:
        future_val = pv * (1 + r) ** n
        return f"Future Value: ${future_val:.2f} (Principal: ${pv}, Rate: {r*100}%, Periods: {n})"

class PresentValueInput(BaseModel):
    fv: float = Field(description="Future value")
    r: float = Field(description="Interest rate as decimal")
    n: float = Field(description="Number of periods")

class PresentValueTool(BaseTool):
    name: str = "present_value"
    description: str = "Calculate present value using PV = FV / (1 + r)^n"
    args_schema: Type[BaseModel] = PresentValueInput

    def _run(self, fv: float, r: float, n: float) -> str:
        present_val = fv / (1 + r) ** n
        return f"Present Value: ${present_val:.2f} (Future Value: ${fv}, Rate: {r*100}%, Periods: {n})"

class RuleOf72Input(BaseModel):
    r: float = Field(description="Interest rate as decimal")

class RuleOf72Tool(BaseTool):
    name: str = "rule_of_72"
    description: str = "Calculate years to double investment using Rule of 72"
    args_schema: Type[BaseModel] = RuleOf72Input

    def _run(self, r: float) -> str:
        years = 72 / (r * 100)
        return f"Rule of 72: Investment will double in approximately {years:.1f} years at {r*100}% interest"

class FVAnnuityInput(BaseModel):
    pmt: float = Field(description="Payment amount per period")
    r: float = Field(description="Interest rate per period as decimal")
    n: float = Field(description="Number of periods")

class FVAnnuityTool(BaseTool):
    name: str = "fv_annuity"
    description: str = "Calculate future value of annuity using FV = PMT * [((1 + r)^n - 1) / r]"
    args_schema: Type[BaseModel] = FVAnnuityInput

    def _run(self, pmt: float, r: float, n: float) -> str:
        if r == 0:
            fv = pmt * n
        else:
            fv = pmt * (((1 + r) ** n - 1) / r)
        return f"Future Value of Annuity: ${fv:.2f} (Payment: ${pmt}, Rate: {r*100}%, Periods: {n})"

class PVAnnuityInput(BaseModel):
    pmt: float = Field(description="Payment amount per period")
    r: float = Field(description="Interest rate per period as decimal")
    n: float = Field(description="Number of periods")

class PVAnnuityTool(BaseTool):
    name: str = "pv_annuity"
    description: str = "Calculate present value of annuity using PV = PMT * [1 - (1 + r)^(-n)] / r"
    args_schema: Type[BaseModel] = PVAnnuityInput

    def _run(self, pmt: float, r: float, n: float) -> str:
        if r == 0:
            pv = pmt * n
        else:
            pv = pmt * (1 - (1 + r) ** (-n)) / r
        return f"Present Value of Annuity: ${pv:.2f} (Payment: ${pmt}, Rate: {r*100}%, Periods: {n})"

class NPERInput(BaseModel):
    pv: float = Field(description="Present value")
    fv: float = Field(description="Future value")
    r: float = Field(description="Interest rate per period as decimal")
    pmt: float = Field(description="Payment per period", default=0)

class NPERTool(BaseTool):
    name: str = "nper"
    description: str = "Calculate number of periods required for investment to grow from PV to FV"
    args_schema: Type[BaseModel] = NPERInput

    def _run(self, pv: float, fv: float, r: float, pmt: float = 0) -> str:
        import math
        if pmt == 0:
            # Simple compound interest: n = ln(FV/PV) / ln(1+r)
            periods = math.log(fv / pv) / math.log(1 + r)
        else:
            # With payments - more complex calculation
            if r == 0:
                periods = (fv - pv) / pmt
            else:
                periods = math.log((fv * r + pmt) / (pv * r + pmt)) / math.log(1 + r)
        
        return f"Number of Periods: {periods:.2f} (PV: ${pv}, FV: ${fv}, Rate: {r*100}%, Payment: ${pmt})"

class ExplainCalculationInput(BaseModel):
    calculation_type: str = Field(description="Type of calculation to explain")
    parameters: dict = Field(description="Parameters used in the calculation")

class ExplainCalculationTool(BaseTool):
    name: str = "explain_calculation"
    description: str = "Provide detailed explanation of financial calculation"
    args_schema: Type[BaseModel] = ExplainCalculationInput

    def _run(self, calculation_type: str, parameters: dict) -> str:
        explanations = {
            "future_value": "Future Value calculation uses compound interest: FV = PV × (1 + r)^n",
            "present_value": "Present Value discounts future money to today's value: PV = FV ÷ (1 + r)^n",
            "rule_of_72": "Rule of 72 estimates doubling time: Years ≈ 72 ÷ (interest rate %)",
            "fv_annuity": "Future Value of Annuity: FV = PMT × [((1 + r)^n - 1) ÷ r]",
            "pv_annuity": "Present Value of Annuity: PV = PMT × [1 - (1 + r)^(-n)] ÷ r",
            "nper": "Number of Periods: n = ln(FV/PV) ÷ ln(1 + r)"
        }
        
        explanation = explanations.get(calculation_type, f"Explanation for {calculation_type}")
        return f"{explanation}\nParameters used: {parameters}"

# Create tool instances
future_value = FutureValueTool()
present_value = PresentValueTool()
rule_of_72 = RuleOf72Tool()
fv_annuity = FVAnnuityTool()
pv_annuity = PVAnnuityTool()
nper = NPERTool()
explain_calculation = ExplainCalculationTool()