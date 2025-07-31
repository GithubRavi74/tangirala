 # app.py
import streamlit as st
from counsellor_agent import generate_response

st.set_page_config(page_title="Family Counsellor", layout="centered")
st.title("💬 AI Family Counsellor")

# Pre-defined conflict description (you can modify or allow user input for this too)
family_conflict_text = """
John and his teenage son have frequent arguments about school performance and phone usage.
The son feels his father doesn't understand him, while John feels his son is irresponsible.
The family wants to rebuild trust and improve communication.
"""

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

chat_placeholder = st.empty()

def render_chat():
    with chat_placeholder.container():
        for sender, msg in st.session_state.chat_history:
            if sender == "user":
                st.markdown(f"👤 **You:** {msg}")
            else:
                st.markdown(f"🧑‍⚕️ **Counsellor:** {msg}")

render_chat()

# Input field
user_input = st.text_input("💬 Ask your question to the counsellor:", placeholder="Type your question here...")

# Clear Chat Button
if st.button("🗑️ Clear Chat"):
    st.session_state.chat_history = []
    chat_placeholder.empty()
    st.experimental_rerun()

# Process Input
if user_input:
    with st.spinner("Counsellor is thinking..."):
        try:
            reply = generate_response(family_conflict_text, user_input)

            # Save to history
            st.session_state.chat_history.append(("user", user_input))
            st.session_state.chat_history.append(("agent", reply))

            render_chat()

            # Clear input
            st.session_state.user_input_key = ""
            st.experimental_rerun()

        except Exception as e:
            st.error(f"❌ LLM Error: {str(e)}")
