# 10 Streaming

Streaming lets you observe graph execution while it runs.

Common use cases:

- show node-by-node progress
- stream final model tokens
- debug state changes
- show tool execution updates

## Simple pattern

```python
for chunk in graph.stream(input_state):
    print(chunk)
```

Think of streaming as watching the graph work step by step.
