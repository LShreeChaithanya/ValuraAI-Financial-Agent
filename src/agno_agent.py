from agno.agent import Agent
from prompts import Financial_planner
from dotenv import load_dotenv
load_dotenv()
from tools.formulas import (
    future_value,
    present_value,
    rule_of_72,
    fv_annuity, 
    pv_annuity,
    explain_calculation,
    nper,   
)
from agno.models.google import Gemini


from agno.agent import Agent

agent = Agent(model=Gemini(id="gemini-2.0-flash"),
              tools=[future_value, present_value, rule_of_72, fv_annuity, pv_annuity, explain_calculation, nper],
              
              description=Financial_planner,
              add_history_to_messages=True,
              show_tool_calls = True,
            

              )
agent.print_response(" Calculate the future value of an investment of $1000 at an interest rate of 5% for 10 years.")