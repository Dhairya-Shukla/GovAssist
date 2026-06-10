from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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

        return render_template(
            "recommendations.html",
            name=name,
            age=age,
            gender=gender,
            occupation=occupation,
            income=income,
            state=state,
            category=category
        )

    return render_template("profile.html")


@app.route("/recommendations")
def recommendations():

    schemes = [
        "PM Scholarship Scheme",
        "PM Awas Yojana",
        "Startup India Scheme"
    ]

    return render_template(
        "recommendations.html",
        schemes=schemes
    )


@app.route("/scheme/<name>")
def scheme_details(name):
    return render_template(
        "scheme_details.html",
        scheme_name=name
    )


if __name__ == "__main__":
    app.run(debug=True)