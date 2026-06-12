from flask import Blueprint, render_template, request
from data.schemes_data import schemes

scheme_bp = Blueprint("scheme", __name__)


@scheme_bp.route("/recommendations", methods=["GET", "POST"])
def recommendations():

    return render_template(
        "recommendations.html",
        schemes=schemes
    )


@scheme_bp.route("/scheme/<scheme_name>")
def scheme_details(scheme_name):

    selected_scheme = None

    for scheme in schemes:
        if scheme["name"] == scheme_name:
            selected_scheme = scheme
            break

    return render_template(
        "scheme_details.html",
        scheme=selected_scheme
    )