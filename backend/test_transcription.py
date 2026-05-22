from app.services.speech_service import transcribe_audio

audio_path = "audio/emergency.m4a"

text = transcribe_audio(audio_path)

print("\nTRANSCRIBED TEXT:\n")
print(text)