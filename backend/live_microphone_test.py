import sounddevice as sd
from scipy.io.wavfile import write
import wavio

from app.services.speech_service import transcribe_audio
from app.services.preprocessing import normalize_hinglish
from app.services.nlp_service import classify_emergency
from app.services.hybrid_classifier import keyword_boost


duration = 5
sample_rate = 44100

print("Recording started... Speak now.")

recording = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1
)

sd.wait()

print("Recording complete.")

audio_path = "live_recording.wav"

write(audio_path, sample_rate, recording)

print("Transcribing audio...")

transcribed_text = transcribe_audio(audio_path)

print("\nTRANSCRIBED:")
print(transcribed_text)

normalized_text = normalize_hinglish(transcribed_text)

prediction = classify_emergency(normalized_text)

keyword_result = keyword_boost(normalized_text)

final_prediction = prediction["label"]

if prediction["score"] < 0.6:
    final_prediction = keyword_result["keyword_prediction"]

print("\nFINAL EMERGENCY DETECTION:")
print(final_prediction)