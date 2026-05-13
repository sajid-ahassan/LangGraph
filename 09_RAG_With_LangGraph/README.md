# 09 RAG with LangGraph

RAG is better in LangGraph when you want controllable steps.

## Basic RAG graph

```text
question -> retrieve -> generate -> answer
```

## Advanced RAG graph

```text
question -> retrieve -> grade documents
                     -> if relevant: generate
                     -> if not relevant: rewrite question -> retrieve again
                     -> grade answer
                     -> if hallucinated: regenerate
```

## Why LangGraph for RAG?

- easy to inspect each step
- easy to retry bad retrieval
- easy to add query rewriting
- easy to add human review
- easy to stream progress
