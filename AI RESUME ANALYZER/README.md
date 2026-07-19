# 📄 AI Resume Analyzer

## 📌 Project Overview
AI Resume Analyzer is a Streamlit-based web application that analyzes resumes and compares them with a job description. It extracts candidate information, identifies skills, calculates an AI ATS score, detects missing skills, and provides resume improvement suggestions.

---

## ✨ Features

- 📄 Upload Resume (PDF)
- 👤 Extract Name, Email, and Phone Number
- 💻 Extract Technical Skills
- 🤖 AI ATS Score Calculation
- ❌ Missing Skills Detection
- 💡 AI Resume Suggestions
- 📥 Download Resume Analysis Report

---

## 🛠 Technologies Used

- Python
- Streamlit
- spaCy
- Sentence Transformers
- PDFPlumber
- Scikit-learn
- Torch
- Pandas
- NumPy

---

## 📂 Project Structure

```
AI_Resume_Analyzer/
│── app.py
│── parser.py
│── extractor.py
│── skills.py
│── ai_ats.py
│── matcher.py
│── suggestions.py
│── report.py
│── requirements.txt
│── README.md
│── .gitignore
└── screenshots/
```

---

## 🚀 Installation

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
streamlit run app.py
```

---

## 📸 Screenshots

Add screenshots inside the `screenshots` folder.

---

## 🔮 Future Enhancements

- Support DOCX resumes
- AI interview question generation
- Resume ranking
- Multi-language resume analysis
- Improved NLP models

---

