# OpenAI Agents Learn

A repository for learning, prototyping, and building intelligent agents using the `openai-agents` SDK.

---

## 🚀 Current Progress & Active Development

We are building and testing multiple agents to explore the capabilities of the `openai-agents` SDK and [Chainlit](https://chainlit.io/).

### 1. First Agent (`first_agent/`)
* **Chainlit Python UI Integration**: Integrated the agent runner with a modern, streaming web-based chat interface using Chainlit.
* **Session-Scoped Memory**: Configured advanced memory persistence using `AdvancedSQLiteSession` linked to Chainlit's unique `user_session.id`. This ensures that conversation context and agent memory are fully maintained across multiple user messages in the same session.

### 2. Second Agent with Tools (`second_agent_tools/`)
* **OpenAI Agent Framework Tool Calling**: Demonstrates how to define and register tools/functions for the agent to call dynamically.
* **Chainlit Chat Message Tools Display**: Displays step-by-step tool execution and tool outputs directly in the Chainlit chat UI.

---

## 📂 Project Structure

```text
├── .chainlit/                  # Global Chainlit configurations
├── first_agent/                # Main development agent folder
│   ├── first_agent.py          # Core Agent definition & model setup
│   ├── first_agent_ui.py       # Chainlit UI wrapper with SQLite session memory
│   └── conversations.db        # SQLite database storing session histories
├── second_agent_tools/         # Second agent folder (Tool calling showcase)
│   ├── bank_agent.py           # Core Bank Agent definition & tool definitions
│   ├── bank_agent_ui.py        # Chainlit UI wrapper displaying tool calls
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

To launch the UI for the **Second Agent (Tools)**:
```powershell
cd second_agent_tools
uv run python -m chainlit run bank_agent_ui.py -w
```
This will start the development server (usually at `http://localhost:8000` or `http://localhost:8001`) with auto-reload enabled.

---

## 📦 Dependencies
- `openai-agents >= 0.14.5`
- `chainlit >= 2.11.1`
