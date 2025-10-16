from langchain_openai import ChatOpenAI
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_community.graphs import Neo4jGraph
from langchain_community.chains.graph_qa.cypher import GraphCypherQAChain
llm = ChatOpenAI(api_key="<OPENAI_API_TOKEN>", model="gpt-4o-mini", temperature=0)

# Instantiate the LLM graph transformer
llm_transformer = LLMGraphTransformer(llm=llm)

# Convert the text documents to graph documents
graph_documents = llm_transformer.convert_to_graph_documents(docs)
print(f"Derived Nodes:\n{graph_documents[0].nodes}\n")
print(f"Derived Edges:\n{graph_documents[0].relationships}")

#use env vars
graph = Neo4jGraph(url=url, username=user, password=password)

# Add the graph documents, sources, and include entity labels
graph.add_graph_documents(
    graph_documents,
    include_source=True,
    baseEntityLabel=True
)

graph.refresh_schema()

# Print the graph schema
print(graph.get_schema)

# <script.py> output:
#     Node properties:
#     Document {id: STRING, source: STRING, text: STRING}
#     Person {id: STRING}
#     Award {id: STRING}
#     Concept {id: STRING}
#     Element {id: STRING}
#     Relationship properties:
    
#     The relationships:
#     (:Document)-[:MENTIONS]->(:Element)
#     (:Document)-[:MENTIONS]->(:Award)
#     (:Document)-[:MENTIONS]->(:Person)
#     (:Document)-[:MENTIONS]->(:Concept)
#     (:Person)-[:EXPLANATION_FOR]->(:Concept)
#     (:Person)-[:KNOWN_FOR]->(:Concept)
#     (:Person)-[:AWARDED]->(:Award)
#     (:Person)-[:DISCOVERED]->(:Element)
#     (:Person)-[:SPOUSE]->(:Person)
#     (:Person)-[:COLLABORATOR]->(:Person)

# Print the graph schema
print(graph.get_schema)

# Query the graph
results = graph.query("""
MATCH (relativity:Concept {id: "Theory Of Relativity"}) <-[:KNOWN_FOR]- (scientist)
return scientist
""")


print(results[0])

#{'scientist': {'id': 'Albert Einstein'}}

graph_qa_chain = GraphCypherQAChain.from_llm(
    llm=ChatOpenAI(api_key="<OPENAI_API_TOKEN>", temperature=0), graph=graph, verbose=True
)

# Invoke the chain with the input provided
result = graph_qa_chain.invoke({"query": "Who discovered the element Radium?"})

# Print the result text
print(f"Final answer: {result['result']}")