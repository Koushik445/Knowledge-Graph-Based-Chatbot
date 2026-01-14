# Graph-RAG Chatbot using Neo4j and Local LLM

This project implements an end-to-end Graph-RAG (Retrieval-Augmented Generation) chatbot that answers domain-specific questions using a Neo4j knowledge graph and a locally hosted Large Language Model (Mistral-7B). The system ensures high accuracy and zero hallucination by treating the graph database as the single source of truth.

---

## 🚀 Features

- Ontology-driven knowledge graph built using Neo4j
- Deterministic Cypher-based retrieval for accurate results
- Local Mistral-7B LLM (via llama.cpp) for grounded answer generation
- No external APIs or cloud dependencies
- Streamlit-based interactive chat interface
- Explainable and reliable question answering

---

## 🧠 System Architecture

User
↓
Streamlit Chat UI
↓
Intent Parsing & Query Routing
↓
Neo4j Knowledge Graph (Cypher Queries)
↓
Retrieved Context
↓
Local Mistral-7B LLM
↓
Grounded Natural Language Answer

---

## 🛠️ Tech Stack

- **Python 3.11**
- **Neo4j (Community Edition)**
- **Cypher**
- **Mistral-7B Instruct (GGUF)**
- **llama-cpp-python**
- **Streamlit**
- **Pandas**

---

## 📂 Project Structure

graph_rag_chatbot/
│
├── data/
│ └── ideas_dataset.csv
│
├── graph/
│ ├── ingest.py
│ ├── neo4j_connection.py
│ └── schema.cypher
│
├── rag/
│ ├── intent_parser.py
│ ├── router.py
│ ├── retriever.py
│ └── answer_generator.py
│
├── llm/
│ ├── load_model.py
│ └── prompt_templates.py
│
├── models/
│ └── mistral-7b-instruct.gguf
│
├── app.py
└── requirements.txt

---

## ▶️ How to Run

### 1. Activate virtual environment
```bash
graphrag311\Scripts\activate
2. Start Neo4j
Ensure Neo4j is running locally at:
bolt://localhost:7687
3. Run the Streamlit app
streamlit run app.py


##🧪 Example Questions

Which ideas use AI?

What initiatives address vegetation interference?

Which projects improve reliability?

Show ideas related to SCADA

##🎯 Key Design Principle

The LLM is used only for answer synthesis, while all factual information is retrieved deterministically from the Neo4j knowledge graph. This design prevents hallucinations and improves reliability.

##📌 Use Cases
Knowledge graph–based decision support
Enterprise innovation analysis
Explainable AI systems

Graph-RAG research and learning projects
