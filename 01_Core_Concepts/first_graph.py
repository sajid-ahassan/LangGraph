"""
First LangGraph example.

Purpose:
- Build the smallest possible graph.
- Understand StateGraph, nodes, edges, START, and END.
"""

from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    """State is the shared data passed between all graph nodes."""
    topic: str
    summary: str


def summarize_node(state: State):
    """A node is just a Python function.

    It receives the current state and returns only the fields it wants to update.
    Here we read state['topic'] and write state['summary'].
    """
    return {"summary": f"LangGraph revision topic: {state['topic']}"}


builder = StateGraph(State)

# Register the node with a name.
builder.add_node("summarize", summarize_node)

# START is the graph entry point.
builder.add_edge(START, "summarize")

# END means graph execution is complete.
builder.add_edge("summarize", END)

# Compile converts the builder into a runnable graph.
graph = builder.compile()

result = graph.invoke({"topic": "nodes and edges"})
print(result)
