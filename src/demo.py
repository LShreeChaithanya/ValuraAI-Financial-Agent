from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

@tool
def add(a: int, b: int) -> int:
    """Adds a and b.

    Args:
        a: first int
        b: second int
    """
    return a + b


llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    max_tokens=1000,
    temperature=0.2,
    api_key=GEMINI_API_KEY,
)

llm_with_tools = llm.bind_tools([add], tool_choice="required")

query = "What is 11 + 11?"

messages = [HumanMessage(query)]
ai_msg = llm_with_tools.invoke(messages)
messages.append(ai_msg)

tool_call = ai_msg.tool_calls[0]
tool_output = add.invoke(tool_call["args"])

# This append the result from our tool to the model
messages.append(ToolMessage(tool_output, tool_call_id=tool_call["id"]))

llm_with_tools.invoke(messages).content