# OpenAI Agents Learn

A repository for learning, prototyping, and building intelligent agents using the `openai-agents` SDK.

---

## 🚀 Current Progress & Active Development

Our primary focus is currently on the **First Agent** (`first_agent/`), which serves as the main active development agent. 

### Key Achievements
1. **Chainlit Python UI Integration**: Integrated the agent runner with a modern, streaming web-based chat interface using [Chainlit](https://chainlit.io/).
2. **Session-Scoped Memory**: Configured advanced memory persistence using `AdvancedSQLiteSession` linked to Chainlit's unique `user_session.id`. This ensures that conversation context and agent memory are fully maintained across multiple user messages in the same session.

---

## 📂 Project Structure

```text
├── .chainlit/                  # Global Chainlit configurations
├── first_agent/                # Main development agent folder
│   ├── first_agent.py          # Core Agent definition & model setup
│   ├── first_agent_ui.py       # Chainlit UI wrapper with SQLite session memory
│   └── conversations.db        # SQLite database storing session histories
├── simple_agent/               # Basic agent implementation for quick tests
├── main.py                     # Synchronous CLI entrypoint
├── main_async.py               # Asynchronous CLI entrypoint with streaming
├── pyproject.toml              # Project dependencies and metadata
└── README.md                   # Project documentation
```

---

## 🛠️ Getting Started

### Prerequisites
Make sure you have Python 3.12+ and [uv](https://github.com/astral-sh/uv) installed.

### 1. Environment Configuration
Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your-api-key
MODEL_NAME=gpt-4o  # or another model of your choice
```

### 2. Run the Chainlit UI
To launch the main UI for the **First Agent**:
```powershell
cd first_agent
uv run python -m chainlit run first_agent_ui.py -w
```
This will start the development server (usually at `http://localhost:8000`) with auto-reload enabled.

---

## 📦 Dependencies
- `openai-agents >= 0.14.5`
- `chainlit >= 2.11.1`
