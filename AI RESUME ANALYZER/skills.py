import spacy

nlp = spacy.load("en_core_web_sm")

SKILLS_DB = [
    "Python", "Java", "C", "C++", "JavaScript",
    "HTML", "CSS", "SQL", "MySQL", "MongoDB",
    "React", "Node.js", "Flask", "Django",
    "Machine Learning", "Deep Learning",
    "Artificial Intelligence", "NLP",
    "Data Science", "Pandas", "NumPy",
    "TensorFlow", "PyTorch",
    "Git", "GitHub",
    "Power BI", "Tableau", "Excel"
]

def extract_skills(text):
    doc = nlp(text.lower())

    found_skills = set()

    for token in doc:
        for skill in SKILLS_DB:
            if token.text == skill.lower():
                found_skills.add(skill)

    # Check multi-word skills
    lower_text = text.lower()
    for skill in SKILLS_DB:
        if " " in skill and skill.lower() in lower_text:
            found_skills.add(skill)

    return sorted(list(found_skills))