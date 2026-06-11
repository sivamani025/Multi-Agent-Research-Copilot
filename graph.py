from typing import TypedDict

from langgraph.graph import (
    StateGraph,
    END
)

from agents.planner import planner_agent
from agents.researcher import researcher_agent
from agents.summarizer import summarizer_agent
from agents.critic import critic_agent
from agents.evaluator import evaluator_agent
from agents.report_generator import (
    report_generator_agent
)


class AgentState(TypedDict):

    topic: str

    plan: str
    research: str
    summary: str
    critique: str

    pdf_path: str
    docx_path: str

    latency: float

    semantic_similarity: float
    bleu_score: float
    critic_score: float


workflow = StateGraph(
    AgentState
)

# Nodes

workflow.add_node(
    "planner",
    planner_agent
)

workflow.add_node(
    "researcher",
    researcher_agent
)

workflow.add_node(
    "summarizer",
    summarizer_agent
)

workflow.add_node(
    "critic",
    critic_agent
)

workflow.add_node(
    "evaluator",
    evaluator_agent
)

workflow.add_node(
    "report_generator",
    report_generator_agent
)

# Entry

workflow.set_entry_point(
    "planner"
)

# Flow

workflow.add_edge(
    "planner",
    "researcher"
)

workflow.add_edge(
    "researcher",
    "summarizer"
)

workflow.add_edge(
    "summarizer",
    "critic"
)

workflow.add_edge(
    "critic",
    "evaluator"
)

workflow.add_edge(
    "evaluator",
    "report_generator"
)

workflow.add_edge(
    "report_generator",
    END
)

graph = workflow.compile()