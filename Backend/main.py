import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def query_rag_system(question: str):
    if not question or not question.strip():
        return "Error: Please provide a valid question."

    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return (
            "Error: GOOGLE_API_KEY environment variable is not set. "
            "Please add it before running the assistant."
        )

    # 1. Define persist directory for ChromaDB
    persist_directory = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../Models/chroma_db')
    )

    if not os.path.exists(persist_directory):
        return "Error: Vector database not found. Please run document_loader.py first!"

    # 2. Initialize local embeddings to load the vector store
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_store = Chroma(
        persist_directory=persist_directory, 
        embedding_function=embeddings
    )

    # 3. Create a retriever from the vector store
    retriever = vector_store.as_retriever(
        search_type="similarity", 
        search_kwargs={"k": 3}
    )

    # 4. Initialize the Gemini LLM for text generation
    model_name = os.getenv("GOOGLE_MODEL", "gemini-3.8-flash")
    llm = ChatGoogleGenerativeAI(model=model_name, temperature=0.2)

    # 5. Define the prompt template for Egyptian business/legal advisory
    template = """You are an expert legal, regulatory, and business advisor assistant for entrepreneurs in Egypt. 
Use the following retrieved context from Egyptian commercial laws, MSME regulations, and venture capital directories to answer the user's question accurately. 
Always cite the specific law, decree, or funding source mentioned in the context. 
If the answer cannot be found in the context, clearly state that you do not have that official regulation on record.

Context:
{context}

User Question: {question}

Answer:"""
    
    prompt = ChatPromptTemplate.from_template(template)

    # 6. Build the RAG chain using LangChain Expression Language (LCEL)
    def format_docs(docs):
      return '\n\n'.join(doc.page_content for doc in docs)

    # FIXED: Changed "pass_through" to "question" to match the prompt template
    chain = (
        {
            'context': retriever | format_docs,
            'question': RunnablePassthrough(),
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    # 7. Execute the chain with the user's question
    # Note: LCEL passes the question into prompt via the dictionary key mapping
    response = chain.invoke(question)
    return response

if __name__ == "__main__":
    # Test query
    test_question = "How do I register an LLC or company via GAFI, and what are the steps?"
    print(f"\n--- Testing Query: '{test_question}' ---\n")
    answer = query_rag_system(test_question)
    print(answer)