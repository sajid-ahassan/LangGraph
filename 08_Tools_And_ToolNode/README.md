# 08 Tools and ToolNode

Tools let the model do actions.

Examples:

- calculator
- search
- database query
- send email
- file operation

LangGraph commonly uses:

- model node: model decides whether to call tool
- tool node: executes tool call
- conditional edge: if tool call exists, go to tools; otherwise end
