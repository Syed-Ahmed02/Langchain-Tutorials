#exercise 3 - few shot prompt template

from langchain_core.prompts import PromptTemplate,FewShotPromptTemplate
from langchain_huggingface import HuggingFacePipeline
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import os 
from dotenv import load_dotenv
load_dotenv()


examples = [
  {
    "question": "How many DataCamp courses has Jack completed?",
    "answer": "36"
  },
  {
    "question": "How much XP does Jack have on DataCamp?",
    "answer": "284,320XP"
  },
  {
    "question": "What technology does Jack learn about most on DataCamp?",
    "answer": "Python"
  }
]

# Complete the prompt for formatting answers
example_prompt = PromptTemplate.from_template("Question: {question}\n{answer}")

# Create the few-shot prompt
prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Question: {input}",
    input_variables=["input"],
)

prompt = prompt_template.invoke({"input": "What is Jack's favorite technology on DataCamp?"})
print(prompt.text)

llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

# Create and invoke the chain
llm_chain = prompt_template | llm
print(llm_chain.invoke({"input": "What is Jack's favorite technology on DataCamp?"}))