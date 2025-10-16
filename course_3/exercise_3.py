#Graph & Agent States
from dotenv.main import load_dotenv
from langchain_openai import ChatOpenAI
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
import os
from IPython.display import Image, display
import dotenv
load_dotenv()
# Define the llm
llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

# Define the State
class State(TypedDict):
    
    # Define messages with metadata
    messages: Annotated[list, add_messages]

# Initialize StateGraph
graph_builder = StateGraph(State)

# Define chatbot function to respond with the model
def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}

# Add chatbot node to the graph
graph_builder.add_node("chatbot", chatbot)

# Define the start and end of the conversation flow
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

# Compile the graph to prepare for execution
graph = graph_builder.compile()

#EXERCISE 5

# Define a function to execute the chatbot based on user input
def stream_graph_updates(user_input: str):
    
    # Start streaming events from the graph with the user's input
    for event in graph.stream({"messages": [("user", user_input)]}):
        
        # Retrieve and print the chatbot node responses
        for item in event.values():
            print("Agent:", item["messages"])

# Define the user query and run the chatbot
user_query = "Who is Ada Lovelace?"
stream_graph_updates(user_query)

# Try generating and displaying the diagram of the graph
try:
    display(Image(graph.get_graph().draw_mermaid_png()))

# Return an exception if the generation fails
except Exception:
    print("Diagram generation requires additional dependencies.")