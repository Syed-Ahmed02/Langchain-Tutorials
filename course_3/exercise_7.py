# Create input message with the user's query
def multi_tool_output(query):
    inputs = {"messages": [HumanMessage(content=query)]}
    
    # Stream messages and metadata from the chatbot application
    for msg, metadata in app.stream(inputs, config, stream_mode="messages"):
        
        # Check if the message has content and is not from a human
        if msg.content and not isinstance(msg, HumanMessage):
            print(msg.content, end="", flush=True)    
    print("\n")

# Call the chatbot with different tools
multi_tool_output("Is `may a moody baby doom a yam` a palindrome?")
multi_tool_output("What happened on 20th July, 1969?")

# <script.py> output:
#     The phrase or word 'may a moody baby doom a yam' is a palindrome.Yes, the phrase "may a moody baby doom a yam" is a palindrome.
    
#     On July 20, 1969, one of the most significant events in human history took place: the Apollo 11 mission successfully landed astronauts Neil Armstrong and Buzz Aldrin on the Moon. Neil Armstrong became the first human to set foot on the lunar surface, followed by Aldrin. Armstrong’s famous words as he stepped onto the Moon were, "That's one small step for [a] man, one giant leap for mankind." This event marked a major milestone in the space race and represented a significant achievement in space exploration and technology. It also had profound implications for science, engineering, and international relations during the Cold War era.On July 20, 1969, one of the most significant events in human history took place: the Apollo 11 mission successfully landed astronauts Neil Armstrong and Buzz Aldrin on the Moon. Neil Armstrong became the first human to set foot on the lunar surface, followed by Aldrin. Armstrong’s famous words as he stepped onto the Moon were, "That's one small step for [a] man, one giant leap for mankind." This event marked a major milestone in the space race and represented a significant achievement in space exploration and technology. It also had profound implications for science, engineering, and international relations during the Cold War era.On July 20, 1969, the Apollo 11 mission successfully landed astronauts Neil Armstrong and Buzz Aldrin on the Moon. Neil Armstrong became the first human to set foot on the lunar surface, followed by Aldrin. His famous words as he stepped onto the Moon were, "That's one small step for [a] man, one giant leap for mankind." This event marked a major milestone in the space race and represented a significant achievement in space exploration and technology, with profound implications for science, engineering, and international relations during the Cold War era.
    
    

Print the user query first for every interaction 
def user_agent_multiturn(queries):  
    for query in queries:
        print(f"User: {query}")
        
        # Stream through messages corresponding to queries, excluding metadata 
        print("Agent: " + "".join(msg.content for msg, metadata in app.stream(
                {"messages": [HumanMessage(content=query)]}, config, stream_mode="messages") 
            
            # Filter out the human messages to print agent messages
            if msg.content and not isinstance(msg, HumanMessage)) + "____")       

queries = ["Is `stressed desserts?` a palindrome?", "What about the word `kayak`?",
    "What happened on the May 8th, 1945?", "What about 9 November 1989?"]
user_agent_multiturn(queries)

#  User: Is `stressed desserts?` a palindrome?
#     Agent: The phrase or word 'stressed desserts?' is a palindrome.Yes, the phrase "stressed desserts?" is a palindrome. This means it reads the same forwards and backwards, ignoring spaces, punctuation, and capitalization.____
#     User: What about the word `kayak`?
#     Agent: The phrase or word 'kayak' is a palindrome.Yes, the word "kayak" is also a palindrome, as it reads the same forwards and backwards.____
#     User: What happened on the May 8th, 1945?
#     Agent: May 8, 1945, is known as V-E Day, or Victory in Europe Day. This date marked the official acceptance of Nazi Germany's unconditional surrender to the Allied Forces, effectively bringing an end to World War II in Europe. Celebrations took place in many cities across Europe and the United States as people rejoiced at the defeat of Hitler's regime. 
    
#     The war in Europe had lasted for nearly six years, resulting in immense loss of life and widespread destruction. V-E Day was a significant turning point, leading to the eventual rebuilding of Europe and the establishment of various international organizations aimed at preventing such global conflicts in the future. Would you like more information about this historical event?May 8, 1945, is known as V-E Day, or Victory in Europe Day. This date marked the official acceptance of Nazi Germany's unconditional surrender to the Allied Forces, effectively bringing an end to World War II in Europe. Celebrations took place in many cities across Europe and the United States as people rejoiced at the defeat of Hitler's regime. 
    
#     The war in Europe had lasted for nearly six years, resulting in immense loss of life and widespread destruction. V-E Day was a significant turning point, leading to the eventual rebuilding of Europe and the establishment of various international organizations aimed at preventing such global conflicts in the future. Would you like more information about this historical event?On May 8, 1945, known as V-E Day (Victory in Europe Day), Nazi Germany officially surrendered to the Allied Forces, effectively bringing an end to World War II in Europe. This day was celebrated across many cities in Europe and the United States as people rejoiced at the defeat of Hitler's regime.
    
#     The war in Europe had lasted nearly six years, resulting in tremendous loss of life and widespread destruction. V-E Day marked a significant turning point, leading to the eventual rebuilding of Europe and the establishment of various international organizations aimed at preventing future global conflicts.____
#     User: What about 9 November 1989?
#     Agent: November 9, 1989, is a significant date in history, primarily known for the fall of the Berlin Wall. The Berlin Wall was a symbol of the Cold War and divided East and West Berlin from its construction in 1961 until 1989. Its fall marked the beginning of the reunification of Germany and was a pivotal moment in the collapse of communist regimes in Eastern Europe. The event is often celebrated as a symbol of freedom and the end of a divided Europe. Would you like to know more about the events surrounding this date or its historical significance?November 9, 1989, is a significant date in history, primarily known for the fall of the Berlin Wall. The Berlin Wall was a symbol of the Cold War and divided East and West Berlin from its construction in 1961 until 1989. Its fall marked the beginning of the reunification of Germany and was a pivotal moment in the collapse of communist regimes in Eastern Europe. The event is often celebrated as a symbol of freedom and the end of a divided Europe. Would you like to know more about the events surrounding this date or its historical significance?On November 9, 1989, the Berlin Wall fell, marking a significant event in history. The wall had been a symbol of the Cold War, dividing East and West Berlin since its construction in 1961. Its fall was a pivotal moment that initiated the reunification of Germany and signaled the decline of communist regimes in Eastern Europe.
    
#     This event is celebrated as a symbol of freedom and the beginning of a new era in Europe, highlighting th