# AI Resume Analyzer using RAG

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square\&logo=python)
![LLM](https://img.shields.io/badge/LLM-Gemini-blue?style=flat-square)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20DB-orange?style=flat-square)
![RAG](https://img.shields.io/badge/RAG-Retrieval%20Augmented-green?style=flat-square)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-red?style=flat-square\&logo=streamlit)](https://shree0156-ai-resume-analyzer-rag-app-iinqgm.streamlit.app/)

> AI-powered Resume Analyzer that evaluates resume-job fit using Retrieval-Augmented Generation (RAG), identifies skill gaps, and provides actionable improvement suggestions.

---

##  The Problem

Recruiters typically spend **seconds scanning resumes**, often relying on keyword matching.
This leads to:

* Strong candidates being overlooked
* Poor alignment between resumes and job roles
* Lack of actionable feedback for candidates

This project solves that by building an **AI-driven resume evaluation system** that understands context, not just keywords.

---

##  How It Works

```
Resume (PDF)
     │
     ▼
Text Extraction (PyPDF2)
     │
     ▼
Chunking
     │
     ▼
Embeddings (Sentence Transformers)
     │
     ▼
FAISS Vector Store
     │
     ▼
Relevant Context Retrieval
     │
     ▼
Gemini LLM (RAG)
     │
     ▼
Structured Output
 ─ Match Score
 ─ Strong Points
 ─ Missing Skills
 ─ Suggestions
     │
     ▼
Streamlit Web App
```

---

##  Features

* Resume-job match scoring
* Skill gap identification
* Context-aware analysis using RAG
* Structured JSON output
* Interactive Streamlit UI
* Real-time PDF resume upload

---

##  Example Output

* **Match Score:** 92%
* **Confidence:** High
* **Strong Points:** ML pipeline, deployment, Python expertise
* **Missing Skills:** Advanced statistics, MLOps exposure
* **Suggestions:** Improve business impact, highlight scalability

---

##  App Demo
<img width="983" height="747" alt="image" src="https://github.com/user-attachments/assets/5c26a6b1-89ad-4531-bcef-08e144f5210f" />

!Demo(demo.gif)

---

##  Project Structure

```
AI-Resume-Analyzer-RAG/
│
├── app.py                  # Streamlit UI
├── rag_pipeline.py         # RAG pipeline (embeddings + retrieval + LLM)
├── requirements.txt        # Dependencies
└── README.md
```

---

##  Run Locally

**1. Clone the repository**

```bash
git clone https://github.com/your-username/AI-Resume-Analyzer-RAG.git
cd AI-Resume-Analyzer-RAG
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Set API Key (Windows)**

```bash
setx GEMINI_API_KEY "your_api_key"
```

**4. Run the app**

```bash
streamlit run app.py
```

---

## 🧠 Tech Stack

| Component       | Technology            |
| --------------- | --------------------- |
| Language        | Python                |
| LLM             | Gemini API            |
| Embeddings      | Sentence Transformers |
| Vector DB       | FAISS                 |
| UI              | Streamlit             |
| PDF Parsing     | PyPDF2                |
| Data Processing | NumPy                 |

---

##  Key Design Decisions

**Why RAG?**
Instead of sending the full resume to the LLM, relevant sections are retrieved first.
This improves:

* accuracy
* context relevance
* reduces hallucination

---

**Why FAISS?**
Efficient similarity search for high-dimensional embeddings, enabling fast retrieval.

---

**Why structured JSON output?**
Makes the system:

* scalable
* API-ready
* easy to integrate into dashboards or ATS systems

---

##  Challenges & Learnings

* Handling LLM output inconsistencies (JSON parsing)
* Managing API limits and quota constraints
* Optimizing chunking and retrieval for better accuracy
* Secure API key handling using environment variables

---

##  Future Improvements

* [ ] Highlight matched resume lines
* [ ] Add score breakdown (skills vs experience)
* [ ] Multi-resume comparison
* [ ] Add MLOps pipeline (Docker + CI/CD)
* [ ] Improve UI/UX for recruiter dashboards

---

##  Author

**Shreeja Maiya**
