# 03 Nodes and Edges

## Node

A node is one unit of work.

Good nodes are small:

- classify intent
- call model
- retrieve documents
- grade answer
- call tool
- format response

## Edge

An edge controls the next step.

```python
builder.add_edge("draft", "review")
```

Means after `draft`, go to `review`.

## Best practice

Do not put everything into one node. Split your graph into reviewable steps.
