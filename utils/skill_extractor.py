# ==========================================
# SKILL EXTRACTION MODULE
# ==========================================


# ==========================================
# MASTER SKILL LIST
# ==========================================

SKILLS_DB = [

    # Programming Languages

    "python",
    "java",
    "c",
    "c++",
    "c#",
    "javascript",
    "typescript",
    "php",
    "sql",

    # Web Development

    "html",
    "css",
    "react",
    "nodejs",
    "express",
    "django",
    "flask",
    "streamlit",

    # AI / ML

    "machine learning",
    "deep learning",
    "nlp",
    "tensorflow",
    "pytorch",
    "scikit-learn",

    # Database

    "mysql",
    "mongodb",
    "postgresql",

    # Tools

    "git",
    "github",
    "docker",
    "figma",

    # Game Development

    "unity",
    "unreal engine",
    "blender",
    "photon",

    # Concepts

    "data structures",
    "algorithms",
    "oop",
    "operating systems",
    "computer graphics"

]


# ==========================================
# EXTRACT SKILLS
# ==========================================

def extract_skills(text):

    text = text.lower()

    found_skills = set()

    for skill in SKILLS_DB:

        if skill.lower() in text:

            found_skills.add(skill)

    return sorted(found_skills)


# ==========================================
# MATCHED + MISSING SKILLS
# ==========================================

def get_skill_analysis(resume_skills, job_skills):

    resume_skills = set(resume_skills)

    job_skills = set(job_skills)

    matched_skills = resume_skills.intersection(job_skills)

    missing_skills = job_skills.difference(resume_skills)

    return {

        "matched_skills": sorted(matched_skills),

        "missing_skills": sorted(missing_skills)

    }