from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from gemini import llm_with_tools
from prompts import Financial_planner

from langchain_core.messages import HumanMessage, AIMessage
from typing import Any, List, Union

def format_chat_history(history: List[Any]) :
    formatted = []

    for msg in history:
        # Safe extraction of role and content
        role = getattr(msg, "role", msg.get("role") if isinstance(msg, dict) else None)
        content = getattr(msg, "content", msg.get("content") if isinstance(msg, dict) else None)

        # Skip if content is None or empty
        if not content or not role:
            continue

        if role == "user":
            formatted.append(HumanMessage(content=content))
        elif role == "assistant":
            formatted.append(AIMessage(content=content))

    return formatted

def build_agent(user_input: str, chat_history):
    """messages = [SystemMessage(content=Financial_planner)] + MessagesPlaceholder(variable_name="chat_history") + [HumanMessage(content=user_input)]
    prompt = ChatPromptTemplate.from_messages(messages)"""
    prompt = ChatPromptTemplate.from_messages([
        ("system", Financial_planner),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}")
    ])
    return prompt | llm_with_tools | StrOutputParser()

def ai_invoke(message: str, chat_history: list) -> str:
    formatted_history = format_chat_history(chat_history)
    agent = build_agent(message, formatted_history)
    return agent.invoke({"input": message, "chat_history": formatted_history})
