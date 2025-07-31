import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import cloudpickle
from sklearn.metrics import classification_report, confusion_matrix
from churn_agent_llm import generate_response

 

# App title
#st.set_page_config(page_title="Customer Churn Prediction", layout="wide")
st.title("📉 RAVI'S ISSUE")

# ✅ Clear pending input if flagged
if "pending_clear_input" in st.session_state:
    if st.session_state.pending_clear_input in st.session_state:
        st.session_state[st.session_state.pending_clear_input] = ""
    del st.session_state.pending_clear_input

 

 
    st.title("🤖 Chat with Conflict Counsellor")
    st.markdown("The agent will respond based on your doubts")

        

        # Ensure chat history dictionary
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = {}

   

     

      
            st.session_state.chat_history[customer_id] = []

            chat_placeholder = st.empty()

            def render_chat():
                with chat_placeholder.container():
                    for sender, msg in st.session_state.chat_history[customer_id]:
                        if sender == "user":
                            st.markdown(f"👤 **You:** {msg}")
                        else:
                            st.markdown(f"🤖 **Agent:** {msg}")

            render_chat()

            user_input_key = f"chat_input_{customer_id}"

            user_input = st.text_input(
                "💬 You (Ask the AI Counsellor your doubt regarding the conflict):",
                placeholder="Type here...",
                key=user_input_key
            )

            # ✅ Clear Chat Button below input
            if st.button("🗑️ Clear Chat"):
                st.session_state.pending_clear_input = user_input_key
                st.rerun()

            if user_input:
                with st.spinner("Generating response..."):
                    try:
                        customer_data_dict = customer_data.iloc[0].drop(["customerID"]).fillna("N/A").to_dict()
                        reply = generate_response(customer_data_dict, user_input)

                        st.session_state.chat_history[customer_id].append(("user", user_input))
                        st.session_state.chat_history[customer_id].append(("agent", reply))

                        render_chat()

                        # ✅ Mark input for clearing after rerun
                        st.session_state.pending_clear_input = user_input_key
                        st.rerun()

                    except Exception as e:
                        st.error(f"❌ LLM Error: {str(e)}")
 
