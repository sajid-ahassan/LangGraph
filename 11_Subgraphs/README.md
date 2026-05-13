# 11 Subgraphs

A subgraph is a graph used inside another graph.

Use subgraphs when one workflow is reusable.

Examples:

- research subgraph
- RAG subgraph
- approval subgraph
- data cleaning subgraph

## Mental model

```text
Main graph
  -> classify
  -> Subgraph: research workflow
  -> final response
```

Subgraphs keep big applications organized.
