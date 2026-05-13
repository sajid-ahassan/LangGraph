"""
Streaming updates example.

Purpose:
- See each graph update as it happens.
"""

from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    text: str
    step1: str
    step2: str


def step1(state: State):
    """First update."""
    return {"step1": state["text"].upper()}


def step2(state: State):
    """Second update."""
    return {"step2": state["step1"] + " !!!"}


builder = StateGraph(State)
builder.add_node("step1", step1)
builder.add_node("step2", step2)
builder.add_edge(START, "step1")
builder.add_edge("step1", "step2")
builder.add_edge("step2", END)

graph = builder.compile()

for update in graph.stream({"text": "stream me", "step1": "", "step2": ""}):
    print(update)
