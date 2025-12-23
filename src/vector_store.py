from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
import os


class VectorStoreManager:
    
    def __init__(self, persist_directory="data/chroma_db"):  
        self.persist_directory = persist_directory
        self.vectorstore = None
        print("Loading embeddings model...")
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
            model_kwargs={'device': 'cpu'}
        )
        print("Model loaded successfully")
    
    def create_vectorstore(self, documents):  
        print(f"\nIndexing {len(documents)} documents...")
        
        # Convert to LangChain documents
        docs = []
        for doc in documents: 
            docs.append(Document(
                page_content=doc['content'],
                metadata={'source': doc['source'], 'type': doc['type']}
            ))
        
        print("Creating vector store ( may take 2-3 minutes)...")
        self.vectorstore = Chroma.from_documents(
            documents=docs,
            embedding=self.embeddings,
            persist_directory=self.persist_directory
        )
        
        print(f"Successfully indexed {len(docs)} documents")
        return self.vectorstore
    
    def load_vectorstore(self):
        if not os.path.exists(self.persist_directory):  
            print("No existing vector store found")
            return None
        
        print("Loading vector store...")
        self.vectorstore = Chroma(
            persist_directory=self.persist_directory,
            embedding_function=self.embeddings
        )
        print("Vector store loaded")
        return self.vectorstore
    
    def search(self, query, k=3): 
        if not self.vectorstore:
            print("Please create or load vector store first")
            return []
        
        return self.vectorstore.similarity_search(query, k=k)


if __name__ == "__main__":
    vs_manager = VectorStoreManager()
    
    if vs_manager.load_vectorstore():
        print("Using existing vector store")
    else:
        print("Creating new vector store...")
        from document_processor import ExcelProcessor
        processor = ExcelProcessor()
        documents = processor.process_all_files()
        vs_manager.create_vectorstore(documents)
    
    print("\n" + "="*50)
    print("Testing search functionality")
    print("="*50)
    
    test_queries = [
        "How many customers bought Laptop?",
        "What is the most expensive product?",
        "Who bought Phone?"
    ]
    
    for query in test_queries:
        print(f"\nQuery: {query}")
        results = vs_manager.search(query, k=2)
        print(f"Results found: {len(results)}")
        if results:
            print(f"Top result: {results[0].page_content[:100]}...")
