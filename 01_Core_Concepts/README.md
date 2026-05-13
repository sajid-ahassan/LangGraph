# 01 Core Concepts

LangGraph is a graph-based orchestration framework. Instead of writing one long chain, you build small steps and connect them.

## Key idea

```text
Input -> Node A -> Node B -> Node C -> Output
```

But LangGraph can also do:

```text
Input -> Classify -> if simple: answer
                  -> if complex: retrieve -> reason -> answer
                  -> if unsafe: human review
```

## When to use LangGraph

Use LangGraph when you need:

- multi-step agents
- loops
- tool calling
- retries
- human approval
- durable memory
- state inspection
- RAG pipelines with quality checks
