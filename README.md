# 🤖 Multi-Agent Research Copilot

An AI-powered research assistant built using **LangGraph**, **LangChain**, **LLMs**, and **Streamlit** that automates the complete research workflow through multiple specialized agents.

---

## 🚀 Overview

Multi-Agent Research Copilot is an Agentic AI system that performs:

* Research Planning
* Detailed Research Generation
* Executive Summarization
* Research Critique
* Automated Evaluation
* PDF Report Generation
* DOCX Report Generation

The system uses a multi-agent architecture where each agent is responsible for a specific task in the research pipeline.

---

## 🏗️ Architecture

```text
User Topic
    ↓
Planner Agent
    ↓
Research Agent
    ↓
Summarizer Agent
    ↓
Critic Agent
    ↓
Evaluator Agent
    ↓
Report Generator Agent
    ↓
PDF / DOCX Reports
```

---

## 🤖 Agents

### 1. Planner Agent

Creates a structured research roadmap.

### 2. Research Agent

Generates detailed research content.

### 3. Summarizer Agent

Produces executive summaries and key findings.

### 4. Critic Agent

Reviews research quality and identifies improvements.

### 5. Evaluator Agent

Computes evaluation metrics.

### 6. Report Generator Agent

Generates downloadable PDF and DOCX reports.

---

## 📊 Evaluation Metrics

The system automatically evaluates research quality using:

| Metric              | Description                             |
| ------------------- | --------------------------------------- |
| Semantic Similarity | Similarity between research and summary |
| BLEU Score          | Content preservation score              |
| Critic Score        | Research quality score                  |
| Latency             | Workflow execution time                 |

---

## 🛠️ Tech Stack

### AI & LLM

* LangGraph
* LangChain
* Ollama (Mistral)
* Sentence Transformers

### Machine Learning

* Scikit-Learn
* NLTK

### Frontend

* Streamlit

### Reporting

* ReportLab
* Python-Docx

### Data Processing

* Pandas
* NumPy

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/multi-agent-research-copilot.git

cd multi-agent-research-copilot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

Start Ollama:

```bash
ollama serve
```

Pull Mistral model:

```bash
ollama pull mistral
```

Run Streamlit:

```bash
streamlit run app.py
```

## 📈 Features

* Multi-Agent Research Workflow
* LangGraph Orchestration
* Automated Evaluation
* PDF Report Generation
* DOCX Report Generation
* Research History Tracking
* Interactive Streamlit Dashboard

---

## 🔮 Future Improvements

* Retrieval-Augmented Generation (RAG)
* SQLite Research Memory
* Hybrid Search (BM25 + Vector Search)
* GraphRAG Integration
* Multi-LLM Support
* Agent Monitoring Dashboard

---

## 👨‍💻 Author

**Sivamani Prodduturi**

AI Engineer | Machine Learning Engineer | Generative AI Enthusiast


LinkedIn: https://linkedin.com/in/sivamani-prodduturi-487114253
