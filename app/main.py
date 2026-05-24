from fastapi import FastAPI
from app.chains.chat_chain import ChatBot
from app.schemas.chat import ChatRequest, ChatResponse

app = FastAPI()

chatbot = ChatBot()

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    reply = chatbot.chat(request.message)
    return ChatResponse(response=reply)