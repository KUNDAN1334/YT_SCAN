from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from transcript_handler import get_transcript, extract_video_id
from llama_chat import generate_answer

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ask")
async def ask_question(request: dict):
    try:
        video_url = request.get("video_url")
        question = request.get("question")
        
        if not video_url or not question:
            raise HTTPException(status_code=400, detail="Missing video_url or question")
        
        # Extract video ID
        video_id = extract_video_id(video_url)
        if not video_id:
            raise HTTPException(status_code=400, detail="Invalid YouTube URL")
        
        # Get transcript
        transcript = get_transcript(video_id)
        
        # Generate answer
        answer = generate_answer(transcript, question)
        
        return {"answer": answer}
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error processing request: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "YouTube Q&A API is running"}
