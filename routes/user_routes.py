from flask import Blueprint, render_template, request
from utils.eligibility_checker import check_eligibility

user_bp = Blueprint("user", __name__)


@user_bp.route("/profile", methods=["GET", "POST"])
def profile():

    if request.method == "POST":

        age = int(request.form.get("age"))
        gender = request.form.get("gender")
        occupation = request.form.get("occupation")

        recommended_schemes = check_eligibility(
            age,
            gender,
            occupation
        )

        return render_template(
            "recommendations.html",
            schemes=recommended_schemes
        )

    return render_template("profile.html")