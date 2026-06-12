from data.schemes_data import schemes


def check_eligibility(age, gender, occupation):

    eligible_schemes = []

    for scheme in schemes:

        if "occupation" in scheme:
            if scheme["occupation"].lower() == occupation.lower() or scheme["occupation"] == "Any":
                eligible_schemes.append(scheme["name"])

        elif "gender" in scheme:
            if scheme["gender"].lower() == gender.lower():
                eligible_schemes.append(scheme["name"])

        else:
            eligible_schemes.append(scheme["name"])

    return eligible_schemes