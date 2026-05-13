# Functional API Notes

The Functional API is useful when your code already looks like normal Python functions.

Instead of thinking first in nodes and edges, you think in tasks and workflows.

Conceptually:

```python
@task
def step_a(...):
    ...

@entrypoint(checkpointer=...)
def workflow(...):
    result = step_a(...).result()
    return result
```

Revision point: Graph API gives maximum control. Functional API gives faster adoption.
