from utils.evaluation import evaluate_pipeline


def evaluator_agent(state):
    """
    Evaluate research pipeline outputs.
    """

    research = state["research"]
    summary = state["summary"]
    critique = state["critique"]

    metrics = evaluate_pipeline(
        research_text=research,
        summary_text=summary,
        critique_text=critique
    )

    state["semantic_similarity"] = metrics[
        "semantic_similarity"
    ]

    state["bleu_score"] = metrics[
        "bleu_score"
    ]

    state["critic_score"] = metrics[
        "critic_score"
    ]

    return state