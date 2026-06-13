from data.schemes_data import schemes

print("USING MY ELIGIBILITY CHECKER")
def check_eligibility(age, gender, occupation, income, state, category):

    print("CHECK_ELIGIBILITY RUNNING")

    age = int(age)
    income = int(income)

    eligible_schemes = []

    for scheme in schemes:

        eligible = True

        # Occupation Check
        if "occupation" in scheme:
            if (
                scheme["occupation"] != "Any"
                and scheme["occupation"].lower() != occupation.lower()
            ):
                eligible = False

        # Gender Check
        if "gender" in scheme:
            if scheme["gender"].lower() != gender.lower():
                eligible = False

        # Category Check
        if "category" in scheme:
            if (
                scheme["category"] != "Any"
                and scheme["category"].lower() != category.lower()
            ):
                eligible = False

        # Income Check
        if "income_limit" in scheme:
            if (
                scheme["income_limit"] is not None
                and income > scheme["income_limit"]
            ):
                eligible = False

        # State Check
        if "state" in scheme:
            if (
                scheme["state"] != "All"
                and scheme["state"].lower() != state.lower()
            ):
                eligible = False

        if eligible:
            eligible_schemes.append(scheme["name"])
        

    return eligible_schemes