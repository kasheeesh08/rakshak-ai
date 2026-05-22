from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from app.api.audio_routes import router as audio_router

from app.services.nlp_service import classify_emergency
from app.services.preprocessing import normalize_hinglish


app = FastAPI()


app.add_middleware(

    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)


class EmergencyRequest(BaseModel):

    text: str


@app.get("/")
def root():

    return {
        "message":
        "Rakshak AI backend is running successfully"
    }


app.include_router(audio_router)


@app.post("/analyze-emergency")
def analyze_emergency(
    request: EmergencyRequest
):

    normalized_text = normalize_hinglish(
        request.text
    )

    classification = classify_emergency(
        normalized_text
    )

    return {

        "original_text":
            request.text,

        "normalized_text":
            normalized_text,

        "predicted_emergency":
            classification["label"],

        "confidence_score":
            classification["score"]
    }