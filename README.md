# GovAssist

**Smart Government Scheme Recommendation System**

GovAssist helps Indian citizens discover government welfare schemes they're actually eligible for. Instead of manually searching through hundreds of scattered scheme websites, users fill out a short profile, and GovAssist instantly matches them against a curated database of 198+ central government schemes — complete with AI-generated personalized explanations of why each scheme fits them.

---

## Problem Statement

India has hundreds of government welfare schemes spanning agriculture, education, healthcare, employment, and social security — but most citizens don't know which ones they qualify for. Information is scattered across dozens of ministry websites, eligibility criteria are confusing, and there's no single place to check "what am I actually eligible for?"

## Our Solution

GovAssist is a web application where users enter basic profile details (age, gender, occupation, income, state, social category), and the system:

1. Matches their profile against a database of 198+ real government schemes
2. Displays matched schemes with full details — benefits, eligibility criteria, and required documents
3. Uses Google's Gemini AI to generate a personalized summary explaining the best-matched scheme and next steps
4. Lets users explore individual scheme details on demand

## Key Features

- **Profile-based eligibility matching** across occupation, gender, income, state, and social category (General/SC/ST/OBC/EWS)
- **198+ government schemes** covering farmers, students, pregnant women, laborers, business owners, government/private employees, self-employed individuals, and senior citizens
- **AI-powered recommendations** using Gemini API to generate a natural-language summary of the best scheme match and reasoning
- **Detailed scheme pages** with overview, benefits, eligibility rules, and required documents for every scheme
- **Session-based flow** so users don't need to re-enter data while browsing recommendations and scheme details
- **Search functionality** to filter schemes on the recommendations page

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, Bootstrap 5
- **AI Integration:** Google Gemini API (`google-genai` SDK)
- **Data:** Custom-curated JSON-style scheme database (Python)
- **Session Management:** Flask sessions

## Project Structure
GovAssist/

├── app.py                      # Main Flask application & routes

├── config.py                   # Configuration settings

├── data/

│   └── schemes_data.py         # 198+ government scheme records

├── routes/

│   ├── scheme_routes.py        # Scheme-related blueprint routes

│   └── user_routes.py          # User-related blueprint routes

├── utils/

│   ├── eligibility_checker.py  # Core matching/filtering logic

│   └── gemini_helper.py        # Gemini AI integration

├── templates/

│   ├── index.html

│   ├── profile.html

│   ├── recommendations.html

│   └── scheme_details.html

├── static/

│   ├── style.css

│   ├── script.js

└── requirements.txt

## How It Works

1. User visits the homepage and navigates to their **Profile** page
2. They fill in their age, gender, occupation, income, state, and category
3. On submission, `eligibility_checker.py` filters the full scheme database against their profile
4. Matched schemes are stored in the session and the user is redirected to **Recommendations**
5. The recommendations page calls the Gemini API with the user's profile and matched scheme names to generate a personalized AI summary
6. Users can click **View Details** on any scheme to see its full overview, benefits, eligibility, and required documents

## Getting Started

### Prerequisites
- Python 3.10+
- A Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey)

### Installation

```bash
git clone <https://github.com/Dhairya-Shukla/GovAssist>
cd GovAssist
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### Environment Setup

Create a `.env` file in the project root:
GEMINI_API_KEY=your_api_key_here

SECRET_KEY=govassist123

### Run the App

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

## Team

| Name | Role |
|---|---|
| **Dhairya Shukla** (Team Lead) | Backend Development — Flask routes, eligibility logic, Gemini AI integration |
| **Deepanshu Joshi** | Frontend Development — UI/UX, HTML/CSS templates |
| **Ayush Bhatt** | Scheme Database — Researched and structured the 198+ government scheme records |
| **Gyanvi Petwal** | Eligibility Logic & Testing — Refined matching rules and tested edge cases across user profiles |

## Future Scope

- Expand scheme database with state-specific schemes
- Add multilingual support for regional language users
- Integrate document upload and auto-eligibility verification
- Add a "save scheme" and application tracking feature
- SMS/WhatsApp notifications for new matching schemes

---

*Built for Elevate Hack Round — 24 Hours, Infinite Possibilities.*
Steps: