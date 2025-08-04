
import os
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from tools.formulas import (
    future_value,
    present_value,
    rule_of_72,
    fv_annuity, 
    pv_annuity,
    explain_calculation,
    nper,   
)
from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=GEMINI_API_KEY
    
)

llm_with_tools = llm.bind_tools([future_value, present_value, rule_of_72, fv_annuity, pv_annuity, explain_calculation, nper])