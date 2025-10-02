from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model="gpt-5-nano-2025-08-07", api_key=os.getenv("OPENAI_API_KEY"))

# Predict the words following the text in question
prompt = 'Three reasons for using LangChain for LLM application development.'
#response = llm.invoke(prompt)
#print(response.content)

## Hugging Face models

from langchain_huggingface import HuggingFacePipeline

# Define the LLM from the Hugging Face model ID
llm = HuggingFacePipeline.from_model_id(
    model_id="crumb/nano-mistral",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 20}
)

prompt = "Hugging Face is"

# Invoke the model
response = llm.invoke(prompt)
print(response)