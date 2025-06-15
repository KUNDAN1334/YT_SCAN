# YouTube AI Assistant Chrome Extension

A Chrome extension that uses AI to answer questions about YouTube video content using RAG (Retrieval Augmented Generation) with LLaMA2.

## Features

- 🤖 AI-powered Q&A about YouTube videos
- 📺 Automatic transcript extraction
- 💬 Chat-like interface
- 🎯 Context-aware responses using RAG
- ⚡ Real-time processing

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript (Chrome Extension)
- **Backend**: FastAPI (Python)
- **AI Model**: LLaMA2 via Ollama
- **Libraries**: 
  - youtube-transcript-api
  - requests
  - uvicorn

## Installation

### Prerequisites

1. Install [Ollama](https://ollama.ai/)
2. Pull LLaMA2 model:
   ```bash
   ollama pull llama2
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

1. Make sure Ollama is running with LLaMA2 model
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
│   └── llama_chat.py        # LLaMA2 integration
├── popup.html               # Extension popup UI
├── popup.js                 # Frontend JavaScript
├── style.css               # Styling
├── manifest.json           # Extension manifest
└── README.md
```

## API Endpoints

- `POST /ask` - Submit question about YouTube video
- `GET /` - Health check

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License
```

Add the README to git:

```bash
git add README.md
```

```bash
git commit -m "Add README.md with project documentation"
```

```bash
git push
