# ingest.py

import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_chroma import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
import chromadb

# --- Load Environment Variables ---
load_dotenv()

# --- Define Constants ---
PDF_URL = "https://arxiv.org/pdf/1706.03762.pdf"
COLLECTION_NAME = "transformer_docs"
CHROMA_HOST = "localhost"
CHROMA_PORT = 8001

def run_ingestion():
    """
    Connects to a ChromaDB server, clears any old data,
    and ingests a PDF into a collection.
    """
    try:
        # 1. Connect to the ChromaDB server
        print(f"--- Connecting to ChromaDB server at {CHROMA_HOST}:{CHROMA_PORT} ---")
        client = chromadb.HttpClient(host=CHROMA_HOST, port=CHROMA_PORT)
        print("Connection successful.")

        # 2. Clear out the old collection if it exists
        print(f"Checking for existing collection '{COLLECTION_NAME}'...")
        existing_collections = [c.name for c in client.list_collections()]
        if COLLECTION_NAME in existing_collections:
            print(f"Collection '{COLLECTION_NAME}' already exists. Deleting it.")
            client.delete_collection(name=COLLECTION_NAME)
            print("Collection deleted.")

        # 3. LOAD the document
        print(f"--- Loading Document from {PDF_URL} ---")
        loader = PyPDFLoader(PDF_URL)
        documents = loader.load()
        if not documents:
            print("Could not load document. Exiting.")
            return False
        print(f"Loaded {len(documents)} pages from the PDF.")

        # 4. SPLIT the document into chunks
        print("\n--- Splitting Document into Chunks ---")
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            add_start_index=True
        )
        chunks = text_splitter.split_documents(documents)
        print(f"Split the document into {len(chunks)} chunks.")

        # 5. EMBED and STORE in the ChromaDB Server
        print("\n--- Embedding Chunks and Storing in ChromaDB Server ---")
        embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")
        
        Chroma.from_documents(
            documents=chunks,
            embedding=embedding_model,
            collection_name=COLLECTION_NAME,
            client=client,
        )
        print("--- Ingestion Complete ---")
        print(f"Data stored in collection '{COLLECTION_NAME}' on ChromaDB server.")
        return True

    except Exception as e:
        print(f"\n--- An error occurred ---")
        print(f"Error: {e}")
        print("Please ensure the ChromaDB server is running in a separate terminal with the command:")
        print(f"chroma run --path ./chroma_server_db --port {CHROMA_PORT}")
        return False

if __name__ == "__main__":
    print("Starting ingestion process...")
    input(f"Please ensure your ChromaDB server is running, then press Enter to continue...")
    success = run_ingestion()
    if success:
        print("\n✅ Ingestion was successful!")
    else:
        print("\n❌ Ingestion failed. Please check the error messages above.")