import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


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

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


if __name__ == "__main__":
    result = get_ai_recommendation(
        "Age 20, Student, Male, Uttarakhand",
        "NSP, INSPIRE Scholarship"
    )
    print(result)