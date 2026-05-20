# ==========================================
# AI RESUME SCREENING SYSTEM
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
    page_title="✨ AI Resume Screening",
    page_icon="🌸",
    layout="wide"
)


# ==========================================
# CUSTOM CSS — PINK GIRLISH THEME
# ==========================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;700&family=Quicksand:wght@400;500;600&display=swap');

:root {
    --pink-lightest: #fff0f6;
    --pink-light:    #ffd6e7;
    --pink-soft:     #ffb3cc;
    --pink-mid:      #ff85aa;
    --pink-deep:     #e8537a;
    --pink-dark:     #c23b65;
    --blush:         #ffe4ee;
    --cream:         #fff8fb;
    --text-dark:     #3d1a2e;
    --text-mid:      #6b3050;
    --text-soft:     #9e5c7a;
    --shadow-pink:   rgba(232, 83, 122, 0.18);
}

html, body, [class*="css"] {
    font-family: 'Quicksand', sans-serif !important;
    color: var(--text-dark) !important;
}

.stApp {
    background: linear-gradient(135deg, #fff0f6 0%, #ffe8f3 40%, #ffd6e7 100%) !important;
    background-attachment: fixed !important;
}

.stApp::before {
    content: "🌸 ✿ 🌺 ✿ 🌸 ✿ 🌺 ✿ 🌸 ✿ 🌺 ✿ 🌸 ✿ 🌺 ✿ 🌸 ✿ 🌺 ✿ 🌸";
    display: block;
    text-align: center;
    font-size: 0.9rem;
    letter-spacing: 4px;
    padding: 6px 0;
    background: linear-gradient(90deg, var(--pink-soft), var(--pink-mid), var(--pink-soft));
    color: white;
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 9999;
    opacity: 0.85;
}

.block-container {
    padding-top: 3.5rem !important;
    padding-bottom: 3rem !important;
    max-width: 1100px !important;
}

h1 {
    font-family: 'Playfair Display', serif !important;
    color: var(--pink-dark) !important;
    font-size: 2.6rem !important;
    letter-spacing: -0.5px;
    text-align: center;
    margin-bottom: 0 !important;
}

h2, h3 {
    font-family: 'Playfair Display', serif !important;
    color: var(--text-mid) !important;
}

hr {
    border: none !important;
    height: 2px !important;
    background: linear-gradient(90deg, transparent, var(--pink-soft), var(--pink-mid), var(--pink-soft), transparent) !important;
    margin: 1.2rem 0 !important;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #ffe0ee 0%, #ffc8de 100%) !important;
    border-right: 2px solid var(--pink-light) !important;
}

[data-testid="stSidebar"] * {
    color: var(--text-dark) !important;
    font-family: 'Quicksand', sans-serif !important;
}

[data-testid="stSidebar"] .stMarkdown h3 {
    color: var(--pink-dark) !important;
    font-family: 'Playfair Display', serif !important;
}

[data-testid="stSidebar"] .stAlert {
    background: rgba(255,255,255,0.55) !important;
    border: 1px solid var(--pink-soft) !important;
    border-radius: 14px !important;
}

.stTextArea textarea {
    background: rgba(255,255,255,0.85) !important;
    border: 2px solid var(--pink-soft) !important;
    border-radius: 16px !important;
    color: var(--text-dark) !important;
    font-family: 'Quicksand', sans-serif !important;
    font-size: 0.95rem !important;
    box-shadow: 0 4px 18px var(--shadow-pink) !important;
    transition: border 0.3s ease, box-shadow 0.3s ease !important;
}
.stTextArea textarea:focus {
    border-color: var(--pink-mid) !important;
    box-shadow: 0 6px 24px var(--shadow-pink) !important;
}

label, .stTextArea label, .stFileUploader label {
    font-family: 'Playfair Display', serif !important;
    font-size: 1.05rem !important;
    color: var(--text-mid) !important;
    font-weight: 600 !important;
}

[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.7) !important;
    border: 2px dashed var(--pink-mid) !important;
    border-radius: 18px !important;
    padding: 1.4rem !important;
    box-shadow: 0 4px 20px var(--shadow-pink) !important;
    transition: border-color 0.3s ease !important;
}
[data-testid="stFileUploader"]:hover {
    border-color: var(--pink-dark) !important;
}
[data-testid="stFileUploader"] * {
    color: var(--text-mid) !important;
}

.stButton > button {
    background: linear-gradient(135deg, var(--pink-mid) 0%, var(--pink-dark) 100%) !important;
    color: white !important;
    font-family: 'Quicksand', sans-serif !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    border: none !important;
    border-radius: 50px !important;
    padding: 0.65rem 2.5rem !important;
    letter-spacing: 0.5px !important;
    box-shadow: 0 6px 20px rgba(194, 59, 101, 0.35) !important;
    transition: all 0.3s ease !important;
    display: block !important;
    margin: 0.5rem auto !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 10px 28px rgba(194, 59, 101, 0.45) !important;
    background: linear-gradient(135deg, var(--pink-deep) 0%, var(--pink-dark) 100%) !important;
}
.stButton > button:active {
    transform: translateY(0) !important;
}

.stDownloadButton > button {
    background: white !important;
    color: var(--pink-dark) !important;
    border: 2px solid var(--pink-soft) !important;
    border-radius: 50px !important;
    font-family: 'Quicksand', sans-serif !important;
    font-weight: 700 !important;
    padding: 0.55rem 2rem !important;
    box-shadow: 0 4px 14px var(--shadow-pink) !important;
    transition: all 0.3s ease !important;
}
.stDownloadButton > button:hover {
    background: var(--pink-lightest) !important;
    border-color: var(--pink-mid) !important;
    transform: translateY(-1px) !important;
}

.stAlert {
    border-radius: 14px !important;
    font-family: 'Quicksand', sans-serif !important;
    font-weight: 600 !important;
}

[data-testid="stMetric"] {
    background: rgba(255,255,255,0.78) !important;
    border: 1.5px solid var(--pink-light) !important;
    border-radius: 18px !important;
    padding: 1.1rem 1.4rem !important;
    box-shadow: 0 6px 22px var(--shadow-pink) !important;
    backdrop-filter: blur(8px) !important;
    transition: transform 0.25s ease !important;
}
[data-testid="stMetric"]:hover {
    transform: translateY(-3px) !important;
}
[data-testid="stMetric"] label {
    color: var(--text-soft) !important;
    font-size: 0.85rem !important;
    font-family: 'Quicksand', sans-serif !important;
    font-weight: 600 !important;
}
[data-testid="stMetricValue"] {
    color: var(--pink-dark) !important;
    font-family: 'Playfair Display', serif !important;
    font-size: 1.9rem !important;
}

.stDataFrame {
    border-radius: 16px !important;
    overflow: hidden !important;
    border: 1.5px solid var(--pink-light) !important;
    box-shadow: 0 6px 24px var(--shadow-pink) !important;
}
.stDataFrame thead th {
    background: linear-gradient(90deg, var(--pink-soft), var(--pink-mid)) !important;
    color: white !important;
    font-family: 'Quicksand', sans-serif !important;
    font-weight: 700 !important;
}
.stDataFrame tbody tr:nth-child(even) {
    background: rgba(255, 214, 231, 0.22) !important;
}
.stDataFrame tbody tr:hover {
    background: rgba(255, 183, 210, 0.35) !important;
}

.stSpinner > div {
    border-top-color: var(--pink-mid) !important;
}

.js-plotly-plot {
    border-radius: 18px !important;
    overflow: hidden !important;
    box-shadow: 0 6px 24px var(--shadow-pink) !important;
}

::-webkit-scrollbar { width: 7px; }
::-webkit-scrollbar-track { background: var(--pink-lightest); }
::-webkit-scrollbar-thumb {
    background: var(--pink-soft);
    border-radius: 10px;
}
::-webkit-scrollbar-thumb:hover { background: var(--pink-mid); }

.stSubheader {
    color: var(--text-mid) !important;
    font-family: 'Playfair Display', serif !important;
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("🌸 AI Resume ATS")
st.sidebar.markdown("---")
st.sidebar.info(
    """
    ### ✨ Features
    
    🌺 Resume Parsing  
    🌸 NLP Processing  
    💗 Skill Extraction  
    🎀 ATS Match Score  
    💖 Multi Resume Ranking  
    🌷 AI Recommendation  
    """
)
st.sidebar.markdown("---")
st.sidebar.success("Developed Using Python + NLP + Streamlit 💕")


# ==========================================
# MAIN TITLE
# ==========================================

st.markdown(
    "<h1>🌸 AI Resume Screening & Job Matching</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center; color:#e8537a; font-family:Quicksand,sans-serif; font-size:1.1rem; font-weight:600; margin-top:-0.5rem;'>✨ Intelligent ATS-Based Resume Analyzer ✨</p>",
    unsafe_allow_html=True
)
st.markdown("---")


# ==========================================
# JOB DESCRIPTION
# ==========================================

job_description = st.text_area(
    "💼 Enter Job Description",
    height=220,
    placeholder="Paste your job description here... 🌷"
)


# ==========================================
# MULTIPLE FILE UPLOADER
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
        f"🌸 {len(uploaded_files)} Resume(s) Uploaded Successfully ✅"
    )

    if st.button("🚀 Analyze Resumes"):

        all_results = []

        with st.spinner("Analyzing Resumes... 💕"):

            # ==========================================
            # PROCESS JOB DESCRIPTION
            # ==========================================

            processed_job = preprocess_text(job_description)
            job_skills = extract_skills(processed_job)

            # ==========================================
            # PROCESS EACH RESUME
            # ==========================================

            for uploaded_file in uploaded_files:

                extracted_text = extract_resume_text(uploaded_file)
                processed_resume = preprocess_text(extracted_text)
                resume_skills = extract_skills(processed_resume)

                analysis = get_skill_analysis(resume_skills, job_skills)

                similarity_score = calculate_similarity(
                    processed_resume, processed_job
                )

                skill_match_score = calculate_skill_match_score(
                    analysis["matched_skills"], job_skills
                )

                final_score = calculate_final_score(
                    similarity_score, skill_match_score
                )

                recommendation = generate_recommendation(final_score)

                all_results.append({
                    "Candidate":      uploaded_file.name,
                    "ATS Score":      final_score,
                    "Similarity":     similarity_score,
                    "Skill Match":    skill_match_score,
                    "Matched Skills": len(analysis["matched_skills"]),
                    "Missing Skills": len(analysis["missing_skills"]),
                    "Recommendation": recommendation
                })

        # ==========================================
        # RESULTS DATAFRAME
        # ==========================================

        results_df = pd.DataFrame(all_results)
        results_df = results_df.sort_values(by="ATS Score", ascending=False)

        top_candidate = results_df.iloc[0]

        st.success(
            f"🏆 Best Candidate: **{top_candidate['Candidate']}** 🌸"
        )

        # ==========================================
        # DASHBOARD METRICS
        # ==========================================

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("🌸 Total Resumes", len(results_df))

        with col2:
            st.metric("🏆 Highest ATS Score", f"{top_candidate['ATS Score']}%")

        with col3:
            st.metric("🎯 Best Match", top_candidate["Candidate"])

        st.markdown("---")

        # ==========================================
        # RESULTS TABLE
        # ==========================================

        st.subheader("💗 Resume Ranking Table")
        st.dataframe(results_df, use_container_width=True)

        # ==========================================
        # DOWNLOAD CSV REPORT
        # ==========================================

        results_df.to_csv("results/ATS_Resume_Report.csv", index=False)

        csv_data = results_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="🌷 Download ATS Report CSV",
            data=csv_data,
            file_name="ATS_Resume_Report.csv",
            mime="text/csv"
        )

        # ==========================================
        # BAR CHART — pink palette
        # ==========================================

        fig = px.bar(
            results_df,
            x="Candidate",
            y="ATS Score",
            color="ATS Score",
            title="🌸 ATS Resume Ranking",
            color_continuous_scale=[
                "#ffe0ee", "#ffb3cc", "#ff85aa", "#e8537a", "#c23b65"
            ],
            template="plotly_white",
        )
        fig.update_layout(
            title_font=dict(family="Playfair Display, serif", size=22, color="#c23b65"),
            font=dict(family="Quicksand, sans-serif", color="#3d1a2e"),
            plot_bgcolor="rgba(255,240,246,0.6)",
            paper_bgcolor="rgba(255,240,246,0)",
            coloraxis_colorbar=dict(
                title="Score",
                tickfont=dict(family="Quicksand, sans-serif"),
            ),
        )
        fig.update_traces(marker_line_color="#c23b65", marker_line_width=0.8)
        st.plotly_chart(fig, use_container_width=True)

        # ==========================================
        # PIE CHART — pink palette
        # ==========================================

        pie_fig = px.pie(
            results_df,
            names="Candidate",
            values="ATS Score",
            title="💖 Candidate Score Distribution",
            color_discrete_sequence=[
                "#ffb3cc", "#ff85aa", "#e8537a", "#c23b65",
                "#ffd6e7", "#ffe0ee", "#ff6b9b", "#d94f72"
            ],
            template="plotly_white",
            hole=0.35,
        )
        pie_fig.update_layout(
            title_font=dict(family="Playfair Display, serif", size=22, color="#c23b65"),
            font=dict(family="Quicksand, sans-serif", color="#3d1a2e"),
            paper_bgcolor="rgba(255,240,246,0)",
            legend=dict(font=dict(family="Quicksand, sans-serif", size=13)),
        )
        pie_fig.update_traces(
            textfont=dict(family="Quicksand, sans-serif", size=13),
            marker=dict(line=dict(color="#ffffff", width=2)),
        )
        st.plotly_chart(pie_fig, use_container_width=True)