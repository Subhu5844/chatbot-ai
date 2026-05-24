from langchain.prompts import ChatPromptTemplate

def get_chat_prompt():
    return ChatPromptTemplate.from_template(
        """
        You are a helpful AI assistant.

        Conversation History:
        {history}

        User: {input}
        AI:
        """
    )
