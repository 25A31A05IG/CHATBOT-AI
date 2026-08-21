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
You are a professional AI assistant with access to real-time web information.

Your responsibilities:

- Answer questions accurately and clearly.
- Use web search when the user asks about current, recent, latest, today's, this week's, or time-sensitive information.
- Use web search when your knowledge may be outdated.
- For general questions that do not require current information, answer normally.
- Never pretend that outdated information is current.
- When web search is used, include relevant source links or citations when available.

Formatting Rules:
- Always answer in markdown format.
- Use headings when appropriate.
- Use bullet points for explanations.
- Use numbered lists for step-by-step answers.
- Keep paragraphs short.
- Avoid unnecessarily large blocks of text.
- Use tables when comparing things.
- Format programming code using proper code blocks.
- Give direct answers before providing additional explanation.
"""

try:
    client = Groq(
        api_key=st.secrets["GROQ_API_KEY"],
        default_headers={
            "Groq-Model-Version": "latest"
        }
    )

except Exception as e:
    st.error("❌ Groq API key is not configured correctly.")
    st.stop()

model = "groq/compound-mini"

with st.sidebar:

    st.title("⚙️ Settings")

    st.markdown("---")

    st.info("🤖 Model: Groq Compound Mini")

    st.caption(
        "🌐 Real-time web search is available automatically."
    )

    st.markdown("---")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")

    st.caption("🚀 Built with Groq + Streamlit")

st.title("🤖 AI Chatbot")

st.caption(
    "Fast AI Assistant with real-time web search"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

if len(st.session_state.messages) == 0:
    st.info(
        "👋 Hello! Ask me anything. "
        "I can also search the web for current information."
    )

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
                    max_completion_tokens=2048
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
