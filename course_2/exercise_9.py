from langchain_openai import ChatOpenAI
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_community.graphs import Neo4jGraph
from langchain_community.chains.graph_qa.cypher import GraphCypherQAChain

graph_qa_chain = GraphCypherQAChain.from_llm(
    graph=graph,llm=llm,verbose=True,exclude_types=["Concept"]
)

# Invoke the chain with the input provided
result = graph_qa_chain.invoke({"query": "Who was Marie Curie married to?"})
print(f"Final answer: {result['result']}")

# <script.py> output:
    
    
#     [1m> Entering new GraphCypherQAChain chain...[0m
#     Generated Cypher:
#     [32;1m[1;3mMATCH (p:Person {id: 'Marie Curie'})-[:SPOUSE]->(spouse:Person) RETURN spouse.id[0m
#     Full Context:
#     [32;1m[1;3m[{'spouse.id': 'Pierre Curie'}][0m
    
#     [1m> Finished chain.[0m
#     Final answer: Marie Curie was married to Pierre Curie.

# Create the graph QA chain, validating the generated Cypher query
graph_qa_chain = GraphCypherQAChain.from_llm(
    graph=graph,llm=llm,verbose=True,validate_cypher=True
)

# Invoke the chain with the input provided
result = graph_qa_chain.invoke({"query": "Who won the Nobel Prize In Physics?"})
print(f"Final answer: {result['result']}")

# > Entering new GraphCypherQAChain chain...
# Generated Cypher:
# cypher
# MATCH (p:Person)-[:AWARDED]->(a:Award {id: "Nobel Prize In Physics"})
# RETURN p.id

# Full Context:
# [{'p.id': 'Albert Einstein'}, {'p.id': 'Marie Curie'}]

# > Finished chain.
# Final answer: Albert Einstein won the Nobel Prize in Physics.


example_prompt = PromptTemplate.from_template(
    "User input: {question}\nCypher query: {query}"
)

# Create the few-shot prompt template
cypher_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="You are a Neo4j expert. Given an input question, create a syntactically correct Cypher query to run.\n\nHere is the schema information\n{schema}.\n\nBelow are a number of examples of questions and their corresponding Cypher queries.",
    suffix="User input: {question}\nCypher query: ",
    input_variables=["question"]
)

# Create the graph Cypher QA chain
graph_qa_chain = GraphCypherQAChain.from_llm(
    graph=graph,llm=llm,cypher_prompt=cypher_prompt,verbose=True,validate_cypher=True
)

# Invoke the chain with the input provided
result = graph_qa_chain.invoke({"query": "Which scientist proposed the Theory Of Relativity?"})
print(f"Final answer: {result['result']}")


# > Entering new GraphCypherQAChain chain...
# Generated Cypher:
# cypher
# MATCH (p:Person)-[:KNOWN_FOR]->(c:Concept {id: 'Theory Of Relativity'}) RETURN p

# Full Context:
# [{'p': {'id': 'Albert Einstein'}}]

# > Finished chain.
# Final answer: Albert Einstein proposed the Theory of Relativity.