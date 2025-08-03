# AI Agent Architecture: From Notebooks to Production

Welcome to my portfolio of hands-on labs, notebooks, and projects, chronicling my journey through the "MentorAI Masterclass" curriculum. This repository documents the end-to-end process of building a production-grade AI application, progressing from fundamental concepts to a fully deployable, observable, and intelligent AI agent.

Each entry serves as a practical demonstration of a core concept, complete with code, analysis, and key learnings.

## Core Competencies Demonstrated

This repository showcases a comprehensive skill set in modern AI engineering:

- **LLM Interaction & Selection:** Comparing and utilizing proprietary APIs (OpenAI, Anthropic) vs. self-hosted open-source models (Llama 3).
- **Vector Database Architecture:** Benchmarking and implementing different vector store strategies (in-process vs. client-server).
- **Advanced RAG Pipelines:** Building and rigorously evaluating state-of-the-art Retrieval Augmented Generation systems to ensure factual accuracy.
- **Agentic Design & Orchestration:** Engineering autonomous agents with LangChain that can reason, use multiple tools, and maintain conversational memory.
- **Productionization & MLOps:**
  - Building robust, high-performance APIs with **FastAPI**.
  - Implementing real-time, low-latency streaming with **Server-Sent Events (SSE)**.
  - Ensuring deep system visibility and debugging with the **LangSmith** observability platform.
  - Preparing applications for deployment.

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

### Module 3: Productionizing the Chatbot

- **8. [`8_FastAPI_Agent_Server/`](./8_FastAPI_Agent_Server/)**: **(Project)** A complete, production-ready FastAPI server for our AI agent. This standalone application features a decoupled architecture, stateful multi-user memory, true token-by-token streaming, and full observability with LangSmith.

---

## How to Use This Repository

- **Notebooks (1-7):** These are self-contained Jupyter/Colab notebooks. They can be run individually. Please check the top of each notebook for specific library installation commands.
- **Projects (8+):** These are complete applications in their own directories. Each project has its own `README.md` file with detailed setup and run instructions.

**General Setup:**

```bash
git clone https://github.com/[Your-GitHub-Username]/AI-Agent-Architecture-Notebooks.git
cd AI-Agent-Architecture-Notebooks

# It is highly recommended to use a virtual environment
python -m venv venv
source venv/bin/activate
```

**Note:** All projects and notebooks require API keys for services like OpenAI, LangSmith, and Cohere. Please create a `.env` file in the appropriate project directory or set environment variables as needed.

---

## Next Steps: Future Modules

This repository is actively being updated. The final module will cover:

- **Module 3.4:** Containerizing our FastAPI Application with Docker.
- **Module 4:** Advanced AI Evaluation and The Future of Agents.
