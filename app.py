import streamlit as st
import PyPDF2
import json
from rag_pipeline import analyze_resume

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title(" AI Resume Analyzer (RAG)")
st.write("Upload your resume and compare it with a job description")

uploaded_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])
jd = st.text_area(" Paste Job Description")

if st.button("Analyze"):

    if uploaded_file is not None and jd:

        reader = PyPDF2.PdfReader(uploaded_file)
        resume_text = ""

        for page in reader.pages:
            resume_text += page.extract_text()

        with st.spinner("Analyzing..."):
            result = analyze_resume(resume_text, jd)

        try:
            clean_result = result.strip()

            # Fix: if LLM adds extra text accidentally
            if clean_result.startswith("```"):
                clean_result = clean_result.replace("```json", "").replace("```", "").strip()

            result_json = json.loads(clean_result)

            st.metric("📊 Match Score", result_json["match_score"])
            st.write("**Confidence:**", result_json["confidence"])

            st.markdown("###  Strong Points")
            for point in result_json["strong_points"]:
                st.success(point)

            st.markdown("###  Missing Skills")
            for skill in result_json["missing_skills"]:
                st.warning(skill)

            st.markdown("###  Suggestions")
            for s in result_json["suggestions"]:
                st.info(s)

        except:
            st.error(" Error parsing result")
            st.write(result)

    else:
        st.warning("Please upload resume and enter job description")