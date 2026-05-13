"""
Checkpoint memory example.

Purpose:
- Save graph state between invocations.
- Use same thread_id to continue a session.
"""

from typing import TypedDict, Annotated
from operator import add
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver


class State(TypedDict):
    messages: Annotated[list[str], add]


def chatbot(state: State):
    """Adds a bot message. The reducer appends it to history."""
    last_user_message = state["messages"][-1]
    return {"messages": [f"Bot remembers you said: {last_user_message}"]}


builder = StateGraph(State)
builder.add_node("chatbot", chatbot)
builder.add_edge(START, "chatbot")
builder.add_edge("chatbot", END)

# InMemorySaver is for demos. Use a database-backed saver in production.
checkpointer = InMemorySaver()
graph = builder.compile(checkpointer=checkpointer)

config = {"configurable": {"thread_id": "revision-thread-1"}}

print(graph.invoke({"messages": ["Hello"]}, config=config))
print(graph.invoke({"messages": ["What did I say?"]}, config=config))
