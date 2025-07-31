import os
import streamlit as st
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

#using groq since its free
client = Groq(api_key=os.getenv("GROQ_API_KEY")) 

def generate_response(family_conflict_text, user_question):
    """
    Takes a conflict description + user question,
    sends to Groq LLM and returns advice as a counsellor.
    """
    prompt = f"""
    You are a kind and empathetic family counsellor.
    Below is a description of a family conflict:

    {family_conflict_text}

    The user has this question: "{user_question}"

    Provide practical advice, emotional support,
    and constructive ways to resolve the conflict.
    Keep the tone warm, professional, and understanding.
    """

    response = client.chat.completions.create(
        model="llama3-70b-8192",  # Can be changed to other Groq-supported models
        messages=[{"role": "system", "content": "You are a family counsellor."},
                  {"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=500
    )

    return response.choices[0].message["content"]
