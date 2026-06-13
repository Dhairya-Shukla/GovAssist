from unicodedata import category
from data.schemes_data import schemes as all_schemes
from flask import Flask, render_template, request, redirect, url_for , session
from utils.eligibility_checker import check_eligibility

app = Flask(__name__)
app.secret_key = "govassist123"

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
        scheme=selected_scheme
    )

@app.route("/recommendations")
def recommendations():

    schemes = session.get("schemes", [])
    matched=[s for s in all_schemes if s["name"] in schemes]

    return render_template(
        "recommendations.html",
        name=session.get("name"),
        age=int(session.get("age", 0)),
        gender=session.get("gender"),
        occupation=session.get("occupation"),
        income=int(session.get("income", 0)),
        state=session.get("state"),
        category=session.get("category"),
        schemes=matched
    )


if __name__ == "__main__":
    app.run(debug=True)