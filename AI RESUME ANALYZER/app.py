import streamlit as st
from parser import extract_text
from extractor import extract_name, extract_email, extract_phone
from skills import extract_skills
from ai_ats import calculate_ats_score
from matcher import find_missing_skills
from suggestions import generate_suggestions
from report import create_report

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.sidebar.title("🤖 AI Resume Analyzer")

st.sidebar.info("""
Upload your resume and compare it with a job description.

### Features
✅ Resume Parsing
                
✅ Skill Extraction
                
✅ AI ATS Score
                
✅ Missing Skills
                
✅ AI Suggestions
""")

st.title("📄 AI Resume Analyzer for Job Portals")

st.markdown(
    "Analyze your resume using AI and compare it with a job description."
)


# ---------------- Upload Resume ----------------
uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

# ---------------- Job Description ----------------
job_description = st.text_area(
    "Paste Job Description Here"
)

# ---------------- Resume Analysis ----------------
if uploaded_file is not None:

    # Extract Resume Text
    text = extract_text(uploaded_file)

    # Extract Candidate Details
    name = extract_name(text)
    email = extract_email(text)
    phone = extract_phone(text)
    skills = extract_skills(text)

    # Display Candidate Details
    st.subheader("👤 Candidate Details")

    st.write("**Name:**", name)
    st.write("**Email:**", email)
    st.write("**Phone:**", phone)

    # Display Skills
    st.subheader("💻 Extracted Skills")

    if skills:
        for skill in skills:
            st.success(skill)
    else:
        st.warning("No skills found.")

    # Display Resume Text
    with st.expander("📄 View Extracted Resume Text"):
        st.write(text)

    # ---------------- AI ATS Analysis ----------------
    if job_description.strip():

        score = calculate_ats_score(text, job_description)

        st.subheader("🤖 AI ATS Score")

        st.progress(min(int(score), 100))
        st.success(f"{score:.2f}% Match")

        # Missing Skills
        missing_skills = find_missing_skills(text, job_description)

        suggestions = generate_suggestions(score, missing_skills)

        st.subheader("❌ Missing Skills")

        if missing_skills:
            for skill in missing_skills:
                st.warning(skill)
        else:
            st.success("No important skills are missing!")
        st.subheader("💡 AI Resume Suggestions")

        for suggestion in suggestions:
            st.info(suggestion)
            report = create_report(
            name,
            email,
            phone,
            skills,
            score,
            missing_skills,
            suggestions
        )

        st.download_button(
            label="📥 Download Analysis Report",
            data=report,
            file_name="Resume_Analysis_Report.txt",
            mime="text/plain"
        )

    

    else:
        st.info("Paste a job description to calculate the AI ATS score.")

else:
    st.info("Please upload a PDF resume to begin analysis.")
    
    