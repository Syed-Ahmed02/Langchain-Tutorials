from langchain_community.retrievers import BM25Retriever
from langchain_core.runnables import RunnablePassthrough
chunks = [
    "RAG stands for Retrieval Augmented Generation.",
    "Graph Retrieval Augmented Generation uses graphs to store and utilize relationships between documents in the retrieval process.",
    "There are different types of RAG architectures; for example, Graph RAG."
]

# Initialize the BM25 retriever
bm25_retriever = BM25Retriever.from_texts(chunks,k=3)

# Invoke the retriever
results = bm25_retriever.invoke("Graph RAG")

# Extract the page content from the first result
print("Most Relevant Document:")
print(results[0].page_content)

# Create a BM25 retriever from chunks
retriever = BM25Retriever.from_documents(chunks,k=5)

# # Create the LCEL retrieval chain
# chain = ({"context": retriever, "question": RunnablePassthrough()}
#          | prompt
#          | llm
#          | StrOutputParser()
# )

# print(chain.invoke("What are knowledge-intensive tasks?"))