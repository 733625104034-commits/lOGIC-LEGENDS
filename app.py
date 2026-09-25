import streamlit as st

st.title("Smart Resume Analyzer & Job Matching System")

st.file_uploader("Upload Your Resume", type=["pdf", "docx"])
job_description = st.text_area("Paste Job Description")
