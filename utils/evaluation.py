import re

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.translate.bleu_score import (
    sentence_bleu,
    SmoothingFunction
)


# Load model once
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def semantic_similarity(
        research_text: str,
        summary_text: str
) -> float:
    """
    Compute cosine similarity between
    research output and summary.
    """

    try:

        research_embedding = embedding_model.encode(
            [research_text]
        )

        summary_embedding = embedding_model.encode(
            [summary_text]
        )

        similarity = cosine_similarity(
            research_embedding,
            summary_embedding
        )[0][0]

        return round(
            float(similarity),
            4
        )

    except Exception as e:

        print(
            f"Semantic Similarity Error: {e}"
        )

        return 0.0


def bleu_score_eval(
        research_text: str,
        summary_text: str
) -> float:
    """
    Compute BLEU score.
    """

    try:

        reference = [
            research_text.split()
        ]

        candidate = (
            summary_text.split()
        )

        smoothie = (
            SmoothingFunction()
            .method1
        )

        bleu = sentence_bleu(
            reference,
            candidate,
            smoothing_function=smoothie
        )

        return round(
            float(bleu),
            4
        )

    except Exception as e:

        print(
            f"BLEU Error: {e}"
        )

        return 0.0


def extract_critic_score(
        critique_text: str
) -> float:
    """
    Extract score from critique.

    Example:
    Overall Score: 8.5/10
    """

    try:

        match = re.search(
            r"(\d+(\.\d+)?)\/10",
            critique_text
        )

        if match:

            return float(
                match.group(1)
            )

        return 0.0

    except Exception as e:

        print(
            f"Critic Score Error: {e}"
        )

        return 0.0


def evaluate_pipeline(
        research_text: str,
        summary_text: str,
        critique_text: str
):
    """
    Run all evaluations together.
    """

    similarity = semantic_similarity(
        research_text,
        summary_text
    )

    bleu = bleu_score_eval(
        research_text,
        summary_text
    )

    critic_score = extract_critic_score(
        critique_text
    )

    return {
        "semantic_similarity": similarity,
        "bleu_score": bleu,
        "critic_score": critic_score
    }