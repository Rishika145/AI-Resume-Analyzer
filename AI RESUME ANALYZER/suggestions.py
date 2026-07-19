def generate_suggestions(score, missing_skills):

    suggestions = []

    if score < 50:
        suggestions.append("Your resume has a low ATS match. Add more keywords from the job description.")
    elif score < 75:
        suggestions.append("Your resume has a moderate ATS score. Consider improving your projects and technical skills.")
    else:
        suggestions.append("Excellent ATS score! Your resume is well matched to the job description.")

    if missing_skills:
        suggestions.append(
            "Consider adding these skills if you have them: "
            + ", ".join(missing_skills[:10])
        )

    suggestions.append("Use action verbs such as Developed, Designed, Implemented, and Optimized.")
    suggestions.append("Include measurable achievements (for example, 'Improved accuracy by 20%').")
    suggestions.append("Keep your resume concise and ATS-friendly.")

    return suggestions