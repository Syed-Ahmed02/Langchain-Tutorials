from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_community.document_loaders import PythonLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter,Language
# Create a document loader for README.md and load it
# loader = UnstructuredMarkdownLoader("README.md")

# markdown_data = loader.load()
# print(markdown_data[0])

loader = PythonLoader("exercise_1.py")

python_data = loader.load()
print(python_data[0])

# Create a Python-aware recursive character splitter
python_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=300, chunk_overlap=100
)

# Split the Python content into chunks
chunks = python_splitter.split_documents(python_data)

for i, chunk in enumerate(chunks[:3]):
    print(f"Chunk {i+1}:\n{chunk.page_content}\n")