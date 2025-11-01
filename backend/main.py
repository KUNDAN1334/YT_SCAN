from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
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

# Request validation model
class QuestionRequest(BaseModel):
    video_url: str
    question: str

@app.post("/ask")
async def ask_question(request: QuestionRequest):
    try:
        video_url = request.video_url
        question = request.question
        
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
        
        return {"answer": answer, "success": True}
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error processing request: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "YouTube Q&A API is running"}

@app.options("/ask")
async def options_ask():
    """Handle CORS preflight requests"""
    return {}
