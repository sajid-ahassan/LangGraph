"""
Conditional routing example.

Flow:
START -> classify
             -> answer_directly OR retrieve_first
             -> END
"""

from typing import TypedDict, Literal
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    question: str
    route: str
    answer: str


def classify(state: State):
    """Decides whether the question needs retrieval.

    In a real app this could be an LLM classifier.
    Here we use simple keyword logic for revision clarity.
    """
    q = state["question"].lower()
    if "document" in q or "rag" in q:
        return {"route": "retrieve"}
    return {"route": "direct"}


def router(state: State) -> Literal["answer_directly", "retrieve_first"]:
    """Returns the next node name based on state['route']."""
    if state["route"] == "retrieve":
        return "retrieve_first"
    return "answer_directly"


def answer_directly(state: State):
    """Answers without retrieval."""
    return {"answer": "Direct answer: use a simple node."}


def retrieve_first(state: State):
    """Pretends to retrieve context before answering."""
    return {"answer": "RAG answer: retrieve context, then answer."}


builder = StateGraph(State)
builder.add_node("classify", classify)
builder.add_node("answer_directly", answer_directly)
builder.add_node("retrieve_first", retrieve_first)
builder.add_edge(START, "classify")
builder.add_conditional_edges("classify", router)
builder.add_edge("answer_directly", END)
builder.add_edge("retrieve_first", END)

graph = builder.compile()
print(graph.invoke({"question": "How does RAG use documents?"}))
