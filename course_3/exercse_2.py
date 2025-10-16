# Define this math function as a tool
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
import math
import os 
from langchain_core.messages import HumanMessage,AIMessage
model = ChatOpenAI(open_api_key=os.getenv("OPEN_API_KEY"),model='gpt-4o-mini')
@tool
def hypotenuse_length(input: str) -> float:
    """Calculates the length of the hypotenuse of a right-angled triangle given the lengths of the other two sides."""
    
    # Split the input string to get the lengths of the triangle
    sides = input.split(',')
    
    # Convert the input values to floats, removing extra spaces
    a = float(sides[0].strip())
    b = float(sides[1].strip())
    
    # Square each of the values, add them together, and find the square root 
    return math.sqrt(a**2 + b**2)

# Create a list variable and pass in your tool
tools = [hypotenuse_length]

# Create a query using natural language
query = "What is the hypotenuse length of a triangle with side lengths of 10 and 12?"

# Pass in the hypotenuse length tool and create the agent
app = create_react_agent(model, tools=tools)

# Invoke the agent and print the response
response = app.invoke({"messages": [("human", query)]})
print(response['messages'][-1].content)


#EXERCISE 3

tools = [hypotenuse_length]
query = "What is the value of the hypotenuse for a triangle with sides 3 and 5?"

# Create the ReAct agent
app = create_react_agent(model, tools)

# Invoke the agent with a query and store the messages
response = app.invoke({"messages": [("human", query)]})

# Define and print the input and output messages
print({
    "user_input": query,
    "agent_output": response["messages"][-1].content
})
#    {'user_input': 'What is the value of the hypotenuse for a triangle with sides 3 and 5?', 'agent_output': 'The length of the hypotenuse for a triangle with sides 3 and 5 is approximately 5.83.'}

message_history = response["messages"]
new_query = "What about one with sides 12 and 14?"

# Invoke the app with the full message history
response = app.invoke({"messages": message_history + [("human",new_query)]})

# Extract the human and AI messages from the result
filtered_messages = [msg for msg in response["messages"] if isinstance(msg, (HumanMessage, AIMessage)) and msg.content.strip()]

# Pass the new query as input and print the final outputs
print({
    "user_input": new_query,
    "agent_output": [f"{msg.__class__.__name__}: {msg.content}" for msg in filtered_messages]
})