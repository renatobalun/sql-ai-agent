import os
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.openai import OpenAI

from dotenv import load_dotenv
from app.engine.prompt import get_technical_support_system_prompt

load_dotenv()

openai_model = os.getenv("MODEL")
openai_llm = OpenAI(model=openai_model)

def get_agent():
    wordpress_tool = WordpressSpec().to_tool_list()
    dns_tool = DnsSpec().to_tool_list()
    fallback_to_human_tool = FallbackToHumanSpec().to_tool_list()
    
    tools = (wordpress_tool + dns_tool + fallback_to_human_tool)
    
    agent = FunctionAgent(
        tools=tools,
        llm=openai_llm,
        verbose=True,
        system_prompt=get_technical_support_system_prompt("English"),
        max_function_calls=1
    )
    
    return agent