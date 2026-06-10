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
        income = request.form.get("income")
        category = request.form.get("category")
        print(name, age, income, category)
        return redirect(url_for("recommendations"))
    return render_template("profile.html")

@app.route("/recommendations")
def recommendations():
    schemes = [
        "PM Scholarship Scheme",
        "PM Awas Yojana",
        "Startup India Scheme"
    ]
    return render_template("recommendations.html", schemes=schemes)

@app.route("/scheme/<name>")
def scheme_details(name):
    return render_template("scheme_details.html", scheme_name=name)

if __name__ == "__main__":
    app.run(debug=True)