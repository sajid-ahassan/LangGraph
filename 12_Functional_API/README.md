# 12 Functional API

LangGraph also has a Functional API.

Use it when you want LangGraph features without manually defining a full `StateGraph`.

Good for:

- existing Python workflows
- simpler migration
- adding persistence/memory/streaming gradually

For revision, remember:

```text
Graph API       -> explicit nodes and edges
Functional API  -> decorate functions/tasks and run workflow style
```
