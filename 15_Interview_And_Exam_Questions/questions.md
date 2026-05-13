# LangGraph Revision Questions

## Basic

1. What is StateGraph?
2. What is a node?
3. What is an edge?
4. What is the difference between START and END?
5. What does `graph.invoke()` do?

## State

1. Why is state important?
2. What happens when a node returns a dictionary?
3. What is a reducer?
4. Why use `Annotated[list, add]`?
5. Why is `add_messages` useful?

## Routing

1. What is a conditional edge?
2. What does a router function return?
3. When should you use branching?
4. How do loops work in LangGraph?

## Memory

1. What is a checkpointer?
2. Why do interrupts require persistence?
3. What is a thread ID?
4. Difference between short-term and long-term memory?

## Agents

1. What is the model-tool loop?
2. What does ToolNode do?
3. What does `tools_condition` do?
4. When does an agent stop?

## RAG

1. Why use LangGraph for RAG?
2. How can you add query rewriting?
3. How can you add answer grading?
4. How can you prevent hallucination?

## Advanced

1. What is a subgraph?
2. When should you use Functional API?
3. What is streaming useful for?
4. How does LangSmith help debug a graph?
