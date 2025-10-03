#document loaders
#https://python.langchain.com/docs/integrations/document_loaders/
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("resume_sept_9_2026.pdf")

data = loader.load()

print(data[0])

# from langchain_community.document_loaders.csv_loader import CSVLoader

# # Create a document loader for fifa_countries_audience.csv
# loader = CSVLoader("fifa_countries_audience.csv")

# # Load the document
# data = loader.load()
# print(data[0])


# from langchain_community.document_loaders import UnstructuredHTMLLoader

# # Create a document loader for unstructured HTML
# loader = UnstructuredHTMLLoader("white_house_executive_order_nov_2023.html")

# # Load the document
# data = loader.load()

# # Print the first document
# print(data[0])

# # Print the first document's metadata
# print(data[0].metadata)

# # Load the HTML document into memory
# loader = UnstructuredHTMLLoader("white_house_executive_order_nov_2023.html")
# data = loader.load()

# # Define variables
# chunk_size = 300
# chunk_overlap = 100

# # Split the HTML
# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=chunk_size,
#     chunk_overlap=chunk_overlap,
#     separators='.')

# docs = splitter.split_documents(data)
# print(docs)