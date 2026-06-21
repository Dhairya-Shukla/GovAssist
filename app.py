from unicodedata import category
from utils.gemini_helper import get_ai_recommendation
from data.schemes_data import schemes as all_schemes
from flask import Flask, render_template, request, redirect, url_for , session
from utils.eligibility_checker import check_eligibility

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = app.config["SECRET_KEY"]

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/profile", methods=["GET", "POST"])
def profile():
    if request.method == "POST":

        name = request.form.get("name")
        age = request.form.get("age")
        gender = request.form.get("gender")
        occupation = request.form.get("occupation")
        income = request.form.get("income")
        state = request.form.get("state")
        category = request.form.get("category")

        matched_schemes = check_eligibility(
            age,
            gender,
            occupation,
            income,
            state,
            category
        )

        print(type(matched_schemes[0]))
        print(matched_schemes[0])

        session["name"] = name
        session["age"] = age
        session["gender"] = gender
        session["occupation"] = occupation
        session["income"] = income
        session["state"] = state
        session["category"] = category
        session["schemes"] = matched_schemes
        
        return redirect(url_for("recommendations"))
    
        
    return render_template("profile.html")




@app.route("/scheme/<name>")
def scheme_details(name):

    selected_scheme = None

    for scheme in all_schemes:
        if scheme["name"] == name:
            selected_scheme = scheme
            break

    return render_template(
    "scheme_details.html",
    scheme=selected_scheme,
    occupation=session.get("occupation"),
    category=session.get("category"),
    age=session.get("age"),
    gender=session.get("gender"),
    state=session.get("state")
   )

@app.route("/recommendations")
def recommendations():

    schemes = session.get("schemes", [])
    matched=[s for s in all_schemes if s["name"] in schemes]
    

    profile_info = f"""
    Age: {session.get('age')}
    Gender: {session.get('gender')}
    Occupation: {session.get('occupation')}
    Income: {session.get('income')}
    State: {session.get('state')}
    Category: {session.get('category')}"""
    scheme_names = [s["name"] for s in matched]
    ai_summary = get_ai_recommendation(
        profile_info,
        scheme_names
    )
    return render_template(
        "recommendations.html",
        name=session.get("name"),
        age=int(session.get("age", 0)),
        gender=session.get("gender"),
        occupation=session.get("occupation"),
        income=int(session.get("income", 0)),
        state=session.get("state"),
        category=session.get("category"),
        schemes=matched,
        ai_summary=ai_summary
    )


if __name__ == "__main__":
    app.run(debug=True)