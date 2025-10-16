from langchain_openai import ChatOpenAI,OpenAIEmbeddings
from ragas.integrations.langchain import EvaluatorChain
from ragas.metrics import context_precision


# Define the context precision chain
context_precision_chain = EvaluatorChain(metric=context_precision, llm=llm, embeddings=embeddings)

# Evaluate the context precision of the RAG chain
eval_result = context_precision_chain({
  "question": "How does RAG enable AI applications?",
  "ground_truth": "RAG enables AI applications by integrating external data in generative models.",
  "contexts": [
    "RAG enables AI applications by integrating external data in generative models.",
    "RAG enables AI applications such as semantic search engines, recommendation systems, and context-aware chatbots."
  ]
})

print(f"Context Precision: {eval_result['context_precision']}")


# from ragas.metrics import faithfulness

# # Query the retriever using the query and extract the document text
# query = "How does RAG improve question answering with LLMs?"
# retrieved_docs = [doc.page_content for doc in retriever.invoke(query)]

# # Define the faithfulness chain
# faithfulness_chain = EvaluatorChain(metric=faithfulness, llm=llm, embeddings=embeddings)

# # Evaluate the faithfulness of the RAG chain
# eval_result = faithfulness_chain({
#   "question": query,
#   "answer": chain.invoke(query),
#   "contexts": retrieved_docs
# })

# print(eval_result)


# Create the QA string evaluator
# qa_evaluator = LangChainStringEvaluator(
#     "qa",
#     config={
#         "llm": eval_llm,
#         "prompt": prompt_template
#     }
# )

# query = "How does RAG improve question answering with LLMs?"

# # Evaluate the RAG output by evaluating strings
# score = qa_evaluator.evaluator.evaluate_strings(
#     prediction=predicted_answer,
#     reference=ref_answer,
#     input=query
# )

# print(f"Score: {score}")