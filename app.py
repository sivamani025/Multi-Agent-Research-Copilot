import os
import json
import time

import streamlit as st

from graph import graph
from utils.logger import save_run


# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="Multi-Agent Research Copilot",
    page_icon="🤖",
    layout="wide"
)


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title("📚 Research History")

history_file = "data/history.json"

if os.path.exists(history_file):

    try:

        with open(
            history_file,
            "r"
        ) as f:

            history = json.load(f)

        for item in reversed(history[-10:]):

            st.sidebar.write(
                f"• {item['topic']}"
            )

    except Exception:
        st.sidebar.info(
            "No history available."
        )


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title(
    "🤖 Multi-Agent Research Copilot"
)

st.markdown(
    """
Research topics using a multi-agent workflow.

### Agents

1. Planner Agent
2. Research Agent
3. Summarizer Agent
4. Critic Agent
5. Evaluator Agent
6. Report Generator Agent
"""
)


# --------------------------------------------------
# Input
# --------------------------------------------------

topic = st.text_input(
    "Research Topic",
    placeholder="Example: GraphRAG, Agentic AI, Generative AI in Healthcare"
)


# --------------------------------------------------
# Run Workflow
# --------------------------------------------------

if st.button(
    "🚀 Start Research",
    key="research_btn"
):

    if not topic.strip():

        st.warning(
            "Please enter a research topic."
        )

        st.stop()

    start_time = time.time()

    with st.spinner(
        "Running Multi-Agent Workflow..."
    ):

        result = graph.invoke(
            {
                "topic": topic
            }
        )

    latency = round(
        time.time() - start_time,
        2
    )

    # ----------------------------------
    # Save Run
    # ----------------------------------

    save_run(
        {
            "topic": topic,
            "latency": latency,
            "semantic_similarity":
            result.get(
                "semantic_similarity",
                0
            ),
            "bleu_score":
            result.get(
                "bleu_score",
                0
            ),
            "critic_score":
            result.get(
                "critic_score",
                0
            )
        }
    )

    st.success(
        "Research Completed Successfully!"
    )

    # ----------------------------------
    # Evaluation Dashboard
    # ----------------------------------

    st.subheader(
        "📊 Evaluation Dashboard"
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Semantic Similarity",
        round(
            result.get(
                "semantic_similarity",
                0
            ),
            3
        )
    )

    col2.metric(
        "BLEU Score",
        round(
            result.get(
                "bleu_score",
                0
            ),
            3
        )
    )

    col3.metric(
        "Critic Score",
        round(
            result.get(
                "critic_score",
                0
            ),
            2
        )
    )

    col4.metric(
        "Latency (sec)",
        latency
    )

    st.divider()

    # ----------------------------------
    # Agent Status
    # ----------------------------------

    st.subheader(
        "⚙️ Agent Execution Status"
    )

    cols = st.columns(6)

    cols[0].success("Planner ✓")
    cols[1].success("Researcher ✓")
    cols[2].success("Summarizer ✓")
    cols[3].success("Critic ✓")
    cols[4].success("Evaluator ✓")
    cols[5].success("Report ✓")

    st.divider()

    # ----------------------------------
    # Workflow
    # ----------------------------------

    st.subheader(
        "🔄 Workflow"
    )

    st.code(
        """
Topic
 ↓
Planner
 ↓
Researcher
 ↓
Summarizer
 ↓
Critic
 ↓
Evaluator
 ↓
Report Generator
"""
    )

    st.divider()

    # ----------------------------------
    # Outputs
    # ----------------------------------

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📋 Plan",
            "🔍 Research",
            "📝 Summary",
            "🧐 Critique"
        ]
    )

    with tab1:

        st.write(
            result.get(
                "plan",
                ""
            )
        )

    with tab2:

        st.write(
            result.get(
                "research",
                ""
            )
        )

    with tab3:

        st.write(
            result.get(
                "summary",
                ""
            )
        )

    with tab4:

        st.write(
            result.get(
                "critique",
                ""
            )
        )

    st.divider()

    # ----------------------------------
    # Download Reports
    # ----------------------------------

    st.subheader(
        "📥 Download Reports"
    )

    col1, col2 = st.columns(2)

    pdf_path = result.get(
        "pdf_path"
    )

    docx_path = result.get(
        "docx_path"
    )

    with col1:

        if pdf_path and os.path.exists(
            pdf_path
        ):

            with open(
                pdf_path,
                "rb"
            ) as f:

                st.download_button(
                    label="📄 Download PDF",
                    data=f,
                    file_name="research_report.pdf",
                    mime="application/pdf",
                    key="pdf_download"
                )

    with col2:

        if docx_path and os.path.exists(
            docx_path
        ):

            with open(
                docx_path,
                "rb"
            ) as f:

                st.download_button(
                    label="📝 Download DOCX",
                    data=f,
                    file_name="research_report.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    key="docx_download"
                )

    st.divider()

    # ----------------------------------
    # Raw Metrics
    # ----------------------------------

    with st.expander(
        "🔬 Raw Evaluation Metrics"
    ):

        st.json(
            {
                "semantic_similarity":
                result.get(
                    "semantic_similarity",
                    0
                ),

                "bleu_score":
                result.get(
                    "bleu_score",
                    0
                ),

                "critic_score":
                result.get(
                    "critic_score",
                    0
                ),

                "latency":
                latency
            }
        )