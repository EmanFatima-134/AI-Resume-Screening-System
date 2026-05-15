# ==========================================
# SIMILARITY CALCULATION MODULE
# ==========================================

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ==========================================
# COSINE SIMILARITY SCORE
# ==========================================

def calculate_similarity(resume_text, job_description):

    documents = [

        resume_text,

        job_description

    ]

    # TF-IDF Vectorization

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(documents)

    # Cosine Similarity

    similarity_score = cosine_similarity(

        tfidf_matrix[0:1],

        tfidf_matrix[1:2]

    )[0][0]

    # Convert to percentage

    similarity_percentage = round(

        similarity_score * 100,

        2

    )

    return similarity_percentage


# ==========================================
# SKILL MATCH SCORE
# ==========================================

def calculate_skill_match_score(

    matched_skills,

    job_skills

):

    if len(job_skills) == 0:

        return 0

    score = (

        len(matched_skills)

        /

        len(job_skills)

    ) * 100

    return round(score, 2)


# ==========================================
# FINAL ATS SCORE
# ==========================================

def calculate_final_score(

    similarity_score,

    skill_match_score

):

    final_score = (

        (0.3 * similarity_score)

        +

        (0.7 * skill_match_score)

    )

    return round(final_score, 2)