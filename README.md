# YouTube AI Assistant Chrome Extension

A Chrome extension that uses AI to answer questions about YouTube video content using RAG (Retrieval Augmented Generation) with Mistral AI.

## Features

- 🤖 AI-powered Q&A about YouTube videos
- 📺 Automatic transcript extraction
- 💬 Chat-like interface
- 🎯 Context-aware responses using RAG
- ⚡ Real-time processing

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript (Chrome Extension)
- **Backend**: FastAPI (Python)
- **AI Model**: Mistral AI
- **Libraries**: 
  - youtube-transcript-api
  - requests
  - uvicorn

## Installation

### Prerequisites

1. Install [Ollama](https://ollama.ai/)
2. Pull Mistral model:
   ```bash
   ollama pull mistral
   ```

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/KUNDAN1334/YT_SCAN.git
   cd YT_SCAN
   ```

2. Install Python dependencies:
   ```bash
   pip install fastapi uvicorn youtube-transcript-api requests
   ```

3. Start the backend server:
   ```bash
   cd backend
   uvicorn main:app --reload
   ```

### Chrome Extension Setup

1. Open Chrome and go to `chrome://extensions/`
2. Enable "Developer mode"
3. Click "Load unpacked"
4. Select the project root directory (YT_SCAN)

## Usage

1. Make sure Ollama is running with Mistral model
2. Start the FastAPI backend server
3. Open the Chrome extension
4. Paste a YouTube URL
5. Click "Load Video"
6. Ask questions about the video content

## Project Structure

```
YT_SCAN/
├── backend/
│   ├── main.py              # FastAPI server
│   ├── transcript_handler.py # YouTube transcript extraction
│   └── llama_chat.py        # Mistral AI integration
├── popup.html               # Extension popup UI
├── popup.js                 # Frontend JavaScript
├── style.css               # Styling
├── manifest.json           # Extension manifest
└── README.md
```

## Configuration

The AI model is configured in `backend/llama_chat.py`. To use Mistral:

```python
response = requests.post(
    'http://localhost:11434/api/generate',
    json={
        "model": "mistral",  # Using Mistral model
        "prompt": prompt,
        "stream": False
    }
)
```

## API Endpoints

- `POST /ask` - Submit question about YouTube video
- `GET /` - Health check

## Model Performance

Mistral offers:
- ✅ Fast response times
- ✅ High-quality text generation
- ✅ Good context understanding
- ✅ Efficient resource usage

## Troubleshooting

1. **Model not found**: Make sure Mistral is pulled with `ollama pull mistral`
2. **Connection error**: Ensure Ollama is running on `http://localhost:11434`
3. **Transcript unavailable**: Some videos may not have transcripts available

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License

## Acknowledgments

- [Ollama](https://ollama.ai/) for local AI model hosting
- [Mistral AI](https://mistral.ai/) for the language model
- YouTube Transcript API for transcript extraction
```

Also, you should update your `llama_chat.py` file to use Mistral instead of LLaMA2:

```python:backend/llama_chat.py
import requests

def generate_answer(context, question):
    prompt = f"""You are an AI assistant. Use the given context to answer the user's question.

Context:
{context}

Question:
{question}

Answer:"""

    response = requests.post(
        'http://localhost:11434/api/generate',
        json={
            "model": "mistral",  # Changed from "llama2" to "mistral"
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()
    return data['response'].strip()
```

Now commit these changes:

```bash
git add .
```

```bash
git commit -m "Update to use Mistral AI model instead of LLaMA2"
```

```bash
git push
