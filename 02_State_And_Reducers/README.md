# 02 State and Reducers

State is the most important LangGraph concept.

## State means

The dictionary-like object that every node reads and updates.

```python
class State(TypedDict):
    messages: list
    question: str
    answer: str
```

## Normal update behavior

Without a reducer, a field is overwritten.

```python
return {"answer": "new answer"}
```

## Reducer behavior

Reducers tell LangGraph how to combine updates.

Example: append messages instead of replacing them.

```python
from typing import Annotated
from operator import add

class State(TypedDict):
    messages: Annotated[list, add]
```

Now every node can return new messages, and they will be appended.
