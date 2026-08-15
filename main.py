import json
from pathlib import Path

import pdfplumber
from flask import Flask, jsonify, request, send_from_directory


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
FRONTEND_DIR = BASE_DIR / "frontend"

app = Flask(__name__, static_folder=str(FRONTEND_DIR), static_url_path="")
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024


def load_json(filename: str):
    with (DATA_DIR / filename).open(encoding="utf-8") as file:
        return json.load(file)


CAREERS = load_json("careers.json")
COURSES = load_json("courses.json")
CAREER_INFO = load_json("career_info.json")
SKILLS_DATA = load_json("skills.json")
CAREERS_BY_NAME = {item["career"]: item["skills"] for item in CAREERS}
CAREER_INFO_BY_NAME = {item["career"]: item for item in CAREER_INFO}
ALL_SKILLS = [skill for group in SKILLS_DATA.values() for skill in group]


def normalise(value: str) -> str:
    return " ".join(value.strip().lower().split())


def unique_skills(skills: list[str]) -> list[str]:
    seen, result = set(), []
    for skill in skills:
        cleaned = str(skill).strip()
        if cleaned and normalise(cleaned) not in seen:
            seen.add(normalise(cleaned))
            result.append(cleaned)
    return result


def score_careers(user_skills: list[str]) -> list[dict]:
    user_set = {normalise(skill) for skill in user_skills}
    results = []
    for career, required in CAREERS_BY_NAME.items():
        matched = [skill for skill in required if normalise(skill) in user_set]
        score = round(100 * len(matched) / len(required), 2) if required else 0
        results.append({
            "career": career,
            "skills": required,
            "matched_skills": matched,
            "score": score,
        })
    return sorted(results, key=lambda item: item["score"], reverse=True)


def build_analysis(user_skills: list[str], target_career: str) -> dict:
    if target_career not in CAREERS_BY_NAME:
        raise ValueError("Please select a valid target career.")

    scores = score_careers(user_skills)
    target = next(item for item in scores if item["career"] == target_career)
    matched = {normalise(skill) for skill in target["matched_skills"]}
    missing = sorted((skill for skill in target["skills"] if normalise(skill) not in matched), key=str.lower)

    top_matches = [
        {"rank": rank, "career": item["career"], "score": item["score"]}
        for rank, item in enumerate((item for item in scores if item["score"] > 0), start=1)
    ][:5]

    insights = [{
        **item,
        **{key: value for key, value in CAREER_INFO_BY_NAME.get(item["career"], {}).items() if key != "career"}
    } for item in top_matches]

    missing_set = {normalise(skill) for skill in missing}
    courses = [course for course in COURSES if normalise(course["skill"]) in missing_set]

    return {
        "user_skills": user_skills,
        "target_career": target_career,
        "readiness_score": target["score"],
        "matched_skills": target["matched_skills"],
        "missing_skills": missing,
        "top_matches": top_matches,
        "best_match": top_matches[0] if top_matches else None,
        "career_insights": insights,
        "recommended_courses": courses,
        "roadmap": [{"month": month, "skill": skill} for month, skill in enumerate(missing[:5], start=1)],
    }


def skills_from_resume(resume) -> list[str]:
    text = ""
    with pdfplumber.open(resume) as pdf:
        for page in pdf.pages:
            text += (page.extract_text() or "") + "\n"
    lowered = text.lower()
    return unique_skills([skill for skill in ALL_SKILLS if normalise(skill) in lowered])


@app.get("/")
def index():
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.get("/api/careers")
def careers():
    return jsonify({"careers": sorted(CAREERS_BY_NAME)})


@app.post("/api/analyze")
def analyze():
    payload = request.get_json(silent=True) or {}
    skills = payload.get("skills", [])
    if not isinstance(skills, list):
        return jsonify({"error": "Skills must be sent as a list."}), 400
    skills = unique_skills(skills)
    if not skills:
        return jsonify({"error": "Enter at least one skill before analyzing."}), 400
    try:
        return jsonify(build_analysis(skills, payload.get("target_career", "")))
    except ValueError as error:
        return jsonify({"error": str(error)}), 400


@app.post("/api/resume-skills")
def resume_skills():
    resume = request.files.get("resume")
    if not resume or not resume.filename:
        return jsonify({"error": "Upload a PDF resume."}), 400
    if not resume.filename.lower().endswith(".pdf"):
        return jsonify({"error": "Only PDF resumes are supported."}), 400
    try:
        return jsonify({"skills": skills_from_resume(resume)})
    except Exception:
        return jsonify({"error": "Unable to read this PDF. Upload a valid text-based resume."}), 400


@app.errorhandler(413)
def file_too_large(_error):
    return jsonify({"error": "Resume size must be 10 MB or smaller."}), 413


if __name__ == "__main__":
    app.run(debug=True)
