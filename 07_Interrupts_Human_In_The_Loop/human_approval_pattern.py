"""
Human approval pattern.

Note:
- This is a revision template.
- Exact resume handling can vary by LangGraph version and client.
- Key idea: interrupt pauses, Command resumes.
"""

from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import interrupt, Command


class State(TypedDict):
    action: str
    approved: bool
    result: str


def request_approval(state: State):
    """Pause the graph and ask a human to approve the action."""
    decision = interrupt({
        "question": "Approve this action?",
        "action": state["action"],
    })
    return {"approved": decision == "approve"}


def execute_action(state: State):
    """Runs only after approval state is available."""
    if state["approved"]:
        return {"result": f"Executed: {state['action']}"}
    return {"result": "Action rejected"}


builder = StateGraph(State)
builder.add_node("approval", request_approval)
builder.add_node("execute", execute_action)
builder.add_edge(START, "approval")
builder.add_edge("approval", "execute")
builder.add_edge("execute", END)

graph = builder.compile(checkpointer=InMemorySaver())
config = {"configurable": {"thread_id": "approval-demo"}}

# First call pauses at interrupt.
print(graph.invoke({"action": "send email", "approved": False, "result": ""}, config=config))

# Resume pattern:
# print(graph.invoke(Command(resume="approve"), config=config))
