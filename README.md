# KoroHelper — AI Telegram Bot

A Telegram bot that lets you chat with a **self-hosted Llama 3.1** model. Messages are sent from Telegram to a local LLM running in [Ollama](https://ollama.com) via [LangChain](https://www.langchain.com), and the model's reply is sent back to the user. No paid APIs, and all model processing stays on your own machine.

## Tech stack

- **Python 3** with `asyncio`
- **[aiogram 3](https://docs.aiogram.dev)** — asynchronous Telegram Bot framework
- **[LangChain](https://python.langchain.com)** + `langchain-ollama` — connects the bot to the model
- **[Ollama](https://ollama.com)** — runs Llama 3.1 locally
- **python-dotenv** — loads the bot token from a `.env` file

## How it works

```
User (Telegram) ──► aiogram bot ──► LangChain (ChatOllama) ──► Ollama / Llama 3.1
       ▲                                                              │
       └──────────────────────── response ◄───────────────────────────┘
```

## Project structure

```
AI-Telegram-Bot/
├── handlers/
│   └── routes.py      # command handlers and LLM message handler
├── main.py            # bot entry point (loads token, starts polling)
├── requirements.txt   # Python dependencies
└── .env               # BOT_TOKEN (not committed)
```

## Bot commands

| Command  | Description                    |
|----------|--------------------------------|
| `/start` | Start the bot                  |
| `/help`  | Show the list of commands      |
| `/about` | Info about the bot             |
| *any text* | Sent to Llama 3.1, and the answer is returned |

## Getting started

### 1. Prerequisites

- Python 3.10+
- [Ollama](https://ollama.com/download) installed
- A Telegram bot token from [@BotFather](https://t.me/BotFather)

### 2. Download the model

```bash
ollama pull llama3.1
```

Make sure the Ollama server is running (`ollama serve` if it isn't started automatically).

### 3. Clone and install

```bash
git clone https://github.com/KOROYED/AI-Telegram-Bot.git
cd AI-Telegram-Bot

python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Configure

Create a `.env` file in the project root:

```env
BOT_TOKEN=your_telegram_bot_token_here
```

### 5. Run

```bash
python3 main.py
```

Open your bot in Telegram, send `/start`, and ask anything.

## Notes

- The model runs with `temperature=0.7`; change it in `handlers/routes.py`.
- Each message is handled independently (the bot does not keep conversation history).
- Response speed depends on your hardware; a GPU makes a big difference.