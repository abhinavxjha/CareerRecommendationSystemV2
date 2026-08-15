# 🚀 AI-Powered Career Recommendation Engine V2

<div align="center">

<strong>Find the careers that actually fit your skills, spot the gaps, and get a smarter roadmap to level up.</strong>

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](#-license)
[![Status](https://img.shields.io/badge/Status-Active-success)]()

[Overview](#-overview) • [Features](#-features) • [How It Works](#-how-it-works) • [Tech Stack](#-tech-stack) • [Installation](#-installation) • [Usage](#-usage) • [Project Structure](#-project-structure) • [Roadmap](#-future-improvements) • [License](#-license)

</div>

---

<a id="-overview"></a>
## 📖 Overview

This project is the upgraded, web-first version of a career guidance system that helps students and early-career professionals discover the best-fitting career paths based on their existing skills.

Instead of generic advice, it does something far more useful:

- compares your skill set with a curated database of careers
- scores how well you match each role
- identifies the exact skill gaps blocking your entry into the career
- suggests relevant courses and a step-by-step roadmap to improve
- lets you upload a resume to extract technical skills automatically

Built for real-world practicality, this version runs as a lightweight Flask backend with a fast single-page frontend, making it easy to use, easy to extend, and easy to deploy locally or on a small web server.

> 💡 The system works entirely on local JSON datasets — no external AI APIs or paid services are required for the core recommendation logic.

---

<a id="-features"></a>
## ✨ Features

### 🎯 Career Matching Engine
- Compares the user's skills against a catalog of career profiles
- Ranks careers by match score from strongest to weakest
- Surfaces the top career matches instantly

### 📉 Skill Gap Analysis
- Shows the exact missing skills for a chosen target career
- Highlights what you already have vs. what you still need
- Helps users focus on the right next learning priorities instead of guessing

### 🧠 Readiness Score
- Converts your skill overlap into an easy-to-understand readiness percentage
- Evaluates how close you are to the target role
- Supports decision-making with a clear score-based summary

### 📚 Course Recommendations
- Matches missing skills to courses in a structured catalog
- Returns relevant learning resources with labeled skill connections
- Makes the next action obvious and actionable

### 🛣️ Personalized Learning Roadmap
- Generates a roadmap based on the missing skills
- Organizes the next few months into a focused growth plan
- Keeps learning realistic and manageable instead of overwhelming

### 📄 Resume Skill Extraction
- Upload a PDF resume
- Extract text from the document
- Match key technical skills against the master skill dataset
- Auto-fill skill input with real resume content

### ⚡ Fast Web Experience
- Clean frontend for interactive skill input and analysis
- No heavy app setup required
- Designed to be simple, fast, and user-friendly

---

<a id="-how-it-works"></a>
## 🔄 How It Works

```text
Skill Input / Resume Upload
              ↓
Skill Normalization
              ↓
Career Match Scoring
              ↓
Gap Analysis
              ↓
Course + Roadmap Recommendations
              ↓
Career Insights Dashboard
```

The engine works like this:

1. User enters skills manually or uploads a resume.
2. Skills are normalized and cleaned.
3. Every career profile is scored against the user's skill list.
4. The most relevant careers are ranked by match percentage.
5. The target career's missing skills are identified.
6. Recommendations are generated for the learning path ahead.

This makes the whole process feel like a smart career advisor without the complexity of a full ML stack.

---

<a id="-tech-stack"></a>
## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Backend | Python, Flask |
| Frontend | HTML, CSS, JavaScript |
| Data Processing | JSON, Python standard libraries |
| PDF Parsing | pdfplumber |
| Environment | Python 3.10+ |

### Project Tech Snapshot
- Lightweight API-driven architecture
- Local JSON datasets for careers, skills, and course mapping
- Simple deployment model
- Minimal dependencies for easy setup

---

<a id="-installation"></a>
## ⚙️ Installation

### 1) Clone the repository

```bash
git clone https://github.com/yourusername/CareerRecommendationV2.git
cd CareerRecommendationV2
```

### 2) Create a virtual environment

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Run the app

```bash
python main.py
```

Then open:

```text
http://localhost:5000
```

> 🚀 The app is designed to run locally with no special deployment setup required.

---

<a id="-usage"></a>
## 🚀 Usage

1. Open the web app in your browser.
2. Enter your skills manually or upload a PDF resume.
3. Select a target career.
4. Click analyze.
5. Review:
   - top matching careers
   - skill gaps
   - readiness score
   - relevant courses
   - roadmap suggestions

This gives you a clean, practical way to answer:

> “What career fits me best, and what do I need to learn next?”

---

<a id="-project-structure"></a>
## 📁 Project Structure

```text
CareerRecommendationV2/
├── .gitignore
├── LICENSE
├── main.py
├── README.md
├── requirements.txt
├── data/
│   ├── career_info.json
│   ├── careers.json
│   ├── courses.json
│   └── skills.json
├── features/
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
├── modules/
│   └── helpers.py
└── .devcontainer/
    └── devcontainer.json
```

### Key files
- `main.py` — Flask backend and API routes
- `data/*.json` — career, skill, and course metadata
- `frontend/` — user interface
- `modules/helpers.py` — reusable helper logic

---

## 🧪 Why this version is stronger

This V2 version improves the original concept by shifting toward:

- a cleaner web app interface
- easier local execution
- a more maintainable file structure
- smoother resume parsing workflow
- a more modular project layout for future expansion

In short, V2 is more polished, more practical, and more ready for future upgrades.

---

<a id="-future-improvements"></a>
## 🔮 Future Improvements

- [ ] Add a smarter ML-based career prediction layer
- [ ] Build a conversational career mentor assistant
- [ ] Add resume score + profile quality analysis
- [ ] Add personalized internship recommendations
- [ ] Add downloadable PDF career reports
- [ ] Add user authentication and saved profiles
- [ ] Replace JSON storage with a database-backed architecture
- [ ] Add richer charts and analytics dashboards

---

## 👤 Author

**Abhinav Jha**

B.Tech Computer Science & Engineering  
Jaypee University of Information Technology, Solan

---

<a id="-license"></a>
## 📜 License

This project is licensed under the MIT License.

```text
MIT License

Copyright (c) 2026 Abhinav Jha

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

<div align="center">

Made with 💡, data, and a lot of career-plotting energy.

</div>
