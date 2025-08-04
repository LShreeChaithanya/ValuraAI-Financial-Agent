from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, ToolMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from tools.formulas import (
    future_value,
    present_value,
    rule_of_72,
    fv_annuity, 
    pv_annuity,
    explain_calculation,
    nper,   
)
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
    return prompt | llm_with_tools

"""def ai_invoke(message: str, chat_history: list) -> str:
    formatted_history = format_chat_history(chat_history)
    agent = build_agent(message, formatted_history)
    return agent.invoke({"input": message, "chat_history": formatted_history})"""

"""def ai_invoke(message: str, chat_history: list):
    formatted_history = format_chat_history(chat_history)
    
    # Create the prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", Financial_planner),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}")
    ])
    
    # Create messages for the first call
    messages = prompt.format_messages(
        input=message,
        chat_history=formatted_history
    )
    
    # First LLM call - DO NOT use StrOutputParser here
    ai_msg = llm_with_tools.invoke(messages)
    
    # Check if AI message has tool calls
    if hasattr(ai_msg, 'tool_calls') and ai_msg.tool_calls:
        tool_messages = []
        
        # Execute each tool call
        for tool_call in ai_msg.tool_calls:
            tool_name = tool_call["name"]
            tool_args = tool_call["args"]
            tool_id = tool_call["id"]
            
            # Map tool names to actual functions
            tool_fn = {
                "future_value": future_value,
                "present_value": present_value,
                "rule_of_72": rule_of_72,
                "fv_annuity": fv_annuity,
                "pv_annuity": pv_annuity,
                "explain_calculation": explain_calculation,
                "nper": nper,
            }.get(tool_name)
            
            if tool_fn:
                try:
                    # Call the tool function directly with arguments
                    # NOT tool_fn.invoke(tool_args) but tool_fn(**tool_args)
                    tool_result = tool_fn(**tool_args)
                    tool_messages.append(
                        ToolMessage(
                            content=str(tool_result), 
                            tool_call_id=tool_id
                        )
                    )
                except Exception as e:
                    print(f"Tool execution error: {e}")
                    tool_messages.append(
                        ToolMessage(
                            content=f"Error executing {tool_name}: {e}", 
                            tool_call_id=tool_id
                        )
                    )
        
        # Create the message sequence for final response
        messages_with_tools = formatted_history + [
            HumanMessage(content=message),
            ai_msg
        ] + tool_messages
        
        # Get final response from LLM with tool results
        final_response = llm_with_tools.invoke(messages_with_tools)
        
        return final_response.content if hasattr(final_response, 'content') else str(final_response)
    
    # If no tool calls, return the original response
    return ai_msg.content if hasattr(ai_msg, 'content') else str(ai_msg)"""

def ai_invoke(message: str, chat_history: list):
    formatted_history = format_chat_history(chat_history)
    
    # Create the prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", Financial_planner),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}")
    ])
    
    # Create messages for the first call
    messages = prompt.format_messages(
        input=message,
        chat_history=formatted_history
    )
    
    # First LLM call
    ai_msg = llm_with_tools.invoke(messages)
    
    # Check if AI message has tool calls
    if hasattr(ai_msg, 'tool_calls') and ai_msg.tool_calls:
        tool_messages = []
        
        # Execute each tool call
        for tool_call in ai_msg.tool_calls:
            tool_name = tool_call["name"]
            tool_args = tool_call["args"]  # Use original args - no mapping needed!
            tool_id = tool_call["id"]
            
            print(f"Tool {tool_name} called with args: {tool_args}")
            
            # Get tool function
            tool_fn = {
                "future_value": future_value,
                "present_value": present_value,
                "rule_of_72": rule_of_72,
                "fv_annuity": fv_annuity,
                "pv_annuity": pv_annuity,
                "explain_calculation": explain_calculation,
                "nper": nper,
            }.get(tool_name)
            
            if tool_fn:
                try:
                    # Use original arguments directly - no mapping!
                    tool_result = tool_fn.invoke(tool_args)
                    tool_messages.append(
                        ToolMessage(
                            content=str(tool_result), 
                            tool_call_id=tool_id
                        )
                    )
                    print(f"Tool {tool_name} executed successfully: {tool_result}")
                    
                except Exception as e:
                    error_msg = f"Error executing {tool_name}: {e}. Args: {tool_args}"
                    print(error_msg)
                    tool_messages.append(
                        ToolMessage(
                            content=error_msg, 
                            tool_call_id=tool_id
                        )
                    )
            else:
                error_msg = f"Tool {tool_name} not found in tool mapping"
                print(error_msg)
                tool_messages.append(
                    ToolMessage(
                        content=error_msg, 
                        tool_call_id=tool_id
                    )
                )
        
        # Create the message sequence for final response
        messages_with_tools = formatted_history + [
            HumanMessage(content=message),
            ai_msg
        ] + tool_messages
        
        # Get final response from LLM with tool results
        final_response = llm_with_tools.invoke(messages_with_tools)
        
        return final_response.content if hasattr(final_response, 'content') else str(final_response)
    
    # If no tool calls, return the original response
    return ai_msg.content if hasattr(ai_msg, 'content') else str(ai_msg)