import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(model="gpt-4o-mini", temperature=0,)