from langchain_openai import ChatOpenAI
from app.config import OPENAI_API_KEY

def get_llm():
    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.7,
        api_key=OPENAI_API_KEY
    )