# 13 Debugging and LangSmith

Debugging matters because agents can be unpredictable.

Use LangSmith to inspect:

- graph traces
- node execution order
- model inputs and outputs
- tool calls
- errors
- latency
- token usage

## Environment variables

```bash
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=your_key_here
```

## Revision habit

Whenever a graph behaves strangely, inspect:

1. input state
2. output state from each node
3. router decision
4. tool call arguments
5. final state
