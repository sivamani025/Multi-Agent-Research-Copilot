from langchain_community.llms import Ollama


llm = Ollama(model="mistral")


def researcher_agent(state):
    """
    Research Agent:
    Generates detailed research based on
    the plan created by the Planner Agent.
    """

    topic = state["topic"]
    plan = state["plan"]

    prompt = f"""
You are a Senior Research Analyst.

Research Topic:
{topic}

Research Plan:
{plan}

Create a detailed research report.

Structure your response as:

# Introduction

# Core Concepts

# Current State of the Field

# Industry Applications

# Benefits

# Challenges and Limitations

# Emerging Trends

# Future Outlook

Requirements:
- Professional tone
- Detailed explanations
- Fact-based content
- Clear section headings
"""

    research = llm.invoke(prompt)

    state["research"] = research

    return state