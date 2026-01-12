import os

from llama_index.core.llms import MessageRole
from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.core.agent.workflow import FunctionAgent

from fastapi.responses import Response
from fastapi import APIRouter, HTTPException, Request, status

from app.classes.chat_data import _ChatData
from app.engine.index import get_agent

model = os.getenv("MODEL")
environment = os.getenv("ENVIRONMENT", "dev")

chat_router = r = APIRouter()

@r.post("")
async def chat(
    data: _ChatData
):
    
    if len(data.messages) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No messages provided.",
        )
        
    lastMessage = data.messages.pop()
    if lastMessage.role != MessageRole.USER:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Last message must be from user.",
        )
        
    messages = [ChatMessage(role=m.role, content=m.content) for m in data.messages]
    
    print("prompt: \n", lastMessage)
    print("----------------------------------")

    print("Fetching the agent...")
    
    agent = get_agent()
    
    print("Running the agent...")
    
    response = await agent.run(lastMessage.content, messages)
    
    print()
    print("response:")
    print(str(response))
    print("----------------------------------")

    return Response(str(response))