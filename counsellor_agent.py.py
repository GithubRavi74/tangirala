# counsellor_agent.py
from groq import Groq

client = Groq(api_key="YOUR_GROQ_API_KEY")

def generate_response(user_question):
    """
    Takes only the user question and generates
    counsellor advice using a predefined conflict text.
    """

    family_conflict_text = """
    John and his teenage son have frequent arguments about school performance and phone usage.
    The son feels his father doesn't understand him, while John feels his son is irresponsible.
    The family wants to rebuild trust and improve communication.
    """

    prompt = f"""
    You are a kind and empathetic family counsellor.

    Below is the family conflict description:
    {family_conflict_text}

    The user has this question: "{user_question}"

    Give practical advice in 4-6 sentences with a warm, understanding tone.
    """

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "You are a compassionate family counsellor."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_tokens=400,
    )

    return response.choices[0].message["content"]
