from llama_index.core import SQLDatabase
from llama_index.llms.openai import OpenAI
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


load_dotenv()

db_connection_string = os.getenv("DB_CONNECTION_STRING")

def generate_database():
    engine = create_engine(db_connection_string)
    llm = OpenAI(temperature=0.1, model="gpt-4.1-mini")