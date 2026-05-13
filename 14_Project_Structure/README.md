# 14 Recommended LangGraph Project Structure

Use this structure when building real projects.

```text
LANGGRAPH_PROJECT/
│
├── app/
│   ├── main.py
│   └── api.py
│
├── graphs/
│   ├── basic_graph.py
│   ├── rag_graph.py
│   ├── agent_graph.py
│   └── approval_graph.py
│
├── state/
│   ├── schemas.py
│   └── reducers.py
│
├── nodes/
│   ├── llm_nodes.py
│   ├── rag_nodes.py
│   ├── tool_nodes.py
│   └── human_nodes.py
│
├── routers/
│   ├── intent_router.py
│   └── tool_router.py
│
├── tools/
│   ├── calculator.py
│   └── search.py
│
├── rag/
│   ├── loaders.py
│   ├── splitters.py
│   ├── vectorstore.py
│   └── retrievers.py
│
├── memory/
│   └── checkpointing.py
│
├── prompts/
│   ├── system_prompts.py
│   └── rag_prompts.py
│
├── configs/
│   └── settings.py
│
├── tests/
│   ├── test_graphs.py
│   └── test_routers.py
│
├── .env
├── requirements.txt
└── README.md
```

## Why this is good

- `state/` keeps schemas clean
- `nodes/` keeps graph steps reusable
- `routers/` keeps branching logic easy to revise
- `graphs/` shows how everything connects
- `memory/` separates persistence from business logic
- `rag/` separates retrieval pipeline from agent logic
