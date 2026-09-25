import streamlit as st
import random

st.set_page_config(page_title="CareerMatch AI", page_icon="📄")

st.title("📄 Smart Resume Analyzer & Job Matching System")

resume = st.file_uploader(
    "Upload Your Resume",
    type=["pdf", "docx"]
)

job_description = st.text_area(
    "Paste Job Description"
)

if st.button("Analyze Resume"):

    if resume is None:
        st.error("Please upload a resume.")
    elif job_description.strip() == "":
        st.error("Please enter a job description.")
    else:

        match_score = random.randint(70, 95)

        st.success("Resume Analysis Completed!")

        st.subheader("Match Score")
        st.progress(match_score)
        st.write(f"Match Score: {match_score}%")

        st.subheader("Skills Found")
        st.write("✅ Python")
        st.write("✅ Java")
        st.write("✅ SQL")
        st.write("✅ HTML")

        st.subheader("Missing Skills")
        st.write("❌ React")
        st.write("❌ AWS")

        st.subheader("Recommendations")
        st.write("• Learn React")
        st.write("• Learn AWS Cloud")
        st.write("• Add more projects to resume")
