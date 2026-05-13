"""
Tool-calling agent template.

Requires a chat model that supports tool calling.
Set OPENAI_API_KEY in .env before running.
"""

from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool


class State(TypedDict):
    # add_messages is a LangGraph reducer designed for chat messages.
    messages: Annotated[list, add_messages]


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


tools = [multiply]
llm = ChatOpenAI(model="gpt-4o-mini").bind_tools(tools)


def chatbot(state: State):
    """Model reads messages and may return either an answer or a tool call."""
    response = llm.invoke(state["messages"])
    return {"messages": [response]}


builder = StateGraph(State)
builder.add_node("chatbot", chatbot)
builder.add_node("tools", ToolNode(tools))
builder.add_edge(START, "chatbot")

# tools_condition routes to "tools" if the model requested a tool.
# Otherwise it routes to END.
builder.add_conditional_edges("chatbot", tools_condition)

# After tool execution, return to chatbot so model can produce final answer.
builder.add_edge("tools", "chatbot")

graph = builder.compile()

# result = graph.invoke({"messages": [("user", "What is 12 times 8?")]})
# print(result["messages"][-1].content)
