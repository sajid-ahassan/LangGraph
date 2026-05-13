# LangGraph One-Page Cheatsheet

## Core imports

```python
from typing import TypedDict, Annotated, Literal
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
```

## Basic graph pattern

```python
class State(TypedDict):
    topic: str
    answer: str

def node_name(state: State):
    return {"answer": f"Revision for {state['topic']}"}

builder = StateGraph(State)
builder.add_node("node_name", node_name)
builder.add_edge(START, "node_name")
builder.add_edge("node_name", END)
graph = builder.compile()

print(graph.invoke({"topic": "LangGraph"}))
```

## What to memorize

| Concept | Meaning | Example |
|---|---|---|
| State | Shared memory between nodes | `messages`, `documents`, `answer` |
| Node | Function that does one task | call LLM, retrieve docs, grade answer |
| Edge | Connection between nodes | `add_edge("a", "b")` |
| Conditional edge | Branching decision | route to `tools` or `END` |
| Reducer | How repeated updates combine | append messages instead of overwrite |
| Checkpointer | Saves graph state | memory, resume, interrupts |
| Interrupt | Pause graph for user input | approval before tool execution |
| ToolNode | Executes tools requested by model | search, calculator, database |
| Subgraph | Graph inside another graph | reusable research workflow |
| Streaming | Watch updates in real time | token/state/debug streams |
