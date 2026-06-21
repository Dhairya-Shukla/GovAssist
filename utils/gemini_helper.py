import google.generativeai as genai

genai.configure(
    api_key="your_api_key_here"
)

model = genai.GenerativeModel("gemini-2.5-flash")


def get_ai_recommendation(profile, schemes):

    prompt = f"""
    User Profile:
    {profile}

    Recommended Schemes:
    {schemes}

    Act as a government scheme advisor.

    Return ONLY HTML using this format:

    <ul>
    <li><strong>Best Scheme:</strong> ...</li>
    <li><strong>Why It Matches:</strong> ...</li>
    <li><strong>Main Benefits:</strong> ...</li>
    <li><strong>What To Do Next:</strong> ...</li>
    </ul>

    Keep each point short.
    Do not use markdown.
    Do not use ```html.
    """

    response = model.generate_content(prompt)

    return response.text
print(
    get_ai_recommendation(
        "Age 20, Student, Male, Uttarakhand",
        "NSP, INSPIRE Scholarship"
    )
)