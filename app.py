from unicodedata import category

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

        matched_schemes = check_eligibility(age, gender, occupation)

        session["name"] = name
        session["age"] = age
        session["gender"] = gender
        session["occupation"] = occupation
        session["income"] = income
        session["state"] = state
        session["category"] = category
        
        return redirect(url_for("recommendations"))
    
        return render_template(
            "recommendations.html",
            name=name,
            age=age,
            gender=gender,
            occupation=occupation,
            income=income,
            state=state,
            category=category,
            schemes=matched_schemes
        )
    return render_template("profile.html")




@app.route("/scheme/<name>")
def scheme_details(name):
    return render_template(
        "scheme_details.html",
        scheme_name=name
    )

@app.route("/recommendations")
def recommendations():

    return render_template(
        "recommendations.html",
        name=session.get("name"),
        age=session.get("age"),
        gender=session.get("gender"),
        occupation=session.get("occupation"),
        income=session.get("income"),
        state=session.get("state"),
        category=session.get("category")
    )


if __name__ == "__main__":
    app.run(debug=True)