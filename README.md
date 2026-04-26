              🚀 Text-to-SQL AI Assistant (RAG + LLM Powered)


📌 Overview
This project is an AI-powered Text-to-SQL + RAG system that converts natural language into SQL queries and retrieves results from a database using 
LangChain, Groq LLM, and Vector Database (RAG pipeline).
It also supports knowledge-based retrieval using embeddings for improved query understanding.

✨ Key Features
        Natural Language → SQL Query generation
        RAG-based context retrieval (VectorDB + Knowledge base)
        Groq LLM for fast inference
        SQLite database integration (enterprise.db)
        Modular pipeline (LLM + Chain + DB + RAG)
        Streamlit dashboard UI
        Scalable architecture for enterprise use cases


🧠 System Architecture
          User Query
             ↓
          Streamlit UI (app.py)
             ↓
          chain.py (Orchestration Layer)
             ↓
          RAG Engine (rag.py + vectordb + knowledge)
             ↓
          LLM Layer (llm.py - Groq)
             ↓
          SQL Generator / DB Query (db.py)
             ↓
          SQLite Database (enterprise.db)
             ↓
          Response Output

Live Demo: https://text-to-sql-app-assitant.streamlit.app/
          
🛠️ Tech Stack
      Python • Streamlit • LangChain • Groq LLM • SQLite • VectorDB • RAG Pipeline • Embeddings

📂 Project Structure
TEXT_TO_SQL_UPGRADE/
│
├── app.py              # Streamlit UI
├── chain.py            # Main orchestration logic
├── rag.py              # RAG pipeline logic
├── build_rag.py        # Builds vector database
├── llm.py              # Groq LLM integration
├── db.py               # Database connection & queries
├── dashboard.py        # Analytics/dashboard UI
│
├── knowledge/          # Knowledge base documents
├── vectordb/           # Vector embeddings storage
├── enterprise.db       # SQLite database
│
├── requirements.txt
├── .env
└── .gitignore
