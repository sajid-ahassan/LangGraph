"""
RAG graph template.

This is intentionally simple and dependency-light.
Replace fake_retrieve() and fake_generate() with real vector store + LLM calls.
"""

from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    question: str
    documents: list[str]
    answer: str


def retrieve(state: State):
    """Retrieves relevant documents.

    Real version:
    docs = vectorstore.similarity_search(state['question'])
    return {'documents': [doc.page_content for doc in docs]}
    """
    docs = [
        "LangGraph uses StateGraph to define stateful workflows.",
        "Nodes update state; edges control execution order.",
    ]
    return {"documents": docs}


def generate(state: State):
    """Generates an answer using retrieved documents.

    Real version:
    prompt = format_prompt(question, documents)
    answer = llm.invoke(prompt)
    """
    context = "\n".join(state["documents"])
    return {"answer": f"Question: {state['question']}\nAnswer based on context:\n{context}"}


builder = StateGraph(State)
builder.add_node("retrieve", retrieve)
builder.add_node("generate", generate)
builder.add_edge(START, "retrieve")
builder.add_edge("retrieve", "generate")
builder.add_edge("generate", END)

graph = builder.compile()
print(graph.invoke({"question": "What is LangGraph?", "documents": [], "answer": ""}))
