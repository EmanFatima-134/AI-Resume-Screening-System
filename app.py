# ==========================================
# AI RESUME SCREENING SYSTEM
# ==========================================

import streamlit as st

from utils.pdf_extractor import extract_resume_text

from utils.text_preprocessing import preprocess_text

from utils.skill_extractor import (
    extract_skills,
    get_skill_analysis
)

from utils.similarity_calculator import (

    calculate_similarity,

    calculate_skill_match_score,

    calculate_final_score

)

from utils.recommendation import generate_recommendation


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(

    page_title="AI Resume Screening System",

    page_icon="📄",

    layout="wide"

)


# ==========================================
# TITLE
# ==========================================

st.title("📄 AI Resume Screening & Job Matching System")

st.markdown("---")


# ==========================================
# JOB DESCRIPTION INPUT
# ==========================================

job_description = st.text_area(

    "💼 Enter Job Description",

    height=200

)


# ==========================================
# FILE UPLOADER
# ==========================================

uploaded_file = st.file_uploader(

    "📄 Upload Resume",

    type=["pdf", "docx", "txt"]

)


# ==========================================
# MAIN ANALYSIS
# ==========================================

if uploaded_file is not None and job_description != "":

    st.success("Resume Uploaded Successfully ✅")

    if st.button("🚀 Analyze Resume"):

        with st.spinner("Analyzing Resume..."):

            # ==========================================
            # EXTRACT RESUME TEXT
            # ==========================================

            extracted_text = extract_resume_text(

                uploaded_file

            )

            # ==========================================
            # NLP PROCESSING
            # ==========================================

            processed_resume = preprocess_text(

                extracted_text

            )

            processed_job = preprocess_text(

                job_description

            )

            # ==========================================
            # SKILL EXTRACTION
            # ==========================================

            resume_skills = extract_skills(

                processed_resume

            )

            job_skills = extract_skills(

                processed_job

            )

            # ==========================================
            # SKILL ANALYSIS
            # ==========================================

            analysis = get_skill_analysis(

                resume_skills,

                job_skills

            )

            # ==========================================
            # COSINE SIMILARITY
            # ==========================================

            similarity_score = calculate_similarity(

                processed_resume,

                processed_job

            )

            # ==========================================
            # SKILL MATCH SCORE
            # ==========================================

            skill_match_score = calculate_skill_match_score(

                analysis["matched_skills"],

                job_skills

            )

            # ==========================================
            # FINAL ATS SCORE
            # ==========================================

            final_score = calculate_final_score(

                similarity_score,

                skill_match_score

            )

            # ==========================================
            # RECOMMENDATION
            # ==========================================

            recommendation = generate_recommendation(

                final_score

            )

        # ==========================================
        # SCORE SECTION
        # ==========================================

        st.subheader("📊 Match Score")

        st.progress(int(final_score))

        st.metric(

            label="Final ATS Match Score",

            value=f"{final_score}%"

        )

        st.write(

            f"📌 Cosine Similarity Score: {similarity_score}%"

        )

        st.write(

            f"🧠 Skill Match Score: {skill_match_score}%"

        )

        # ==========================================
        # RECOMMENDATION
        # ==========================================

        st.subheader("🎯 Recommendation")

        st.info(recommendation)

        # ==========================================
        # SKILL DISPLAY
        # ==========================================

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("🧠 Resume Skills")

            st.success(

                resume_skills

            )

        with col2:

            st.subheader("💼 Job Skills")

            st.warning(

                job_skills

            )

        # ==========================================
        # MATCHED SKILLS
        # ==========================================

        st.subheader("✅ Matched Skills")

        st.success(

            analysis["matched_skills"]

        )

        # ==========================================
        # MISSING SKILLS
        # ==========================================

        st.subheader("❌ Missing Skills")

        st.error(

            analysis["missing_skills"]

        )

        # ==========================================
        # RAW RESUME TEXT
        # ==========================================

        with st.expander(

            "📄 View Extracted Resume Text"

        ):

            st.text_area(

                "Resume Content",

                extracted_text,

                height=300

            )

        # ==========================================
        # NLP PROCESSED TEXT
        # ==========================================

        with st.expander(

            "🧠 View NLP Processed Text"

        ):

            st.text_area(

                "Processed Resume",

                processed_resume,

                height=300

            )