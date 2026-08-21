import streamlit as st
from groq import Groq
import time

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.stChatMessage {
    padding: 12px;
    border-radius: 15px;
    margin-bottom: 10px;
}

.block-container {
    padding-top: 2rem;
}

.stTextInput > div > div > input {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

SYSTEM_PROMPT = """
You are a professional AI assistant.

Formatting Rules:
- Always answer in markdown format.
- Use headings for topics.
- Use bullet points for explanations.
- Use numbered lists for step-by-step answers.
- Keep paragraphs short.
- Avoid large blocks of text.
- Use tables when comparing things.
- Format code properly using code blocks.
"""

try:
    client = Groq(
        api_key=st.secrets["GROQ_API_KEY"]
    )
except Exception:
    st.error("❌ Groq API key is not configured correctly.")
    st.stop()

try:
    models_response = client.models.list()
    available_models = [model.id for model in models_response.data]

except Exception as e:
    st.error(f"❌ Could not retrieve Groq models: {e}")
    st.stop()

with st.sidebar:

    st.title("⚙️ Settings")

    st.markdown("---")

    if not available_models:
        st.error("No models are available for this API key.")
        st.stop()

    model = st.selectbox(
        "Choose AI Model",
        available_models
    )

    st.markdown("---")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")

    st.caption("🚀 Built with Groq + Streamlit")

st.title("🤖 AI Chatbot")

st.caption("Fast AI Assistant powered by Groq")

if "messages" not in st.session_state:
    st.session_state.messages = []

if len(st.session_state.messages) == 0:
    st.info("👋 Hello! Ask me anything.")

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Type your message here...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {
                            "role": "system",
                            "content": SYSTEM_PROMPT
                        }
                    ] + st.session_state.messages,
                    temperature=0.7,
                    max_tokens=512
                )

                reply = response.choices[0].message.content

                placeholder = st.empty()

                full_response = ""

                for chunk in reply.split(" "):

                    full_response += chunk + " "

                    time.sleep(0.02)

                    placeholder.markdown(
                        full_response + "▌"
                    )

                placeholder.markdown(full_response)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": full_response
                    }
                )

            except Exception as e:

                st.error(
                    f"❌ Error while generating response:\n\n{e}"
                )
