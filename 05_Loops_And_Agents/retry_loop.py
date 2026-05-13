"""
Loop example.

Flow:
START -> draft -> grade
                 -> rewrite if bad
                 -> END if good
"""

from typing import TypedDict, Literal
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    draft: str
    score: int
    attempts: int


def draft(state: State):
    """Creates the first draft."""
    return {"draft": "short answer", "attempts": 1}


def grade(state: State):
    """Grades the answer.

    In real life, this can be an LLM-as-judge or rule-based evaluator.
    """
    score = 10 if len(state["draft"]) > 30 else 4
    return {"score": score}


def rewrite(state: State):
    """Improves the draft and increments attempts."""
    return {
        "draft": state["draft"] + " with more explanation and examples",
        "attempts": state["attempts"] + 1,
    }


def should_continue(state: State) -> Literal["rewrite", "end"]:
    """Stops if score is good or too many attempts are used."""
    if state["score"] >= 8 or state["attempts"] >= 3:
        return "end"
    return "rewrite"


builder = StateGraph(State)
builder.add_node("draft", draft)
builder.add_node("grade", grade)
builder.add_node("rewrite", rewrite)
builder.add_edge(START, "draft")
builder.add_edge("draft", "grade")
builder.add_conditional_edges("grade", should_continue, {"rewrite": "rewrite", "end": END})
builder.add_edge("rewrite", "grade")

graph = builder.compile()
print(graph.invoke({"draft": "", "score": 0, "attempts": 0}))
