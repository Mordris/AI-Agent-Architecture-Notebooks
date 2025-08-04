# Production-Ready FastAPI Server for an AI Agent

<<<<<<< HEAD
This project is the capstone of the "Productionization" module. It takes the advanced, multi-tool, memory-equipped AI agent developed in the course and builds a robust, production-grade infrastructure around it.
=======
This project represents the capstone for Module 3, focusing on **Productionization**. We take the advanced, multi-tool, memory-equipped AI agent developed in the previous modules and build a robust, production-grade infrastructure around it.
>>>>>>> c455c1f41d9b88431d375e19a02ce8f5d101bd33

This is a complete, runnable, containerized web application that demonstrates modern best practices for deploying AI systems.

## Core Features & Architecture

- **FastAPI Web Server:** A high-performance, asynchronous web server (`main.py`) provides the API endpoints for interacting with the agent.
- **Decoupled Agent Logic:** All agent and tool definitions are cleanly separated into `agent.py`. The architecture uses **lazy initialization** for database connections to ensure robust, dependency-aware startup in a multi-service environment.
- **Client-Server Vector Store:** The application connects to a standalone **ChromaDB server** process, demonstrating a production-ready, decoupled microservices architecture.
- **Persistent Data Volumes:** Docker volumes are used to ensure that the ChromaDB vector store data persists across container restarts, preventing data loss.
- **Stateful, Multi-User Memory:** The server manages conversation histories on a per-user basis, ensuring that conversations are isolated and stateful.
- **Real-Time Streaming with `astream_events`:** The main `/chat/stream` endpoint uses LangChain's low-level `astream_events` method to provide a true, low-latency, token-by-token streaming experience similar to platforms like ChatGPT.
- **Full Observability with LangSmith:** The entire application is instrumented for LangSmith, providing deep, visual traces of every agent execution for debugging, optimization, and monitoring.

## How to Run This Project

### 1. Prerequisites

- You must have **Docker** and **Docker Compose** installed and running on your machine.
- Create a `.env` file in this directory and populate it with your API keys. At a minimum, you need `OPENAI_API_KEY`. For full observability, also include `LANGCHAIN_API_KEY`, `LANGCHAIN_PROJECT`, etc.

### 2. Run with Docker Compose (Recommended)

This is the simplest and most reliable way to run the entire application.

```bash
# From this directory (8_FastAPI_Agent_Server/)

# Step 1: Build and start the services in the background (-d)
docker-compose up --build -d

# Step 2: Run the one-time data ingestion process
# This command executes the ingest.py script inside the running 'api' container
docker-compose exec api python ingest.py

# Step 3: View the application logs
docker-compose logs -f
```

### 3. Test the API

Your agent is now running and accessible at `http://localhost:8000`.

- **Interactive Docs:** Visit `http://localhost:8000/docs` in your browser.
- **Streaming Endpoint:** Use a `curl` command to test the streaming endpoint from your terminal.

  ```bash
  curl -N -X 'POST' \
    'http://localhost:8000/chat/stream' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "user_id": "test_user_123",
    "message": "What is the attention mechanism?"
  }'
  ```

### 4. Stopping the Application

```bash
# Stop and remove the containers and the network
docker-compose down

# To also remove the persistent data volume, add the -v flag
docker-compose down -v
```
