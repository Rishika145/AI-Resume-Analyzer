import re
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")


# Extract Name
def extract_name(text):
    doc = nlp(text)

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text

    # Fallback: first non-empty line
    lines = text.split("\n")
    for line in lines:
        line = line.strip()
        if len(line.split()) >= 2 and len(line) < 40:
            return line

    return "Not Found"


# Extract Email
def extract_email(text):
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    match = re.search(pattern, text)

    if match:
        return match.group(0)

    return "Not Found"


# Extract Phone Number
def extract_phone(text):
    patterns = [
        r"(\+91[\-\s]?)?[6-9]\d{9}",      # Indian numbers
        r"\+?\d[\d\s\-]{9,15}"            # International numbers
    ]

    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(0)

    return "Not Found"


