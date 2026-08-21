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

You have access to real-time browser search.

For questions about current or recent information, use browser search
before answering.

This includes:

- Current Prime Minister
- Current Chief Ministers
- Current Deputy Chief Ministers
- Current Presidents
- Current Governors
- IAS officers
- Government officials
- Elections
- Election results
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

For current political and government questions:

1. Search the web for recent information.
2. Prefer official government websites.
3. Prefer Election Commission sources for elections.
4. Prefer recent and reliable news sources when appropriate.
5. Pay close attention to dates.
6. Never guess a current office holder.
7. If reliable sources disagree, explain the disagreement.
8. Do not use outdated knowledge when current web information is available.

For normal questions that do not require current information,
answer normally.

When browser search is used, provide citations or source links
when available.

Formatting rules:

- Give the direct answer first.
- Use headings when useful.
- Use bullet points for explanations.
- Use numbered lists for steps.
- Use tables when comparing information.
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

    st.error(
        f"❌ Groq API configuration error:\n\n{e}"
    )

    st.stop()


MODEL = "openai/gpt-oss-120b"


with st.sidebar:

    st.title("⚙️ Settings")

    st.markdown("---")

    st.info(
        "🤖 Model: GPT-OSS 120B"
    )

    st.caption(
        "🌐 Real-time browser search enabled"
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
    "AI Assistant with real-time web search"
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


    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ] + st.session_state.messages


    with st.chat_message("assistant"):

        with st.spinner(
            "Thinking..."
        ):

            try:

                response = client.chat.completions.create(

                    model=MODEL,

                    messages=messages,

                    tools=[
                        {
                            "type": "browser_search"
                        }
                    ],

                    max_completion_tokens=2048
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
                        "Please start a new chat or shorten the conversation."
                    )

                elif "model_not_found" in error_message:

                    st.error(
                        "❌ GPT-OSS 120B is not available "
                        "for this API key."
                    )

                else:

                    st.error(
                        "❌ Error while generating response:\n\n"
                        + error_message
                    )
