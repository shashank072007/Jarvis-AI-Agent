# Jarvis AI Agent 🤖

A Python-based AI voice assistant inspired by JARVIS from *Iron Man*.

The project uses **LiveKit, Gemini, and other AI tools** to create an interactive voice-based assistant capable of understanding user input and performing different tasks.

## 🚀 Features

* 🎙️ Voice-based interaction
* 🤖 AI-powered conversational responses
* 🧠 Gemini integration
* 🔧 Custom tools and functions
* 🔐 Environment-variable based configuration
* 🐍 Built using Python

## 🛠️ Technologies Used

* Python
* LiveKit
* Google Gemini
* Python-dotenv
* AI/LLM tools

## 📁 Project Structure

```text
JarvisAgent/
│
├── agent.py
├── prompts.py
├── tools.py
├── requirements.txt
├── .gitignore
└── .env
```

### File Description

* `agent.py` — Main application/agent logic
* `prompts.py` — AI prompts and instructions
* `tools.py` — Custom tools used by the agent
* `requirements.txt` — Python dependencies
* `.gitignore` — Files excluded from Git
* `.env` — API keys and environment variables

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/shashank072007/Jarvis-AI-Agent.git
```

Move into the project directory:

```bash
cd Jarvis-AI-Agent
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the project directory and add the required API keys and configuration values.

**Do not upload your `.env` file to GitHub.**

The `.gitignore` file is configured to keep it private.

## ▶️ Running the Project

After activating the virtual environment and configuring the required environment variables, run:

```bash
python agent.py
```

## 🔮 Future Improvements

* Add more useful tools and functions
* Improve natural language understanding
* Add additional automation capabilities
* Improve voice interaction
* Add more integrations
* Develop a more advanced user interface

## 👨‍💻 Author

**Shashank**

Built as a learning project while exploring Python, AI agents, APIs, and modern AI development.
