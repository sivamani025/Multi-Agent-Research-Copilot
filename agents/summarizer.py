from langchain_community.llms import Ollama


llm = Ollama(model="mistral")


def summarizer_agent(state):

    research = state["research"]

    prompt = f"""
You are a Senior Research Summarization Agent.

Create an executive summary of the research.

Return the response in the following format:

Executive Summary:
(brief overview)

Key Findings:
- finding 1
- finding 2
- finding 3

Challenges:
- challenge 1
- challenge 2

Future Outlook:
(short paragraph)

Research:
{research}
"""

    summary = llm.invoke(prompt)

    state["summary"] = summary

    return state