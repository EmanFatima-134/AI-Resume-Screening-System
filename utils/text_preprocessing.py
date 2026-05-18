# ==========================================
# NLP TEXT PREPROCESSING MODULE
# ==========================================

import re
import nltk

nltk.download('stopwords')
nltk.download('punkt_tab')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


# ==========================================
# STOPWORDS + LEMMATIZER
# ==========================================

stop_words = set(stopwords.words("english"))

lemmatizer = WordNetLemmatizer()


# ==========================================
# CLEAN TEXT FUNCTION
# ==========================================

def clean_text(text):

    # Lowercase

    text = text.lower()

    # Remove URLs

    text = re.sub(r"http\\S+", " ", text)

    # Remove emails

    text = re.sub(r"\\S+@\\S+", " ", text)

    # Remove special characters

    text = re.sub(r"[^a-zA-Z0-9 ]", " ", text)

    # Remove extra spaces

    text = re.sub(r"\\s+", " ", text)

    return text


# ==========================================
# TOKENIZATION + STOPWORD REMOVAL
# ==========================================

def preprocess_text(text):

    # Clean text

    text = clean_text(text)

    # Tokenization

    tokens = word_tokenize(text)

    # Remove stopwords + Lemmatization

    processed_tokens = []

    for word in tokens:

        if word not in stop_words and len(word) > 2:

            lemma = lemmatizer.lemmatize(word)

            processed_tokens.append(lemma)

    # Join final text

    processed_text = " ".join(processed_tokens)

    return processed_text