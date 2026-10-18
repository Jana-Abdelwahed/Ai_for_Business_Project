# 🇪🇬 Egypt Entrepreneurship & Legal RAG Assistant

An AI-powered Retrieval-Augmented Generation (RAG) assistant designed to help Egyptian entrepreneurs, founders, and investors navigate complex local regulations, company incorporation steps (GAFI), MSME laws, and venture capital funding directories.

Styled with an official **GAFI (General Authority for Investment and Free Zones)** inspired color palette (professional navy blue and gold accents).

---

## 🚀 Key Features

* **Official Regulations Support:** Query information on Egyptian Company Law (Law 159/1981), MSME Development Law (Law 152/2020), and GAFI registration procedures.
* **Venture Capital Directory:** Access structured data on Egyptian VCs, accelerators, and ticket sizes.
* **Hybrid Architecture:** Powered by **Google Gemini** for generation and a **Local HuggingFace embedding model (`all-MiniLM-L6-v2`)** for fast, reliable, and cost-free local vector embeddings.
* **ChromaDB Vector Store:** Efficiently retrieves contextually relevant legal clauses and funding details.
* **Custom Streamlit Frontend:** Clean, branded web interface featuring dark navy styling and golden highlights.

---

## 🛠️ Tech Stack

* **Orchestration & RAG:** LangChain (LCEL)
* **Vector Database:** ChromaDB
* **Embeddings:** HuggingFace (`sentence-transformers/all-MiniLM-L6-v2`)
* **LLM Generation:** Google Gemini (`gemini-3.8-flash`)
* **Frontend:** Streamlit with custom CSS theme

---

## 📁 Project Directory Structure

```text
Ai_for_Business_Project/
│
├── Backend/
│   ├── document_loader.py   # Processes markdown datasets and builds ChromaDB
│   └── main.py              # RAG query pipeline and LCEL chain logic
│
├── Frontend/
│   └── app.py               # Streamlit web interface with GAFI styling
│
├── Datasets/                # Raw markdown files (GAFI, laws, VC directories)
├── Models/
│   └── chroma_db/           # Persisted Chroma vector database
├── .env                     # Environment variables (API keys)
└── requirements.txt         # Project dependencies
---

⚙️ Installation & Setup
1. Clone the Repository
Bash
git clone [https://github.com/YOUR_USERNAME/Egypt_Business_RAG_Assistant.git](https://github.com/YOUR_USERNAME/Egypt_Business_RAG_Assistant.git)
cd Egypt_Business_RAG_Assistant
2. Create and Activate a Virtual Environment
Bash
python -m venv .venv
# On Windows (PowerShell):
.venv\Scripts\Activate.ps1
# On macOS/Linux:
source .venv/bin/activate
3. Install Dependencies
Bash
pip install -r requirements.txt
4. Configure Environment Variables
Create a .env file in the root directory of your project and add your Google Gemini API key:

Code snippet
GOOGLE_API_KEY="your_actual_google_gemini_api_key_here"
GOOGLE_MODEL="gemini-3.8-flash"

💡 Example Queries to Try
"What are the steps to register an LLC via GAFI?"

"What tax benefits are provided under MSME Law 152/2020?"

"Which venture capital firms in Egypt fund Pre-Seed fintech startups and what are their ticket sizes?"

📄 License
This project is open-source and developed for educational and entrepreneurial empowerment in Egypt.
