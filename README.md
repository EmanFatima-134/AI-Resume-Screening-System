# AI Resume Screening & Job Matching System📖

---

## **📌 Project Overview**

The **AI Resume Screening & Job Matching System** is an AI-powered recruitment assistance platform developed for the **Software Engineering Semester Project**.

This system automates the process of:
- Resume screening
- Skill extraction
- ATS score calculation
- Candidate ranking
- Resume-job matching

The project uses:
- Natural Language Processing (NLP)
- TF-IDF Vectorization
- Cosine Similarity
- Skill Matching Algorithms

Unlike manual recruitment screening, this system provides:
- faster evaluation
- skill gap analysis
- ATS-based ranking
- automated recommendations

---

## **👥 Team Information**

**Group Members**
- Eman Fatima (BSCS24134)
- Naimal Munir (BSCS24101)

---

## **💡 Project Objectives**

The main objectives of this project are:

- Automate resume screening
- Reduce manual recruitment effort
- Improve hiring efficiency
- Provide ATS-based candidate ranking
- Identify matched & missing skills
-  Generate recruiter-friendly reports
- Support multiple resume analysis  

---

## **✨ Core Features**

### 1- Resume Parsing

Supports:
- PDF resumes
- DOCX resumes
- TXT resumes

The system automatically extracts textual content from uploaded resumes.

### 2- NLP Text Processing

The project performs:
- Lowercase conversion
- Stopword removal
- Tokenization
- Punctuation removal
- Text normalization

using NLTK-based preprocessing.

### 3- Skill Extraction Engine

The system identifies technical skills such as:

- Python
- Java
- SQL
- Unity
- Git
- Blender
- Streamlit
- NLP
- Unreal Engine

and many others using custom keyword matching.

---

### 4- ATS Match Scoring

The ATS engine combines:

**1. Cosine Similarity Score**

Using:
- TF-IDF Vectorization
- Cosine Similarity

**2. Skill Match Score**

Using:
- matched skills
- missing skills
- job requirement comparison

**Final Hybrid ATS Score**

The final score is generated using weighted scoring logic.

### 5- AI Recommendation System

Based on ATS score, the system automatically generates recruiter recommendations such as:

- Excellent Match 
- Good Match 
- Average Match 
- Not Suitable 

### 6- Multi Resume Ranking

The system supports:
- multiple resume uploads
- automatic candidate comparison
- ATS-based ranking
  
Candidates are sorted automatically from highest to lowest ATS score.

### 7- Dashboard Analytics

The system includes:
- ATS metrics
- ranking table
- bar charts
- pie charts
- candidate comparison dashboard

### 8- CSV Report Export

Recruiters can:
- download ATS reports
- export ranking results
- store candidate analysis

The project automatically generates:

results/ATS_Resume_Report.csv

---

## **🧠 Why AI Resume Screening?**

Traditional recruitment processes involve manually reviewing hundreds of resumes.

This creates problems such as:
- time consumption
- human bias
- inconsistent evaluation
- recruiter fatigue

This AI-based system improves:
- speed
- consistency
- transparency
- scalability

---

## **🏗️ System Architecture**

The project follows a layered architecture.
```
Resume Upload
↓
Text Extraction
↓
NLP Preprocessing
↓
Skill Extraction
↓
TF-IDF Vectorization
↓
Cosine Similarity
↓
ATS Score Calculation
↓
Candidate Ranking
↓
Visualization & Reports
```

---

## **📁 Project Structure**

```
semester_project/
│
├── data/
│   └── sample_job_description.txt
│
├── results/
│   └── ATS_Resume_Report.csv
│
├── resumes/
│   ├── Resume 1.docx
│   ├── Resume 2.docx
│   ├── Resume 3.docx
│   └── Realistic Game Developer Resume.pdf
│
├── screenshots/
│   ├── home_page.png
│   ├── resume_upload.png
│   ├── ats_dashboard.png
│   ├── ranking_table.png
│   ├── charts.png
│   └── report_download.png
│
├── utils/
│   ├── pdf_extractor.py
│   ├── recommendation.py
│   ├── similarity_calculator.py
│   ├── skill_extractor.py
│   ├── text_preprocessing.py
│   └── visualizer.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```
---

## **⚙️ Technologies Used**

**Frontend**
- Streamlit

**Backend**
- Python

**NLP & AI**
- NLTK
- Scikit-learn

**Data Processing**
- Pandas

**Visualization**
- Plotly

---

## **📦 Python Libraries Used**

- streamlit
- nltk
- scikit-learn
- pandas
- plotly
- python-docx
- PyPDF2

---

## **⚙️ Installation & Setup**

### 1. Clone Repository
```
git clone https://github.com/EmanFatima-134/AI-Resume-Screening-System.git
```

### 2. Open Project Folder**
```
cd AI-Resume-Screening-System
```

### 3. Create Virtual Environment
```
python -m venv venv
```

### 4. Activate Virtual Environment
```
venv\Scripts\activate
```

### 5. Install Dependencies
```
pip install -r requirements.txt
```

### 6. Download NLTK Resources
```
python
```

Then run:
```
import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
exit()
```

### 7. Run Project
```
streamlit run app.py
```

---

## **🌐 Application Workflow**

### Step 1 — Enter Job Description

Recruiter enters:
- job requirements
- technical skills
- preferred qualifications

### Step 2 — Upload Resume(s)

Upload:
- PDF
- DOCX
- TXT resumes

Supports multiple resumes simultaneously.

### Step 3 — NLP Processing

The system:
- extracts text
- cleans text
- removes stopwords
- normalizes tokens

### Step 4 — ATS Analysis

The system calculates:
- similarity score
- skill match score
- final ATS score

### Step 5 — Candidate Ranking

Candidates are:
- compared
- scored
- ranked automatically

### Step 6 — Export Report

Recruiters can:
- download CSV reports
- save ranking data
- review candidate comparisons

---

## **📊 Dashboard Features**

The dashboard includes:

- ATS Score
- Similarity Score
- Skill Match Score
- AI Recommendation
- Resume Ranking Table
- Best Candidate Detection
- Charts & Analytics
- CSV Report Export  

---

## **📈 ATS Scoring Logic**

The final ATS score combines:

| Component | Weight |
|---|---|
| Skill Match Score | 70% |
| Cosine Similarity | 30% |

This improves scoring reliability by considering:
- semantic similarity
- actual skill overlap

---

## **📸 Project Screenshots**

**Home Page**
- Resume upload
- Job description input
- Sidebar features

**ATS Dashboard**
- ATS score
- Recommendation
- Metrics

**Ranking Table**
- Candidate comparison
- ATS ranking

**Charts**
- Bar graph
- Pie chart

**CSV Report Download**
- Recruiter report export

---

## **🧪 Sample Test Scenario**

### Job Role

Unity Game Developer

### Required Skills
- Unity
- Python
- Git
- Blender
- C#

### Results

The system:
- analyzes resumes
- identifies matching skills
- detects missing skills
- ranks candidates automatically

---

## **⚠️ Current Limitations**

Current limitations include:

- No deep learning models
- No database integration
- No authentication system
- Keyword-based skill extraction
- Limited resume formatting support

These limitations were acceptable within the semester project scope.

---

## **🚀 Future Improvements**

Future enhancements may include:

- Deep learning-based ranking
- BERT embeddings
- MongoDB/MySQL integration
- Recruiter login system
- Resume history tracking
- Cloud database deployment
- Advanced semantic search
- Real-time analytics

---

## **Project Compliance**

This project satisfies:
- SRS requirements
- Architecture & Design requirements
- Functional requirements
- Non-functional requirements

The project demonstrates:
- layered architecture
- modular design
- clean separation of concerns
- NLP integration
- AI-assisted recruitment workflow

---

## **🎯 Learning Outcomes**

This project helped us understand:
- Software Engineering workflow
- Requirement analysis
- Layered architecture
- NLP preprocessing
- TF-IDF vectorization
- Cosine similarity
- ATS systems
- Resume parsing
- Streamlit deployment
- Dashboard development
- GitHub collaboration

---

## **📝 Final Notes**

The AI Resume Screening & Job Matching System successfully combines:
- AI
- NLP
- recruitment automation
- dashboard analytics
- ATS ranking
- report generation

into a complete recruiter-assistance platform.

The project demonstrates practical implementation of:
- Natural Language Processing
- similarity matching
- candidate ranking
- AI-based screening systems

using modern Python technologies.

---
## **👤 Contact**

If you have any questions or would like to discuss the project:
- Naimal Munir - nemalmunir@gmail.com
- Eman Fatima - emanfatima5978@gmail.com
