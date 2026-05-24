from langchain.chains import LLMChain
from app.llm import get_llm
from app.prompt import get_chat_prompt
from app.memory import get_memory

class ChatBot:
    def __init__(self):
        self.llm = get_llm()
        self.prompt = get_chat_prompt()
        self.memory = get_memory()

        self.chain = LLMChain(
            llm=self.llm,
            prompt=self.prompt,
            memory=self.memory
        )

    def chat(self, user_input: str):
        return self.chain.predict(input=user_input)