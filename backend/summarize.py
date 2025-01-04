# summarize.py
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.tokenize import sent_tokenize

# Ensure that punkt is downloaded for sentence tokenization
nltk.download('punkt')

# Initialize a global list to store summary history
summary_history = []

def summarize_document(text, num_sentences=3):
    # Tokenize the document into sentences
    sentences = sent_tokenize(text)
    
    # Vectorize the sentences using TF-IDF
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(sentences)
    
    # Rank sentences by their importance (TF-IDF scores)
    sentence_scores = tfidf_matrix.sum(axis=1).A1
    ranked_sentences = [sentences[i] for i in sentence_scores.argsort()[::-1]]
    
    # Get the summary
    summary = ' '.join(ranked_sentences[:num_sentences])
    
    # Add the original text and summary to the history
    summary_history.append((text, summary))
    
    return summary

def get_summary_history():
    return summary_history
