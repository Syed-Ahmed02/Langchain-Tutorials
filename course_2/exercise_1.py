# Import library
from langchain_community.document_loaders import PyPDFLoader, UnstructuredHTMLLoader 

# Create a document loader for rag_paper.pdf
loader = PyPDFLoader(file_path="rag_paper.pdf")

# Load the document
data = loader.load()
print(data[0])

# Create a document loader for unstructured HTML
loader = UnstructuredHTMLLoader(file_path="datacamp-blog.html")

# Load the document
data = loader.load()

# Print the first document's content
print(data[0].page_content)

# Print the first document's metadata
print(data[0].metadata)