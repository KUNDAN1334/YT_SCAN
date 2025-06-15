# YouTube AI Assistant Chrome Extension

A Chrome extension that uses AI to answer questions about YouTube video content using RAG (Retrieval Augmented Generation) with Groq's Llama AI.

## Features

- 🤖 AI-powered Q&A about YouTube videos
- 📺 Automatic transcript extraction
- 💬 Chat-like interface
- 🎯 Context-aware responses using RAG
- ⚡ Lightning-fast responses with Groq API
- 🔒 Secure API key management

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript (Chrome Extension)
- **Backend**: FastAPI (Python)
- **AI Model**: Llama 3.1 8B Instant (via Groq API)
- **Libraries**:
  - youtube-transcript-api
  - groq
  - tiktoken
  - python-dotenv
  - uvicorn
  - fastapi

## Installation

### Prerequisites

1. Get a free Groq API key from [console.groq.com](https://console.groq.com)
2. Python 3.8+ installed

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/KUNDAN1334/YT_SCAN.git
   cd YT_SCAN
   ```

2. Install Python dependencies:
   ```bash
   pip install fastapi uvicorn youtube-transcript-api groq tiktoken python-dotenv
   ```

3. Create a `.env` file in the project root:
   ```env
   GROQ_API_KEY=your-groq-api-key-here
   ```

4. Start the backend server:
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

1. Make sure your `.env` file contains your Groq API key
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
│   └── llama_chat.py        # Groq API integration
├── popup.html               # Extension popup UI
├── popup.js                 # Frontend JavaScript
├── style.css               # Styling
├── manifest.json           # Extension manifest
├── .env                    # Environment variables (API keys)
├── .gitignore              # Git ignore file
└── README.md
```

## Configuration

The AI model is configured in `backend/llama_chat.py` using Groq API:

```python
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_answer(context, question):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # Fast Llama model
        messages=[{"role": "user", "content": prompt}],
        max_tokens=800,
        temperature=0.1,
        stream=False
    )
    return response.choices[0].message.content.strip()
```

## API Endpoints

- `POST /ask` - Submit question about YouTube video
- `GET /` - Health check

## Model Performance

Groq's Llama 3.1 8B Instant offers:
- ⚡ Ultra-fast response times (1-3 seconds)
- 🎯 High-quality text generation
- 🧠 Excellent context understanding
- 💰 Free tier with generous limits
- 🔄 No local setup required

## Token Management

The extension automatically handles large video transcripts by:
- 📊 Counting tokens using tiktoken
- ✂️ Smart context truncation (keeps recent content)
- 🛡️ Preventing API limit errors
- 🎯 Maintaining answer quality

## Environment Variables

Create a `.env` file with:
```env
GROQ_API_KEY=your-actual-groq-api-key-here
```

**Important**: Never commit your `.env` file to version control!

## Troubleshooting

1. **API Key Error**: 
   - Check your `.env` file exists and contains valid Groq API key
   - Verify API key at [console.groq.com](https://console.groq.com)

2. **Token Limit Error**: 
   - The extension automatically truncates long transcripts
   - If issues persist, try shorter video segments

3. **Connection Error**: 
   - Ensure FastAPI server is running on `http://localhost:8000`
   - Check your internet connection for Groq API access

4. **Transcript Unavailable**: 
   - Some videos may not have transcripts available
   - Try videos with auto-generated captions

## Rate Limits

**Groq Free Tier:**
- 6,000 tokens per minute
- Automatic context truncation handles this
- Upgrade to Dev Tier for higher limits

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Security

- ✅ API keys stored in `.env` file
- ✅ `.env` file excluded from git
- ✅ No sensitive data in code
- ✅ Secure API communication

## License

MIT License

## Changelog

### v2.0.0
- ⚡ Switched from local Mistral to Groq API
- 🚀 10x faster response times
- 🔧 Added automatic token management
- 🔒 Improved security with environment variables
- 📊 Added response time monitoring

### v1.0.0
- 🎉 Initial release with local Mistral model

## Acknowledgments

- [Groq](https://groq.com/) for lightning-fast AI inference
- [Meta](https://ai.meta.com/) for the Llama model
- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api) for transcript extraction
- [FastAPI](https://fastapi.tiangolo.com/) for the backend framework
```

Now commit these changes:

```bash
git add .
```

```bash
git commit -m "Update README: Switch from Mistral to Groq API with Llama 3.1"
```

```bash
git push
