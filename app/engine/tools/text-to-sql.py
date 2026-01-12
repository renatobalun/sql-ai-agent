from sqlalchemy import create_engine
from llama_index.core.tools.tool_spec.base import BaseToolSpec
from llama_index.core import SQLDatabase
from llama_index.llms.openai import OpenAI


class TextToSQLSpec(BaseToolSpec):
    """Text to SQL Spec"""
    
    spec_functions = ["text_to_sql"]
    
    def text_to_sql(self, query:str):
        "A tool for converting natural language to SQL. When user asks a question this tool converts that question to SQL and contacts the database for that information."
        
        

