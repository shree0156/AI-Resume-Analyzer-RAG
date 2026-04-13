
import google.generativeai as genai
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Configure Gemini API
import os

api_key = os.getenv("GEMINI_API_KEY")

if api_key is None:
    api_key = "YOUR_API_KEY"

genai.configure(api_key=api_key)
llm = genai.GenerativeModel("gemini-2.5-flash")

# Load embedding model
embed_model = SentenceTransformer("all-MiniLM-L6-v2")


def chunk_text(text, chunk_size=200):
    words = text.split()
    return [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]


def create_embeddings(chunks):
    embeddings = embed_model.encode(chunks)
    return np.array(embeddings)


def build_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index


def retrieve(query, chunks, index, k=3):
    query_embedding = embed_model.encode([query])
    D, I = index.search(query_embedding, k)
    return [chunks[i] for i in I[0]]


def analyze_resume(resume_text, job_description):

    # Step 1: Chunking
    chunks = chunk_text(resume_text)

    # Step 2: Embeddings
    embeddings = create_embeddings(chunks)

    # Step 3: FAISS index
    index = build_faiss_index(embeddings)

    # Step 4: Retrieval
    relevant_chunks = retrieve(job_description, chunks, index)
    context = "\n".join(relevant_chunks)

    # Step 5: LLM Prompt
    prompt = f"""
You are an AI hiring assistant.

STRICT RULES:
- Return ONLY valid JSON
- No extra text
- No explanation outside JSON

Format:
{{
    "match_score": "",
    "confidence": "",
    "strong_points": [],
    "missing_skills": [],
    "suggestions": []
}}

Context:
{context}

Job Description:
{job_description}
"""

    # Step 6: Generate response
    response = llm.generate_content(prompt)

    return response.text
