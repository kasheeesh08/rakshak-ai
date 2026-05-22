import wave
import audioop


THRESHOLD = 500


def contains_speech(audio_path):

    wf = wave.open(audio_path, "rb")

    frames = wf.readframes(wf.getnframes())

    rms = audioop.rms(frames, 2)

    wf.close()

    return rms > THRESHOLD