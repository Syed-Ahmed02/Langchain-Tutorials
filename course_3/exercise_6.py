#Excerise 6
# Use a decorator to label the tool and set the input format to string
@tool
def historical_events(date_input: str) -> str:
    """Provide a list of important historical events for a given date in any format."""
    try:

      	# Invoke the LLM to interpret the date and generate historical events
        response = llm.invoke(f"List important historical events that occurred on {date_input}.")
        
        # Return the response
        return response.content

    # Set an exception block for errors in retrieval
    except Exception as e:
        return f"Error retrieving events: {str(e)}"
    
    
@tool
# Set input format to string
def palindrome_checker(text: str) -> str:
    """Check if a word or phrase is a palindrome."""
    
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    
    # Set up if-else block to check reversed text against original text
    if cleaned_text == cleaned_text[::-1]:
        return f"The phrase or word '{text}' is a palindrome."
    else:
        # Print an alternative statement if text is not a palindrome
        return f"The phrase or word '{text}' is not a palindrome."
    

# Import modules required for defining tool nodes
from langgraph.prebuilt import ToolNode

# List of tools
tools = [ palindrome_checker, historical_events]

# Pass the tools to the ToolNode()
tool_node = ToolNode(tools)

# Bind tools to the LLM
model_with_tools = llm.bind_tools(tools)


# Use MessagesState to define the state of the function
def should_continue(state: MessagesState):
    
    # Get the last message from the state
    last_message = state["messages"][-1]
    
    # Check if the last message includes tool calls
    if last_message.tool_calls:
        return "tools"
    
    # End the conversation if no tool calls are present
    return END

# Extract the last message from the history
def call_model(state: MessagesState):
    last_message = state["messages"][-1]

    # If the last message has tool calls, return the tool's response
    if isinstance(last_message,AIMessage) and last_message.tool_calls:
        
        # Return only the messages from the tool call
        return {"messages": [AIMessage(content=last_message.tool_calls[0]["response"])]}
    
    # Otherwise, proceed with a regular LLM response
    return {"messages": [model_with_tools.invoke(state["messages"])]}

# Add nodes for chatbot and tools
workflow.add_node("chatbot", call_model)
workflow.add_node("tools", tool_node)

# Define an edge connecting START to the chatbot
workflow.add_edge(START, "chatbot")

# Define conditional edges and route "tools" back to "chatbot"
workflow.add_conditional_edges("chatbot", should_continue, ["tools", END])
workflow.add_edge("tools", "chatbot")

# Set up memory and compile the workflow
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)

display(Image(app.get_graph().draw_mermaid_png()))

