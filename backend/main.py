from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from transcript_handler import get_transcript, extract_video_id
from llama_chat import generate_answer

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/ask")
async def ask_question(request: dict):
    try:
        video_url = request.get("video_url")
        question = request.get("question")
        
        # Extract video ID
        video_id = extract_video_id(video_url)
        if not video_id:
            return {"error": "Invalid YouTube URL"}
        
        # Get transcript
        transcript = get_transcript(video_id)
        
        # Generate answer
        answer = generate_answer(transcript, question)
        
        return {"answer": answer}
        
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
async def root():
    return {"message": "YouTube Q&A API is running"}
