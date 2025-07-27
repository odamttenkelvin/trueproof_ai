from fastapi import APIRouter, UploadFile, File
import tempfile
from app.services.audio_analyzer import transcribe_audio, get_voice_embedding

router = APIRouter()

@router.post("/analyze/audio")
async def analyze_uploaded_audio(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    transcript = transcribe_audio(tmp_path)
    embedding = get_voice_embedding(tmp_path)

    return {
        "status": "ok",
        "transcription": transcript,
        "embedding_preview": embedding[:5]
    }