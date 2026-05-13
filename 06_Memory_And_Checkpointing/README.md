# 06 Memory and Checkpointing

Persistence/checkpointing saves graph state.

It enables:

- short-term memory
- continuing a thread
- resuming after interruption
- human-in-the-loop
- state inspection
- time travel/debugging

## Thread ID

A thread ID identifies one conversation/session.

```python
config = {"configurable": {"thread_id": "user-1"}}
graph.invoke(input_state, config=config)
```

Use the same thread ID to continue the same saved state.
