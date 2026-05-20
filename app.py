# ==========================================
# AI RESUME SCREENING & JOB MATCHING SYSTEM
# ==========================================

import streamlit as st
import plotly.express as px
import pandas as pd

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
# CUSTOM CSS
# ==========================================

st.markdown("""

<style>

.main {
    background-color: #0E1117;
}

.stButton>button {

    width: 100%;
    border-radius: 10px;
    height: 3em;
    font-size: 18px;
    font-weight: bold;
}

.metric-card {

    background-color: #1E1E1E;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
}

.skill-box {

    background-color: #1E1E1E;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 10px;
}

</style>

""", unsafe_allow_html=True)


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("📄 AI Resume ATS")

st.sidebar.markdown("---")

st.sidebar.info(

    """
    ### Features

    ✅ Resume Parsing

    ✅ NLP Processing

    ✅ Skill Extraction

    ✅ ATS Match Score

    ✅ Multi Resume Ranking

    ✅ AI Recommendation

    """
)

st.sidebar.markdown("---")

st.sidebar.success(

    "Developed Using Python + NLP + Streamlit"

)


# ==========================================
# MAIN TITLE
# ==========================================

st.title("📄 AI Resume Screening & Job Matching System")

st.markdown(

    "### Intelligent ATS-Based Resume Analyzer"

)

st.markdown("---")


# ==========================================
# JOB DESCRIPTION INPUT
# ==========================================

job_description = st.text_area(

    "💼 Enter Job Description",

    height=220,

    placeholder="Paste complete job description here..."

)


# ==========================================
# FILE UPLOADER
# ==========================================

uploaded_files = st.file_uploader(

    "📄 Upload Resume(s)",

    type=["pdf", "docx", "txt"],

    accept_multiple_files=True

)


# ==========================================
# MAIN ANALYSIS
# ==========================================

if uploaded_files and job_description != "":

    st.success(

        f"{len(uploaded_files)} Resume(s) Uploaded Successfully ✅"

    )

    if st.button("🚀 Analyze Resumes"):

        all_results = []

        with st.spinner("Analyzing Resumes..."):

            # ==========================================
            # PROCESS JOB DESCRIPTION
            # ==========================================

            processed_job = preprocess_text(

                job_description

            )

            job_skills = extract_skills(

                processed_job

            )

            # ==========================================
            # PROCESS EACH RESUME
            # ==========================================

            for uploaded_file in uploaded_files:

                # ==========================================
                # EXTRACT TEXT
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

                # ==========================================
                # SKILL EXTRACTION
                # ==========================================

                resume_skills = extract_skills(

                    processed_resume

                )

                # ==========================================
                # SKILL ANALYSIS
                # ==========================================

                analysis = get_skill_analysis(

                    resume_skills,

                    job_skills

                )

                matched_skills = analysis["matched_skills"]

                missing_skills = analysis["missing_skills"]

                # ==========================================
                # SIMILARITY SCORE
                # ==========================================

                similarity_score = calculate_similarity(

                    processed_resume,

                    processed_job

                )

                # ==========================================
                # SKILL MATCH SCORE
                # ==========================================

                skill_match_score = calculate_skill_match_score(

                    matched_skills,

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
                # SAVE RESULTS
                # ==========================================

                all_results.append({

                    "Candidate":

                    uploaded_file.name,

                    "ATS Score":

                    round(final_score, 2),

                    "Similarity":

                    round(similarity_score, 2),

                    "Skill Match":

                    round(skill_match_score, 2),

                    "Matched Skills":

                    ", ".join(matched_skills)

                    if matched_skills else "None",

                    "Missing Skills":

                    ", ".join(missing_skills)

                    if missing_skills else "None",

                    "Recommendation":

                    recommendation

                })

        # ==========================================
        # CREATE DATAFRAME
        # ==========================================

        results_df = pd.DataFrame(

            all_results

        )

        # ==========================================
        # SORT RESULTS
        # ==========================================

        results_df = results_df.sort_values(

            by="ATS Score",

            ascending=False

        )

        # ==========================================
        # BEST CANDIDATE
        # ==========================================

        top_candidate = results_df.iloc[0]

        st.success(

            f"🏆 Best Candidate: {top_candidate['Candidate']}"

        )

        # ==========================================
        # DASHBOARD METRICS
        # ==========================================

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(

                "📄 Total Resumes",

                len(results_df)

            )

        with col2:

            st.metric(

                "🏆 Highest ATS Score",

                f"{top_candidate['ATS Score']}%"

            )

        with col3:

            st.metric(

                "🎯 Best Match",

                top_candidate["Candidate"]

            )

        st.markdown("---")

        # ==========================================
        # RESULTS TABLE
        # ==========================================

        st.subheader("📊 Resume Ranking Table")

        st.dataframe(

            results_df,

            use_container_width=True

        )

        # ==========================================
        # DOWNLOAD CSV REPORT
        # ==========================================

        results_df.to_csv(

            "results/ATS_Resume_Report.csv",

            index=False

        )

        csv_data = results_df.to_csv(

            index=False

        ).encode("utf-8")

        st.download_button(

            label="⬇ Download ATS Report CSV",

            data=csv_data,

            file_name="ATS_Resume_Report.csv",

            mime="text/csv"

        )

        st.markdown("---")

        # ==========================================
        # BAR CHART
        # ==========================================

        st.subheader("📈 ATS Resume Ranking")

        fig = px.bar(

            results_df,

            x="Candidate",

            y="ATS Score",

            color="ATS Score",

            text="ATS Score",

            title="ATS Resume Ranking"

        )

        fig.update_layout(

            template="plotly_dark",

            height=500

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

        # ==========================================
        # PIE CHART
        # ==========================================

        st.subheader("🥧 Candidate Score Distribution")

        pie_fig = px.pie(

            results_df,

            names="Candidate",

            values="ATS Score",

            title="Candidate Score Distribution"

        )

        pie_fig.update_layout(

            template="plotly_dark",

            height=500

        )

        st.plotly_chart(

            pie_fig,

            use_container_width=True

        )

        # ==========================================
        # DETAILED CANDIDATE ANALYSIS
        # ==========================================

        st.markdown("---")

        st.subheader("🧠 Detailed Candidate Analysis")

        for index, row in results_df.iterrows():

            with st.expander(

                f"📄 {row['Candidate']} | ATS Score: {row['ATS Score']}%"

            ):

                col1, col2 = st.columns(2)

                with col1:

                    st.success("✅ Matched Skills")

                    st.write(row["Matched Skills"])

                with col2:

                    st.error("❌ Missing Skills")

                    st.write(row["Missing Skills"])

                st.info(

                    f"🎯 Recommendation: {row['Recommendation']}"

                )

else:

    st.info(

        "👈 Please upload resume(s) and enter job description to begin analysis."

    )