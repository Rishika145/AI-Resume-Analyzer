def create_report(name, email, phone, skills, score, missing_skills, suggestions):

    report = f"""
=============================
      AI RESUME ANALYZER
=============================

Candidate Details
-----------------
Name : {name}
Email : {email}
Phone : {phone}

Extracted Skills
----------------
{', '.join(skills)}

ATS Score
---------
{score:.2f} %

Missing Skills
--------------
{', '.join(missing_skills)}

AI Suggestions
--------------
"""

    for s in suggestions:
        report += f"- {s}\n"

    return report