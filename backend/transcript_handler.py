from youtube_transcript_api import YouTubeTranscriptApi
import re

def extract_video_id(url):
    """Extract video ID from YouTube URL"""
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([^&\n?#]+)',
        r'youtube\.com\/watch\?.*v=([^&\n?#]+)'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

def get_transcript(video_id):
    """Get transcript for a YouTube video"""
    try:
        # Try multiple language codes
        language_codes = ['en', 'en-US', 'en-GB']
        
        for lang_code in language_codes:
            try:
                transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang_code])
                transcript_text = ' '.join([item['text'] for item in transcript_list])
                return transcript_text
            except:
                continue
        
        # If specific language codes fail, try getting any available transcript
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = ' '.join([item['text'] for item in transcript_list])
        return transcript_text
        
    except Exception as e:
        raise Exception(f"Could not retrieve transcript: {str(e)}")
