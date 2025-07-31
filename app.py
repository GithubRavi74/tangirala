import streamlit as st
from counsellor_agent import generate_response

#from groq import Groq
#client = Groq(api_key=os.getenv("GROQ_API_KEY"))
st.set_page_config(page_title="Family Counsellor", layout="centered")
st.title("💬 Tangirala AI Family Counsellor")

# ✅ Initialize Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ✅ Render Chat with Chat Bubbles
for sender, msg in st.session_state.chat_history:
    if sender == "user":
        with st.chat_message("user", avatar="👤"):
            st.markdown(msg)
    else:
        with st.chat_message("assistant", avatar="🧑‍⚕️"):
            st.markdown(msg)

# ✅ Input box at bottom
user_input = st.chat_input("Type your question for the counsellor regarding Shankar Ravi Issue...")

# ✅ Clear Chat Button at top
if st.button("🗑️ Clear Chat"):
    st.session_state.chat_history = []
    st.rerun()

# ✅ Process User Input
if user_input:
    # Show user's message immediately
    st.session_state.chat_history.append(("user", user_input))
    with st.chat_message("user", avatar="👤"):
        st.markdown(user_input)

    with st.spinner("Counsellor is typing..."):
        try:
            reply = generate_response(user_input)

            # Add counsellor's reply
            st.session_state.chat_history.append(("assistant", reply))
            with st.chat_message("assistant", avatar="🧑‍⚕️"):
                st.markdown(reply)

        except Exception as e:
            st.error(f"❌ LLM Error: {str(e)}")
