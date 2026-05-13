"""
Subgraph template.

Purpose:
- Show how one compiled graph can be used as a node in another graph.
"""

from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class ResearchState(TypedDict):
    topic: str
    notes: str


def collect_notes(state: ResearchState):
    """Research subgraph node."""
    return {"notes": f"Collected notes about {state['topic']}"}


research_builder = StateGraph(ResearchState)
research_builder.add_node("collect_notes", collect_notes)
research_builder.add_edge(START, "collect_notes")
research_builder.add_edge("collect_notes", END)
research_graph = research_builder.compile()


class MainState(TypedDict):
    topic: str
    notes: str
    final: str


def final_writer(state: MainState):
    """Uses subgraph output to write final response."""
    return {"final": f"Final answer using notes: {state['notes']}"}


main_builder = StateGraph(MainState)

# A compiled graph can be added as a node.
main_builder.add_node("research", research_graph)
main_builder.add_node("final_writer", final_writer)
main_builder.add_edge(START, "research")
main_builder.add_edge("research", "final_writer")
main_builder.add_edge("final_writer", END)

main_graph = main_builder.compile()
print(main_graph.invoke({"topic": "subgraphs", "notes": "", "final": ""}))
