# LangGraph Revision Material

Goal: revise LangGraph by looking at folder names and small runnable examples.

LangGraph is used when an LLM app needs **state**, **steps**, **branching**, **loops**, **memory**, **streaming**, or **human approval**.

## Mental Model

```text
State  -> shared data of the graph
Node   -> one function/step that reads state and returns updates
Edge   -> path from one node to another
Router -> function that decides the next path
Graph  -> compiled workflow/agent
Checkpoint -> saved state for memory, resume, interrupt, time travel
```

## Best Revision Order

1. `01_Core_Concepts`
2. `02_State_And_Reducers`
3. `03_Nodes_And_Edges`
4. `04_Routing_And_Conditional_Edges`
5. `05_Loops_And_Agents`
6. `06_Memory_And_Checkpointing`
7. `07_Interrupts_Human_In_The_Loop`
8. `08_Tools_And_ToolNode`
9. `09_RAG_With_LangGraph`
10. `10_Streaming`
11. `11_Subgraphs`
12. `12_Functional_API`
13. `13_Debugging_LangSmith`
14. `14_Project_Structure`

## Install

```bash
pip install langgraph langchain langchain-openai python-dotenv
```

Optional for local testing:

```bash
pip install grandalf
```

`grandalf` helps when drawing graphs in some environments.
"# LangGraph" 
