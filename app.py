import streamlit as st
import PyPDF2
import docx2txt
import openai  # optional, for AI feedback

st.set_page_config(page_title="ResumeRanker AI", layout="centered")
st.title("📄 ResumeRanker AI")
st.write("Upload your resume and get **AI-powered feedback** instantly!")

uploaded_file = st.file_uploader("📤 Upload your resume", type=["pdf", "docx"])

def extract_text(file):
    if file.name.endswith(".pdf"):
        pdf_reader = PyPDF2.PdfReader(file)
        return "\n".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
    elif file.name.endswith(".docx"):
        return docx2txt.process(file)
    return ""

def basic_score(text):
    keywords = ["Python", "SQL", "Machine Learning", "Data Analysis", "Communication", "Leadership"]
    found = [kw for kw in keywords if kw.lower() in text.lower()]
    score = int((len(found) / len(keywords)) * 100)
    return score, found

if uploaded_file:
    resume_text = extract_text(uploaded_file)
    st.subheader("📝 Resume Text (First 1000 characters)")
    st.write(resume_text[:1000])

    score, matched_keywords = basic_score(resume_text)
    st.subheader("📊 Resume Score")
    st.write(f"Your resume scored **{score}%** based on key industry terms.")

    st.subheader("✅ Matched Keywords")
    st.write(", ".join(matched_keywords) if matched_keywords else "No key terms found.")

    st.info("Tip: Add more technical and soft skills to improve your score!")
