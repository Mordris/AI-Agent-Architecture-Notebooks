# Production-Ready FastAPI Server for an AI Agent

This project represents the capstone for Module 3 of the MentorAI Masterclass, focusing on **Productionization**. We take the advanced, multi-tool, memory-equipped AI agent developed in the previous modules and build a robust, production-grade infrastructure around it.

This is not a notebook; it is a complete, runnable web application built with modern best practices.

## Core Features and Architecture

- **FastAPI Web Server:** A high-performance, asynchronous web server (`main.py`) provides the API endpoints for interacting with the agent.
- **Decoupled Agent Logic:** All agent and tool definitions are cleanly separated into `agent.py`, promoting a modular and maintainable codebase.
- **Client-Server Vector Store:** The application connects to a standalone ChromaDB server process (`chroma run...`), demonstrating a production-ready, decoupled database architecture.
- **Data Ingestion Script:** A dedicated `ingest.py` script handles the population of the ChromaDB vector store.
- **Stateful, Multi-User Memory:** The server manages conversation histories on a per-user basis, ensuring that conversations are isolated and stateful.
- **Real-Time Streaming with `astream_events`:** The main `/chat/stream` endpoint uses LangChain's low-level `astream_events` method to provide a true, low-latency, token-by-token streaming experience similar to platforms like ChatGPT.
- **Full Observability with LangSmith:** The entire application is instrumented for LangSmith, providing deep, visual traces of every agent execution for debugging, optimization, and monitoring.

## How to Run This Project

1.  **Prerequisites:**

    - Ensure you have a running ChromaDB server instance.
      ```bash
      # In a separate terminal
      chroma run --path ./chroma_server_db --port 8001
      ```
    - Make sure your `.env` file is populated with the necessary API keys (`OPENAI_API_KEY`, `LANGCHAIN_API_KEY`, etc.).

2.  **Set up the environment:**

    ```bash
    # (Inside this project's directory)
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3.  **Run the Data Ingestion:**

    - You only need to do this once.

    ```bash
    python ingest.py
    ```

4.  **Run the FastAPI Server:**

    ```bash
    uvicorn main:app --reload
    ```

5.  **Test the API:**
    - You can use the automatically generated docs at `http://127.0.0.1:8000/docs`.
    - Or use a `curl` command to test the streaming endpoint:
    ```bash
    curl -N -X 'POST' \
      'http://127.0.0.1:8000/chat/stream' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "user_id": "test_user_123",
      "message": "What is the attention mechanism?"
    }'
    ```
