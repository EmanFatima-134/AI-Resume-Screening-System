# ==========================================
# PDF / DOCX / TXT RESUME EXTRACTOR
# ==========================================

import PyPDF2
import pdfplumber
from docx import Document


# ==========================================
# EXTRACT TEXT FROM PDF USING PDFPLUMBER
# ==========================================

def extract_text_from_pdf(pdf_file):

    text = ""

    try:

        with pdfplumber.open(pdf_file) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

    except Exception as e:

        return f"Error reading PDF file: {e}"

    return text


# ==========================================
# EXTRACT TEXT FROM DOCX
# ==========================================

def extract_text_from_docx(docx_file):

    text = ""

    try:

        document = Document(docx_file)

        for para in document.paragraphs:

            text += para.text + "\n"

    except Exception as e:

        return f"Error reading DOCX file: {e}"

    return text


# ==========================================
# EXTRACT TEXT FROM TXT
# ==========================================

def extract_text_from_txt(txt_file):

    try:

        text = txt_file.read().decode("utf-8")

        return text

    except Exception as e:

        return f"Error reading TXT file: {e}"


# ==========================================
# MAIN FILE HANDLER
# ==========================================

def extract_resume_text(uploaded_file):

    file_name = uploaded_file.name.lower()

    if file_name.endswith(".pdf"):

        return extract_text_from_pdf(uploaded_file)

    elif file_name.endswith(".docx"):

        return extract_text_from_docx(uploaded_file)

    elif file_name.endswith(".txt"):

        return extract_text_from_txt(uploaded_file)

    else:

        return "Unsupported file format"