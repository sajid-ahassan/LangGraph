"""
Reducer example.

Purpose:
- Show how reducers combine state updates.
- Without `Annotated[list, add]`, the second node would overwrite messages.
"""

from typing import TypedDict, Annotated
from operator import add
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    # add means: old list + new list
    messages: Annotated[list[str], add]


def first_node(state: State):
    """Adds the first message."""
    return {"messages": ["First node completed"]}


def second_node(state: State):
    """Adds another message without deleting the first one."""
    return {"messages": ["Second node completed"]}


builder = StateGraph(State)
builder.add_node("first", first_node)
builder.add_node("second", second_node)
builder.add_edge(START, "first")
builder.add_edge("first", "second")
builder.add_edge("second", END)

graph = builder.compile()
print(graph.invoke({"messages": []}))
