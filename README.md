# 📦 Meridian Supply Chain RAG Assistant

An intelligent, full-stack Retrieval-Augmented Generation (RAG) system built to analyze and answer questions based on Meridian Supply Chain and Procurement policy documents.

### 🌐 Live Demo
**Test the application live on the cloud:** [Live Streamlit App](https://supplychain-rag-swapnilpatil.streamlit.app/)

---

## 🏗️ System Architecture

This project is built with a decoupled architecture, demonstrating both a modern frontend UI and a professional REST API backend.

* **Frontend (UI):** Built with **Streamlit** (`app.py`), featuring a premium dark-mode aesthetic, custom CSS styling, and intuitive file uploading.
* **Backend (API):** Built with **FastAPI** (`api/main.py`), exposing modular REST endpoints (`/ingest`, `/ask`, `/stats`) for programmatic access.
* **Orchestration:** Powered by **Langchain**, which seamlessly connects the document loaders, vector database, and language models.

## 🧠 AI Models Used

* **Language Model (LLM):** `Meta Llama 3.3 (70B)` via the Groq API. Chosen for its state-of-the-art reasoning capabilities and lightning-fast inference speed.
* **Embedding Model:** `FastEmbed (BAAI/bge-small-en-v1.5)`. A lightweight, highly efficient local embedding model that runs directly on the CPU without requiring paid APIs.
* **Vector Database:** `ChromaDB`. Used to persist and query the mathematical vector embeddings of the PDF documents locally.

---

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/swapnilpatil3/supplychain-rag.git
cd supplychain-rag

### 2. Set up the Virtual Environment
python -m venv venv
venv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Set Environment Variables
Create a `.env` file in the root directory and add your Groq API Key:
GROQ_API_KEY=gsk_your_api_key_here

### 5. Start the Application
To run the Streamlit Web UI:
streamlit run app.py

To run the FastAPI Backend (Optional):
uvicorn api.main:app --reload
