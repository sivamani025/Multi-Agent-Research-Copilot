from langchain_community.llms import Ollama


llm = Ollama(model="mistral")


def critic_agent(state):

    summary = state["summary"]

    prompt = f"""
You are a Senior Research Quality Analyst.

Evaluate the following research summary.

Give output in this format:

Overall Score: X/10

Strengths:
- point 1
- point 2

Weaknesses:
- point 1
- point 2

Missing Information:
- point 1
- point 2

Improvement Suggestions:
- point 1
- point 2

Research Summary:
{summary}
"""

    critique = llm.invoke(prompt)

    state["critique"] = critique

    return state