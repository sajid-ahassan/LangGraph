# Common LangGraph Mistakes

## 1. Putting everything in one node

Bad because it is hard to debug.

Better: split into classify, retrieve, generate, grade.

## 2. Forgetting reducers

If multiple nodes update a list, you may accidentally overwrite data.

Use reducers like `add` or `add_messages`.

## 3. No thread_id with memory

Checkpointing needs a config with `thread_id`.

## 4. Router returns wrong label

The label returned by a router must match the conditional edge mapping.

## 5. Infinite loops

Always include a stopping rule, such as max attempts.

## 6. Using InMemorySaver in production

Good for learning, not durable for production.

## 7. Mixing graph logic and business logic

Keep nodes, routers, state schemas, tools, and prompts in separate files.
