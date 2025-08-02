# AI Agent Architecture Notebooks

Welcome to my collection of hands-on labs and notebooks, chronicling my journey through the "MentorAI Masterclass" curriculum. This repository serves as a practical portfolio of my work, progressing from the fundamental building blocks of modern AI to the advanced architecture of production-grade AI Agents.

The goal of this repository is to document the process of building a sophisticated AI chatbot, capable of advanced retrieval, tool use, and autonomous reasoning. Each notebook represents a core concept, complete with code, analysis, and key learnings.

## Core Concepts Covered

This repository explores the entire stack required for building modern AI applications:

- **LLM Interaction:** Comparing proprietary APIs (OpenAI, Anthropic) with self-hosted open-source models (Llama 3 via Ollama).
- **Vector Databases:** Benchmarking and understanding the trade-offs between in-process libraries (FAISS) and client-server databases (ChromaDB).
- **Orchestration Frameworks:** Using LangChain as a structured way to build chains and connect components.
- **Retrieval Augmented Generation (RAG):**
  - Building a complete data ingestion pipeline (Load, Split, Embed, Store).
  - Implementing advanced retrieval strategies like MMR and Re-ranking.
  - Developing a rigorous evaluation framework to compare retrieval methods objectively.
- **Agentic Architecture:** Designing and building autonomous agents that can reason, use tools, and manage memory.
- **Productionization:** Creating robust APIs (FastAPI), implementing streaming (SSE), ensuring observability (LangSmith), and containerizing for deployment (Docker).

---

## Notebooks in this Repository

### Module 0: The Modern AI Stack

- **1. [`1_Proprietary_vs_OpenSource_LLM_Interaction.ipynb`](./1_Proprietary_vs_OpenSource_LLM_Interaction.ipynb)**

  - A practical comparison of interacting with managed LLM APIs (OpenAI GPT-4o, Anthropic Claude 3) versus a locally-hosted open-source model (Llama 3) via Ollama.

- **2. [`2_Vector_Database_Benchmark_FAISS_ChromaDB.ipynb`](./2_Vector_Database_Benchmark_FAISS_ChromaDB.ipynb)**

  - An experimental benchmark comparing the performance and programming models of an in-process vector library (FAISS) and a persistent, client-server vector database (ChromaDB).

- **3. [`3_langchain_intro_example.ipynb`](./3_langchain_intro_example.ipynb)**
  - The "Hello, World!" of orchestration. This notebook introduces the core concepts of LangChain by building a simple `PromptTemplate | LLM | OutputParser` chain.

### Module 1: Deep Dive into RAG

- **4. [`4_advanced_rag_retrieval_strategies.ipynb`](./4_advanced_rag_retrieval_strategies.ipynb)**
  - A comprehensive deep dive into building and evaluating a production-grade RAG pipeline. This notebook covers data ingestion, implementing advanced retrieval strategies (MMR, custom heuristics, Cohere Re-ranker), and provides a full evaluation framework to compare their performance.

### Module 2: Mastering Agentic Architecture

- **5. [`5_Manual_ReAct_Loop.ipynb`](./5_Manual_ReAct_Loop.ipynb)**

  - A first-principles approach to understanding agents by building one from scratch. This lab manually implements the `Thought -> Action -> Observation` loop to reveal the core logic of agentic reasoning.

- **6. [`6_The_Evolution_of_LangChain_Agents.ipynb`](./6_The_Evolution_of_LangChain_Agents.ipynb)**

  - A comparative analysis of agent creation in LangChain. This notebook contrasts the classic `ReAct` agent with the modern, reliable **Tool Calling** approach, demonstrating the evolution toward more robust and production-ready agent designs.

- **7. [`7_Agent_Memory_and_Routing.ipynb`](./7_Agent_Memory_and_Routing.ipynb)**
  - The capstone lab for Module 2. This notebook builds a single agent that can intelligently route between multiple tools (RAG vs. a standard tool) and maintain conversational memory.

---

## How to Use

To run these notebooks, clone the repository and install the necessary dependencies.

```bash
git clone https://github.com/[Your-GitHub-Username]/AI-Agent-Architecture-Notebooks.git
cd AI-Agent-Architecture-Notebooks

# It is recommended to create a virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies (you may need to create a requirements.txt)
pip install openai anthropic ollama faiss-cpu chromadb pypdf beautifulsoup4 langchain langchain_openai langchain_community langchain_cohere matplotlib
```

**Note:** Most notebooks require API keys for services like OpenAI, HuggingFace and Cohere. Please add your keys to your environment variables or a `.env` file to run the code successfully.

---

## Coming Soon: Future Modules

This repository is actively being updated as I progress through the curriculum. Future modules will include:

- **Module 3:** Productionizing the Chatbot (FastAPI, Streaming, Observability with LangSmith, Docker).
- **Module 4:** Advanced Evaluation and The Future (Agent Evaluation, Multi-Agent Systems).
