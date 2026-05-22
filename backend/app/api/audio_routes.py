from fastapi import APIRouter, UploadFile, File
import shutil

from app.services.speech_service import transcribe_audio
from app.services.preprocessing import normalize_hinglish
from app.services.nlp_service import classify_emergency
from app.services.hybrid_classifier import keyword_boost
from app.services.location_service import extract_location
from app.services.severity_service import detect_severity


router = APIRouter()


@router.post("/analyze-audio-emergency")
async def analyze_audio_emergency(
    file: UploadFile = File(...)
):

    audio_path = f"audio/{file.filename}"

    with open(audio_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    transcribed_text = transcribe_audio(
        audio_path
    )

    normalized_text = normalize_hinglish(
        transcribed_text
    )

    prediction = classify_emergency(
        normalized_text
    )

    keyword_result = keyword_boost(
        normalized_text
    )

    final_prediction = prediction["label"]

    if prediction["score"] < 0.6:

        final_prediction = (
            keyword_result["keyword_prediction"]
        )

    detected_location = extract_location(
        transcribed_text
    )

    detected_severity = detect_severity(
        transcribed_text
    )

    return {

        "transcribed_text": transcribed_text,

        "final_emergency_prediction":
            final_prediction,

        "detected_location":
            detected_location,

        "detected_severity":
            detected_severity
    }