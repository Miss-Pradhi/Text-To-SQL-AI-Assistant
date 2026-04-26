              🚀 Text-to-SQL AI Assistant (RAG + LLM Powered)
This project is an AI-powered Text-to-SQL + RAG system that converts natural language into SQL queries and retrieves results from a database using LangChain, Groq LLM, and Vector Database (RAG pipeline).
It also supports knowledge-based retrieval using embeddings for improved query understanding.

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

✨ Key Features
        1) Natural Language → SQL Query generation
        2) RAG-based context retrieval (VectorDB + Knowledge base)
        3) Groq LLM for fast inference
        4) SQLite database integration (enterprise.db)
        5) Modular pipeline (LLM + Chain + DB + RAG)
        6) treamlit dashboard UI
        7) Scalable architecture for enterprise use cases
