# 05 Loops and Agents

Loops are useful for agents and quality improvement.

Example:

```text
write answer -> grade answer -> if bad: rewrite -> grade again -> if good: END
```

## Agent loop idea

```text
model -> tool -> model -> tool -> model -> final answer
```

The model decides whether to call a tool or finish.
