# Local Ollama Chat

A minimal terminal chat program that sends a running conversation to a locally served Ollama model. The current script selects `qwen2.5:7b` and keeps the conversation history for the current run.

## Requirements

- Python 3
- Ollama installed and running
- The `qwen2.5:7b` model available locally

Install the Python dependency and run the script:

```bash
pip install -r requirements.txt
python main.py
```

Enter `exit` to end the conversation.
