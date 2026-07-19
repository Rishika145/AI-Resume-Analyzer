import re

def find_missing_skills(resume_text, job_description):

    resume_words = set(re.findall(r'\b[a-zA-Z+#.]+\b', resume_text.lower()))
    job_words = set(re.findall(r'\b[a-zA-Z+#.]+\b', job_description.lower()))

    ignore = {
        "the","and","or","with","for","to","of","in","on",
        "a","an","is","are","will","looking","experience",
        "candidate","developer","engineer","years"
    }

    missing = sorted(list((job_words - resume_words) - ignore))

    return missing