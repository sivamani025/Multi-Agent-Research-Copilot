from utils.report_utils import (
    generate_pdf,
    generate_docx
)


def report_generator_agent(state):

    topic = state["topic"]
    summary = state["summary"]
    critique = state["critique"]

    metrics = {
        "Semantic Similarity":
        state["semantic_similarity"],

        "BLEU Score":
        state["bleu_score"],

        "Critic Score":
        state["critic_score"]
    }

    pdf_path = generate_pdf(
        topic,
        summary,
        critique,
        metrics
    )

    docx_path = generate_docx(
        topic,
        summary,
        critique,
        metrics
    )

    state["pdf_path"] = pdf_path
    state["docx_path"] = docx_path

    return state