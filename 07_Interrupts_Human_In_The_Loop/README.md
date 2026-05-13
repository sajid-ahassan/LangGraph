# 07 Interrupts and Human-in-the-Loop

Interrupts pause graph execution and wait for external input.

Use cases:

- approve email before sending
- review tool call
- ask user for missing information
- confirm dangerous action

Important: interrupts need persistence/checkpointing because the graph must save state before pausing.
