# app/api/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from financial_agent import ai_invoke
from langchain_core.messages import AIMessage, HumanMessage

from typing import Dict, Any

app = FastAPI(title="Financial Advisor API")



    
class chat_history(BaseModel):
    role: str
    content: str

class ChatRequest_Response(BaseModel):
    message: str
    chat_history: list[chat_history]


    
@app.post("/chat", response_model=ChatRequest_Response)
async def chat(request: ChatRequest_Response):
    try:
        raw_history = [msg.model_dump() for msg in request.chat_history]
        response= ai_invoke(request.message, chat_history=request.chat_history)
        return ChatRequest_Response(message=response, chat_history=request.chat_history)
    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))