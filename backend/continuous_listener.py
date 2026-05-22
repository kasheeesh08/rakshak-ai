import sounddevice as sd
from scipy.io.wavfile import write

from app.services.speech_service import transcribe_audio
from app.services.preprocessing import normalize_hinglish
from app.services.nlp_service import classify_emergency
from app.services.hybrid_classifier import keyword_boost
from app.services.wakeword_service import detect_wake_word
from app.services.vad_service import contains_speech

SAMPLERATE = 16000
DURATION = 5

def record_audio():

    print("\nListening for emergency speech...")

    audio = sd.rec(
        int(DURATION * SAMPLERATE),
        samplerate=SAMPLERATE,
        channels=1,
        dtype='int16'
    )

    sd.wait()

    write(
        "live_audio.wav",
        SAMPLERATE,
        audio
    )

    return "live_audio.wav"


while True:

    try:

        audio_path = record_audio()

        speech_detected = contains_speech(
        audio_path
        )

        if not speech_detected:

            print("\nNo speech activity detected.")
            print("\n" + "=" * 50)
            continue

        transcribed_text = transcribe_audio(audio_path)

        if not transcribed_text:

            print("\nNo speech detected.")
            print("\n" + "=" * 50)
            continue

        print("\nTRANSCRIBED:")
        print(transcribed_text)

        wake_detected = detect_wake_word(
            transcribed_text
        )

        if not wake_detected:

            print("\nNo wake word detected.")
            print("\n" + "=" * 50)
            continue

        normalized_text = normalize_hinglish(
            transcribed_text
        )

        transformer_prediction = classify_emergency(
            normalized_text
        )

        keyword_prediction = keyword_boost(
            normalized_text
        )

        final_prediction = (
            keyword_prediction["keyword_prediction"]
            if keyword_prediction["keyword_score"] > 0
            else transformer_prediction["label"]
        )

        print("\nFINAL EMERGENCY DETECTION:")
        print(final_prediction)

        print("\n" + "=" * 50)

    except KeyboardInterrupt:

        print("\nStopped listening.")
        break