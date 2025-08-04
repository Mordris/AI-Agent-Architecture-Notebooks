# agent.py

from datetime import datetime
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain.agents import tool, create_openai_tools_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import chromadb

# --- 1. Define the Tools ---
@tool
def get_current_time(tool_input: str = "") -> str:
    """
    Returns the current date and time as a string.
    Use this tool for any questions about the current time.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@tool
def get_knowledge_from_library(query: str) -> str:
    """
    Your primary tool. Use this to find information to answer a user's question.
    This tool searches a library of documents about the Transformer architecture
    and attention mechanisms. Use it for any questions about these topics.
    """
    # --- LAZY INITIALIZATION ---
    # The connection to ChromaDB is now made ONLY when this tool is called.
    print("--- Connecting to ChromaDB inside the tool ---")
    client = chromadb.HttpClient(host="chroma", port=8000)
    embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")
    vector_store = Chroma(
        client=client,
        collection_name="transformer_docs",
        embedding_function=embedding_model,
    )
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    
    print(f"--- Searching for: {query} ---")
    docs = retriever.invoke(query)
    return "\n---\n".join([doc.page_content for doc in docs])

tools = [get_current_time, get_knowledge_from_library]

# --- 2. Create the Agent ---
llm = ChatOpenAI(model="gpt-4o", temperature=0)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="chat_history", optional=True),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

agent = create_openai_tools_agent(llm, tools, prompt)

# --- 3. Create the Agent Executor ---
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True
)