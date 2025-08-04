# AI Agent Architecture: From Notebooks to Production

Welcome to my portfolio of hands-on labs and projects, chronicling my journey to master the architecture of modern AI applications. This repository documents the end-to-end process of building a production-grade system, progressing from fundamental concepts to a fully deployable, observable, and intelligent AI agent.

Each entry serves as a practical demonstration of a core concept, complete with code, analysis, and key learnings.

## Core Competencies Demonstrated

This repository showcases a comprehensive skill set in modern AI engineering:

- **LLM Interaction & Selection:** Comparing and utilizing proprietary APIs vs. self-hosted open-source models.
- **Vector Database Architecture:** Benchmarking and implementing different vector store strategies.
- **Advanced RAG Pipelines:** Building and rigorously evaluating state-of-the-art Retrieval Augmented Generation systems.
- **Agentic Design & Orchestration:** Engineering autonomous agents with LangChain that can reason, use multiple tools, and maintain conversational memory.
- **Productionization & MLOps:**
  - Building robust, high-performance APIs with **FastAPI**.
  - Implementing real-time, low-latency streaming with **Server-Sent Events (SSE)**.
  - Ensuring deep system visibility and debugging with **LangSmith**.
  - Containerizing a multi-service application with **Docker and Docker Compose** for reproducible deployment.
- **AI Evaluation:** Creating automated evaluation suites using the **LLM-as-a-Judge** pattern to programmatically measure agent quality.

---

## Projects & Notebooks

### Module 0: The Modern AI Stack

- **1. [`1_Proprietary_vs_OpenSource_LLM_Interaction.ipynb`](./1_Proprietary_vs_OpenSource_LLM_Interaction.ipynb)**: A practical comparison of managed LLM APIs vs. a locally-hosted open-source model.
- **2. [`2_Vector_Database_Benchmark_FAISS_ChromaDB.ipynb`](./2_Vector_Database_Benchmark_FAISS_ChromaDB.ipynb)**: An experimental benchmark of in-process vs. client-server vector databases.
- **3. [`3_langchain_intro_example.ipynb`](./3_langchain_intro_example.ipynb)**: The "Hello, World!" of orchestration, introducing the core concepts of LangChain.

### Module 1: Deep Dive into RAG

- **4. [`4_advanced_rag_retrieval_strategies.ipynb`](./4_advanced_rag_retrieval_strategies.ipynb)**: A comprehensive deep dive into building and evaluating a production-grade RAG pipeline.

### Module 2: Mastering Agentic Architecture

- **5. [`5_Manual_ReAct_Loop.ipynb`](./5_Manual_ReAct_Loop.ipynb)**: A first-principles lab building an agent from scratch to understand the core ReAct logic loop.
- **6. [`6_The_Evolution_of_LangChain_Agents.ipynb`](./6_The_Evolution_of_LangChain_Agents.ipynb)**: A comparative analysis of classic vs. modern tool-calling agent architectures.
- **7. [`7_Agent_Memory_and_Routing.ipynb`](./7_Agent_Memory_and_Routing.ipynb)**: A capstone lab building a single agent that can intelligently route between multiple tools and maintain conversational memory.

### Module 3 & 4: Productionization & Evaluation

- **8. [`8_FastAPI_Agent_Server/`](./8_FastAPI_Agent_Server/)**: **(Project)** A complete, containerized FastAPI server for our AI agent. This standalone application features a decoupled microservices architecture, persistent data volumes, stateful multi-user memory, true token-by-token streaming, and full observability with LangSmith.
- **9. [`9_Agent_Evaluation_Suite.ipynb`](./9_Agent_Evaluation_Suite.ipynb)**: A hands-on lab that builds a complete, automated evaluation framework for an AI agent using the powerful "LLM-as-a-Judge" pattern.

---

## How to Use This Repository

- **Notebooks (1-7, 9):** These are self-contained Jupyter/Colab notebooks. They can be run individually.
- **Projects (8):** The FastAPI Server is a standalone application. Please see the detailed `README.md` file inside that directory for specific setup and run instructions.

**General Setup:**

```bash
git clone https://github.com/[Your-GitHub-Username]/AI-Agent-Architecture-Notebooks.git
cd AI-Agent-Architecture-Notebooks

# It is highly recommended to use a virtual environment
python -m venv venv
source venv/bin/activate
```

**Note:** All projects and notebooks require API keys for services like OpenAI and LangSmith. Please use a `.env` file or set environment variables as needed.
