from fastapi import APIRouter, UploadFile, File
import shutil

from app.services.speech_service import transcribe_audio
from app.services.preprocessing import normalize_hinglish
from app.services.nlp_service import classify_emergency


router = APIRouter()


@router.post("/analyze-audio-emergency")
async def analyze_audio_emergency(file: UploadFile = File(...)):

    audio_path = f"audio/{file.filename}"

    with open(audio_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    transcribed_text = transcribe_audio(audio_path)

    normalized_text = normalize_hinglish(transcribed_text)

    prediction = classify_emergency(normalized_text)

    return {
        "transcribed_text": transcribed_text,
        "normalized_text": normalized_text,
        "predicted_emergency": prediction["label"],
        "confidence_score": prediction["score"]
    }