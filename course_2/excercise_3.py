from langchain_core.prompts import ChatPromptTemplate 
from langchain_openai import ChatOpenAI
import os

llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"), max_completion_tokens=20)	
prompt = """
Use the only the context provided to answer the following question. If you don't know the answer, reply that you are unsure.
Context: {context}
Question: {question}
"""

# Convert the string into a chat prompt template
prompt_template = ChatPromptTemplate.from_template(prompt)

# Create an LCEL chain to test the prompt
chain = prompt_template | llm

# Invoke the chain on the inputs provided
print(chain.invoke({"context": "DataCamp's RAG course was created by Meri Nova and James Chapman!", "question": "Who created DataCamp's RAG course?"}))

# Convert the vector store into a retriever
# retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k":2})

# # Create the LCEL retrieval chain
# chain = (
#     {"context": retriever, "question": RunnablePassthrough()}
#     | prompt_template
#     | llm
#     | StrOutputParser()
# )

# # Invoke the chain
# print(chain.invoke("Who are the authors?"))