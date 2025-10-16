from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
import math
import os 
model = ChatOpenAI(open_api_key=os.getenv("OPEN_API_KEY"),model='gpt-4o-mini')
# 
# Create the agent
app = create_react_agent(model=model, tools=[count_r_in_word])

# Create a query
query = "How many r's are in the word 'Terrarium'?"

# Invoke the agent and store the response
response = app.invoke({"messages": [("human", query)]})

# Print the agent's response
print(response['messages'][-1].content)