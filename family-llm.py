import os
import streamlit as st
from openai import OpenAI
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

#using groq since its free
client = Groq(api_key=os.getenv("GROQ_API_KEY")) 

def generate_response(customer_data_dict, user_message):
    """
    Generates a response from the AI agent based on customer data and user message.

    Args:
        customer_data_dict (dict): Dictionary of customer attributes.
        user_message (str): Message/question entered by the user.

    Returns:
        str: AI-generated reply.
    """
    prompt = f"""You are a customer support executive. You are given this customer's data:
{customer_data_dict}

The user asked:
"{user_message}"

Respond in 1 line or 2 but Keep it friendly, clear, and informative."""
 
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "You are a helpful customer retention AI agent."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
