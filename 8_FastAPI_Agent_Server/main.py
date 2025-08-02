# main.py

import uvicorn
import os
from fastapi import FastAPI
from pydantic import BaseModel
from langchain.memory import ConversationBufferWindowMemory
from langchain_core.messages import AIMessage, HumanMessage

# Set up your OpenAI API key
try:
    from dotenv import load_dotenv
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OpenAI API key is not set in the environment.")
    print("OpenAI API key loaded successfully.")
except Exception as e:
    print(f"Error: {e}")

# Import the agent executor from our agent.py file
from agent import agent_executor

# Initialize the FastAPI app
app = FastAPI(
    title="Auto-Support Agent API",
    description="The main API for the production-ready AI Auto-Support Agent.",
    version="0.1.0",
)

# In-memory storage for user chat histories.
# In a production app, this would be a database (e.g., Redis, PostgreSQL).
chat_histories = {}

# Define our data models
class ChatRequest(BaseModel):
    user_id: str
    message: str

class ChatResponse(BaseModel):
    agent_id: str
    response: str

# Define our API endpoints
@app.get("/health", summary="Health Check")
async def health_check():
    return {"status": "ok"}

@app.post("/chat", response_model=ChatResponse, summary="Process a Chat Message")
async def chat(request: ChatRequest) -> ChatResponse:
    print(f"Received request from user: {request.user_id}")
    print(f"Message: {request.message}")

    # Get or create the chat history for the user
    if request.user_id not in chat_histories:
        chat_histories[request.user_id] = ConversationBufferWindowMemory(
            k=5, return_messages=True
        )
    memory = chat_histories[request.user_id]

    # The agent's input now includes the message and the chat history
    agent_input = {
        "input": request.message,
        "chat_history": memory.chat_memory.messages
    }
    
    agent_response = await agent_executor.ainvoke(agent_input)

    final_response = agent_response["output"]

    # Save the interaction to memory
    memory.save_context({"input": request.message}, {"output": final_response})

    return ChatResponse(agent_id="auto_support_agent_v1.0", response=final_response)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)