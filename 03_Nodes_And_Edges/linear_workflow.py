"""
Linear workflow example.

Flow:
START -> plan -> write -> polish -> END
"""

from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    topic: str
    plan: str
    draft: str
    final: str


def plan(state: State):
    """Creates a simple plan from the topic."""
    return {"plan": f"Explain {state['topic']} in 3 simple points."}


def write(state: State):
    """Uses the plan to create a draft."""
    return {"draft": f"Draft based on plan: {state['plan']}"}


def polish(state: State):
    """Turns the draft into final output."""
    return {"final": state["draft"].replace("Draft", "Final answer")}


builder = StateGraph(State)
builder.add_node("plan", plan)
builder.add_node("write", write)
builder.add_node("polish", polish)
builder.add_edge(START, "plan")
builder.add_edge("plan", "write")
builder.add_edge("write", "polish")
builder.add_edge("polish", END)

graph = builder.compile()
print(graph.invoke({"topic": "conditional edges"}))
