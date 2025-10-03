#Custom Tool Calls
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool
import os 
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

@tool
def retrieve_customer_info(name: str) -> str:
    """Retrieve customer information based on their name."""
    #customer_info = customers[customers['name'] == name]
    #return customer_info.to_string()
    return "cool math names"
  
# Print the tool's arguments
print(retrieve_customer_info("Peak Performance Co."))
print(retrieve_customer_info.args)

agent = create_react_agent(llm,[retrieve_customer_info])

# Invoke the agent on the input
messages = agent.invoke({"messages": [("human", "Create a summary of our customer: Peak Performance Co.")]})
print(messages['messages'][-1].content)

