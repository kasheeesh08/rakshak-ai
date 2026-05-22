from transformers import pipeline


pipe = pipeline(
    task="automatic-speech-recognition",
    model="openai/whisper-small"
)


def transcribe_audio(audio_path):

    result = pipe(
        audio_path,
        generate_kwargs={
            "language": "hindi"
        }
    )

    return result["text"]