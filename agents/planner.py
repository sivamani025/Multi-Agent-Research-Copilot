from langchain_community.llms import Ollama


llm = Ollama(model="mistral")


def planner_agent(state):

    topic = state["topic"]

    prompt = f"""
You are a Senior Research Planning Agent.

Your task is to create a detailed research roadmap.

Generate:

# Research Objective

# Key Research Questions

# Core Concepts

# Industry Applications

# Current Challenges

# Emerging Trends

# Future Research Areas

Topic:
{topic}

Return the plan in a well-structured format.
"""

    plan = llm.invoke(prompt)

    state["plan"] = plan

    return state