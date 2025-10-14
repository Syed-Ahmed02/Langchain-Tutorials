import tiktoken 
from langchain_text_splitters import TokenTextSplitter  
from langchain_openai import OpenAIEmbeddings
from langchain_experimental.text_splitter import SemanticChunker

# Get the encoding for gpt-4o-mini
encoding = tiktoken.encoding_for_model("gpt-4o-mini")

# Create a token text splitter
token_splitter = TokenTextSplitter(encoding_name=encoding.name, chunk_size=100, chunk_overlap=10)

# Split the PDF into chunks
chunks = token_splitter.split_documents("resume.pdf")

for i, chunk in enumerate(chunks[:3]):
    print(f"Chunk {i+1}:\nNo. tokens: {len(encoding.encode(chunk.page_content))}\n{chunk}\n")
    
# Instantiate an OpenAI embeddings model
embedding_model = OpenAIEmbeddings(api_key="<OPENAI_API_TOKEN>", model='text-embedding-3-small')

# Create the semantic text splitter with desired parameters
semantic_splitter = SemanticChunker(
    embeddings=embedding_model, breakpoint_threshold_type="gradient", breakpoint_threshold_amount=0.8
)

# Split the document
chunks = semantic_splitter.split_documents("resume.pdf")
print(chunks[0])