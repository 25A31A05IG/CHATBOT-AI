# 🤖 Chatbot AI

An intelligent conversational AI chatbot built with **Python, Streamlit, and Groq API**. The application uses **OpenAI GPT-OSS 120B** through Groq and supports **real-time browser search** for current and recent information.

🚀 Click here to open my App: https://rameshchatbotai.streamlit.app/

## 📌 Overview

Chatbot AI is a Generative AI-based web application designed to provide natural-language conversations between users and an AI assistant.

The application accepts user questions or messages, sends them to a Large Language Model through the Groq API, and displays the generated response through an interactive Streamlit chat interface.

The chatbot also supports **real-time browser search**, allowing it to retrieve updated information for questions related to current affairs, government officials, elections, recent events, and other time-sensitive topics.

The project demonstrates the practical integration of **Generative AI, Large Language Models, API integration, browser search, conversational AI, prompt engineering, and web application development**.

---

## ✨ Features

- 🤖 AI-powered conversational chatbot
- 💬 Natural-language interaction
- ⚡ Fast AI response generation
- 🧠 Conversation-based interaction
- 🌐 Real-time browser search
- 📰 Current and recent information retrieval
- 🔎 Web-based information verification
- 🔌 Groq API integration
- 🧠 OpenAI GPT-OSS 120B model
- 📝 Markdown-formatted responses
- ⌨️ Typing animation
- 🗑️ Clear chat functionality
- 🔐 Secure API key management
- ⚠️ API error handling
- 📱 Simple and user-friendly interface
- 🚀 Easy to run and deploy

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application and UI |
| Groq API | AI model API integration |
| GPT-OSS 120B | Large Language Model |
| Browser Search | Real-time information retrieval |
| HTML/CSS | UI customization |
| GitHub | Source code management |
| Streamlit Cloud | Application deployment |

---

## 🏗️ Project Architecture

```text
                ┌──────────────────┐
                │      User        │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │  Streamlit UI    │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │   Python App     │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │    Groq API      │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │  GPT-OSS 120B    │
                └────────┬─────────┘
                         │
                  ┌──────┴───────┐
                  │              │
                  ▼              ▼
          ┌──────────────┐ ┌───────────────┐
          │    Model     │ │ Browser Search│
          │   Knowledge  │ │ Real-Time Data│
          └──────┬───────┘ └───────┬───────┘
                 │                 │
                 └────────┬────────┘
                          ▼
                 ┌──────────────────┐
                 │  AI Generated    │
                 │    Response      │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │   Streamlit UI   │
                 └──────────────────┘
```

---

## 📂 Project Structure

```text
chatbot-ai/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
└── .streamlit/
    └── secrets.toml
```

### `app.py`

Contains the main chatbot application, Streamlit interface, Groq API integration, GPT-OSS 120B configuration, browser search functionality, conversation handling, typing animation, and error handling.

### `requirements.txt`

Contains all Python packages required to run the project.

### `.streamlit/secrets.toml`

Stores sensitive configuration such as the Groq API key securely.

> ⚠️ Never upload `secrets.toml` containing your API key to GitHub.

### `.gitignore`

Prevents sensitive and unnecessary files from being committed to the repository.

### `README.md`

Contains the project overview, features, technologies, installation instructions, architecture, and documentation.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/25A31A05IG/CHATBOT-AI.git
```

### 2. Open the Project

```bash
cd CHATBOT-AI
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/macOS

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 API Configuration

The application uses the Groq API to access the GPT-OSS 120B model.

For local development, create:

```text
.streamlit/secrets.toml
```

Add:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

Replace the value with your actual Groq API key.

### Important

Do not share your API key publicly.

Make sure the secret file is not uploaded to GitHub.

Recommended `.gitignore` entries:

```text
.streamlit/secrets.toml
venv/
__pycache__/
.env
```

---

## ▶️ Running the Application

Run the following command:

```bash
streamlit run app.py
```

The application will start locally and Streamlit will provide a URL similar to:

```text
http://localhost:8501
```

Open the URL in your browser to use the chatbot.

---

## 💬 How It Works

The chatbot follows these steps:

```text
User enters a message
        ↓
Streamlit receives the message
        ↓
Python processes the input
        ↓
Conversation context is prepared
        ↓
Request is sent to Groq API
        ↓
GPT-OSS 120B processes the request
        ↓
Model determines whether browser search is useful
        ↓
Browser Search retrieves current information
        ↓
AI generates the final response
        ↓
Response is returned to the application
        ↓
Typing animation displays the response
        ↓
Response is stored in conversation history
```

---

## 🌐 Real-Time Web Search

One of the main features of the chatbot is its ability to retrieve current information using browser search.

This is useful because Large Language Models have a knowledge cutoff and may not know about events that occurred after their training data.

The chatbot can use browser search for questions such as:

- Who is the current Prime Minister of India?
- Who is the current Chief Minister of Andhra Pradesh?
- Who is the current Deputy Chief Minister of Andhra Pradesh?
- Who is the current Chief Minister of Tamil Nadu?
- What are the current affairs in India?
- What happened recently in India?

For time-sensitive questions, the model can retrieve information from the web instead of relying only on its built-in knowledge.

The system prompt also instructs the chatbot to:

- Search for recent information
- Prefer official government sources
- Prefer Election Commission sources for elections
- Pay attention to dates
- Avoid guessing current office holders
- Consider disagreements between sources
- Use recent information when available

---

## 🧠 Conversation Context

The chatbot maintains conversation history using Streamlit session state.

This allows users to ask follow-up questions without repeating the previous context.

### Example

**User:**

```text
Who is the Prime Minister of India?
```

**Chatbot:**

```text
The Prime Minister of India is ...
```

**User:**

```text
What political party does he belong to?
```

The chatbot can use the previous conversation to understand what "he" refers to.

---

## 🧪 Example

### User

```text
What is Artificial Intelligence?
```

### Chatbot

```text
Artificial Intelligence is a field of computer science
that focuses on creating systems capable of performing
tasks that normally require human intelligence.

Examples include:

- Machine Learning
- Natural Language Processing
- Computer Vision
- Robotics
```

Users can continue the conversation by entering additional questions.

---

## 🌐 Current Information Example

### User

```text
Who is the current Chief Minister of Andhra Pradesh?
```

### Processing

```text
User Question
      ↓
GPT-OSS 120B
      ↓
Browser Search
      ↓
Recent Web Information
      ↓
AI Verification
      ↓
Final Answer
```

This allows the chatbot to provide information that may have changed after the model's original training data.

---

## 🔒 Security

The project follows basic security practices:

- API keys are stored using Streamlit Secrets.
- Sensitive secret files are excluded from Git.
- API credentials are not hard-coded into the source code.
- Sensitive information should not be displayed in application logs.
- The Groq API key should never be shared publicly.

---

## ⚠️ Limitations

- Requires an active internet connection for browser search.
- Depends on the availability of the Groq API.
- API usage may be subject to rate limits.
- AI-generated responses may occasionally contain inaccurate information.
- Search results may sometimes contain outdated or conflicting information.
- Conversation history is limited by the model's context window.
- The chatbot should not be treated as an authoritative source for critical decisions.
- Real-time search depends on the availability and quality of web sources.

---

## 🚀 Future Enhancements

The project can be extended with:

- 🎙️ Voice input and output
- 📄 PDF/document question answering
- 🖼️ Image analysis
- 🔐 User authentication
- 💾 Persistent conversation storage
- 👤 Personalized AI assistants
- 📥 Conversation export
- 📱 Mobile application
- 🌍 Multi-language support
- 🧠 Automatic conversation summarization
- 🔍 Advanced source and citation display
- 🎨 Multiple UI themes
- 📊 Chat and usage analytics
- 📚 RAG-based document question answering

---

## 🎯 Learning Outcomes

Through this project, the following concepts are demonstrated:

- Python application development
- Generative AI
- Large Language Models
- GPT-OSS 120B
- Groq API integration
- Browser Search integration
- Prompt engineering
- Conversational AI
- Streamlit development
- Session state management
- API error handling
- Rate-limit handling
- API security
- Secrets management
- Git and GitHub
- Cloud deployment

---

## 📚 Documentation

For complete technical and academic documentation, create:

```text
documentation/PROJECT_DOCUMENTATION.md
```

The documentation can contain:

- Abstract
- Introduction
- Problem Statement
- Objectives
- Scope
- Proposed System
- System Architecture
- Technologies Used
- System Requirements
- Functional Requirements
- Non-Functional Requirements
- System Workflow
- Browser Search Integration
- Algorithm
- Implementation
- Testing
- Advantages
- Limitations
- Applications
- Future Enhancements
- Conclusion
- References

---

## ☁️ Deployment

The application is deployed using **Streamlit Community Cloud**.

🚀 Live Application:

https://rameshchatbotai.streamlit.app/

The deployment process includes:

1. Uploading the project to GitHub.
2. Connecting the repository to Streamlit Community Cloud.
3. Selecting `app.py` as the main application file.
4. Adding the `GROQ_API_KEY` through Streamlit Secrets.
5. Deploying the application.
6. Accessing the chatbot through the generated Streamlit URL.

---

## 👨‍💻 Author

**Ramesh Netheti**

B.Tech – Computer Science and Engineering

📧 Email: rameshnetheti2008@gmail.com

🔗 LinkedIn: https://www.linkedin.com/in/25a31a05ig/

💻 GitHub: https://github.com/25A31A05IG

---

## ⭐ Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.
