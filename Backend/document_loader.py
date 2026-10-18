import os
from langchain_chroma import Chroma
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_vector_database():
  datasets_path = (
      os.path.abspath(os.path.join(os.path.dirname(__file__), '../Datasets'))
      if os.path.exists(
          os.path.abspath(os.path.join(os.path.dirname(__file__), '../Datasets'))
      )
      else './Datasets'
  )
  persist_directory = os.path.abspath(
      os.path.join(os.path.dirname(__file__), '../Models/chroma_db')
  )

  print(f'Loading markdown files from: {datasets_path}')

  loader = DirectoryLoader(
      datasets_path,
      glob='**/*.md',
      loader_cls=TextLoader,
      loader_kwargs={'encoding': 'utf-8'},
  )
  documents = loader.load()
  print(f'Loaded {len(documents)} raw document(s) successfully.')

  text_splitter = RecursiveCharacterTextSplitter(
      chunk_size=800, chunk_overlap=100
  )
  chunks = text_splitter.split_documents(documents)
  print(f'Split documents into {len(chunks)} chunks.')

  print('Initializing local embedding model (all-MiniLM-L6-v2)...')
  embeddings = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')

  print('Generating vector embeddings and saving to ChromaDB...')
  vector_store = Chroma.from_documents(
      documents=chunks,
      embedding=embeddings,
      persist_directory=persist_directory,
  )

  print(f'Vector database successfully created and saved at: {persist_directory}')
  return vector_store


if __name__ == '__main__':
  create_vector_database()