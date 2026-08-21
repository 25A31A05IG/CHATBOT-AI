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
</style>
""", unsafe_allow_html=True)

SYSTEM_PROMPT = """
You are a reliable professional AI assistant.

For normal questions, answer using your knowledge.

For questions involving CURRENT or RECENT information,
the application may provide web-search results.

When web-search information is provided:

- Prefer recent information.
- Prefer official government sources for government questions.
- Prefer Election Commission sources for election questions.
- Pay attention to dates.
- Do not contradict reliable current sources using outdated knowledge.
- Do not guess current office holders.
- If sources disagree, explain the disagreement.

Formatting rules:

- Give the direct answer first.
- Use headings when useful.
- Use bullet points for explanations.
- Use numbered lists for steps.
- Use tables for comparisons.
- Keep paragraphs short.
- Format code using proper code blocks.
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


NORMAL_MODEL = "openai/gpt-oss-120b"
WEB_MODEL = "groq/compound-mini"


def needs_web_search(question):

    keywords = [
        "current",
        "currently",
        "latest",
        "today",
        "now",
        "recent",
        "this week",
        "this month",
        "2026",
        "news",
        "current affairs",
        "prime minister",
        "chief minister",
        "deputy chief minister",
        "president",
        "governor",
        "election",
        "elections",
        "election result",
        "minister",
        "ias officer",
        "collector",
        "who is the cm",
        "who is the pm"
    ]

    question_lower = question.lower()

    return any(
        keyword in question_lower
        for keyword in keywords
    )


with st.sidebar:

    st.title("⚙️ Settings")

    st.markdown("---")

    st.info(
        "🤖 AI Model: Groq"
    )

    st.caption(
        "🌐 Web search is automatically used "
        "for current-information questions."
    )

    st.markdown("---")

    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = []

        st.rerun()

    st.markdown("---")

    st.caption(
        "🚀 Built with Groq + Streamlit"
    )


st.title("🤖 AI Chatbot")

st.caption(
    "AI Assistant with real-time information support"
)


if "messages" not in st.session_state:

    st.session_state.messages = []


if len(st.session_state.messages) == 0:

    st.info(
        "👋 Hello! Ask me anything."
    )


for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(
            message["content"]
        )


prompt = st.chat_input(
    "Type your message here..."
)


if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):

        st.markdown(prompt)


    recent_messages = []

    for message in st.session_state.messages[-8:]:

        recent_messages.append(
            {
                "role": message["role"],
                "content": message["content"][:3000]
            }
        )


    use_web = needs_web_search(prompt)


    if use_web:

        model = WEB_MODEL

    else:

        model = NORMAL_MODEL


    with st.chat_message("assistant"):

        if use_web:

            status_text = (
                "🌐 Checking current information..."
            )

        else:

            status_text = "🤔 Thinking..."


        with st.spinner(status_text):

            try:

                if use_web:

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

                else:

                    response = client.chat.completions.create(

                        model=model,

                        messages=[
                            {
                                "role": "system",
                                "content": SYSTEM_PROMPT
                            }
                        ] + recent_messages,

                        temperature=0.7,

                        max_tokens=512
                    )


                reply = (
                    response
                    .choices[0]
                    .message
                    .content
                )


                placeholder = st.empty()

                full_response = ""


                for word in reply.split(" "):

                    full_response += (
                        word + " "
                    )

                    time.sleep(0.015)

                    placeholder.markdown(
                        full_response + "▌"
                    )


                placeholder.markdown(
                    full_response
                )


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

                elif "413" in error_message:

                    st.error(
                        "⚠️ The request was too large. "
                        "Please try a shorter question."
                    )

                elif "model_not_found" in error_message:

                    st.error(
                        "❌ The selected Groq model is "
                        "not available for this API key."
                    )

                elif "model_terms_required" in error_message:

                    st.error(
                        "❌ This Groq model requires "
                        "additional terms acceptance."
                    )

                else:

                    st.error(
                        "❌ Error while generating response:\n\n"
                        + error_message
                    )
