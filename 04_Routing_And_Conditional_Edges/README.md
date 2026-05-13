# 04 Routing and Conditional Edges

Conditional edges make LangGraph powerful.

They let the graph choose the next node based on state.

```text
question -> classifier -> simple_answer
                      -> rag_answer
                      -> human_review
```

## Router function

A router returns a label.

```python
def route(state):
    if state["needs_search"]:
        return "search"
    return "answer"
```

Then map labels to nodes.
