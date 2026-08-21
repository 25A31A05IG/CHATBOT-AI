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
You are a reliable AI assistant with access to real-time web search.

CURRENT INFORMATION RULES:

For any question involving current or recent information, you MUST use web search before answering.

This includes:
- Current Prime Ministers
- Current Chief Ministers
- Current Presidents
- Government officials
- Elections and election results
- Current affairs
- Breaking news
- Recent events
- Current sports results
- Current company CEOs
- Current prices
- Current laws and policies
- Today's information
- This week's information
- 2026 events

For political and government questions:

1. Search for recent information.
2. Prefer authoritative government sources and Election Commission sources.
3. Cross-check important claims with reliable recent sources.
4. Pay close attention to dates.
5. Never rely only on your internal knowledge for current information.
6. Never guess a current office holder.
7. If sources disagree, explain the disagreement instead of guessing.

For current office-holder questions, verify:
- Person's name
- Position
- State or country
- Political party when relevant
- Date the person assumed office

For general questions that do not require current information, answer normally.

When web search is used, provide source citations or links when available.

Formatting rules:
- Give the direct answer first.
- Use headings when useful.
- Use bullet points for explanations.
- Use numbered lists for steps.
- Use tables for comparisons.
- Keep paragraphs short.
- Format programming code using code blocks.
"""

try:
    client = Groq(
        api_key=st.secrets["GROQ_API_KEY"],
        default_headers={
            "Groq-Model-Version": "latest"
        }
    )
except Exception as e:
    st.error(f"❌ Groq API configuration error: {e}")
    st.stop()

model = "groq/compound-mini"

with st.sidebar:

    st.title("⚙️ Settings")

    st.markdown("---")

    st.info("🤖 Model: Groq Compound Mini")

    st.caption("🌐 Real-time web search enabled")

    st.markdown("---")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")

    st.caption("🚀 Built with Groq + Streamlit")

st.title("🤖 AI Chatbot")

st.caption("Fast AI Assistant with real-time web search")

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

    recent_messages = st.session_state.messages[-10:]

    with st.chat_message("assistant"):

        with st.spinner("Thinking and checking current information..."):

            try:

                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {
                            "role": "system",
                            "content": SYSTEM_PROMPT
                        }
                    ] + recent_messages,
                    compound_custom={
                        "tools": {
                            "enabled_tools": [
                                "web_search",
                                "visit_website"
                            ]
                        }
                    },
                    max_completion_tokens=1024
                )

                reply = response.choices[0].message.content

                placeholder = st.empty()

                full_response = ""

                for chunk in reply.split(" "):

                    full_response += chunk + " "

                    time.sleep(0.015)

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

                error_message = str(e)

                if "429" in error_message:
                    st.error(
                        "⏳ Groq rate limit reached. "
                        "Please wait a few seconds and try again."
                    )
                else:
                    st.error(
                        f"❌ Error while generating response:\n\n{e}"
                    )
