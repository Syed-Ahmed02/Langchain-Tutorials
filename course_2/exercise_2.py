from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain_core.document_loaders import PyPDFLoader
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
text = '''RAG (retrieval augmented generation) is an advanced NLP model that combines retrieval mechanisms with generative capabilities. RAG aims to improve the accuracy and relevance of its outputs by grounding responses in precise, contextually appropriate data.'''

# Define a text splitter that splits on the '.' character
text_splitter = CharacterTextSplitter(
    separator=".",
    chunk_size=75,  
    chunk_overlap=10  
)

# Split the text using text_splitter
chunks = text_splitter.split_text(text)
print(chunks)
print([len(chunk) for chunk in chunks])


loader = PyPDFLoader("rag_paper.pdf")
document = loader.load()

# Define a text splitter that splits recursively through the character list
text_splitter = RecursiveCharacterTextSplitter(
    separators=['\n', '.', ' ', ''],
    chunk_size=75,  
    chunk_overlap=10  
)

# Split the document using text_splitter
chunks = text_splitter.split_documents(document)
print(chunks)
print([len(chunk.page_content) for chunk in chunks])


# Initialize the OpenAI embedding model
embedding_model = OpenAIEmbeddings(api_key="<OPENAI_API_TOKEN>", model='text-embedding-3-small')

# Create a Chroma vector store and embed the chunks
vector_store = Chroma.from_documents(
    documents=chunks,
    embedding = embedding_model
)