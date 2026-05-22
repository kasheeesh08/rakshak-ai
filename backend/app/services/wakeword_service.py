WAKE_WORDS = [

    "rakshak",
    "help",
    "emergency",
    "bachao",
    "bachau",
    "save me",
    "sos"
]


def detect_wake_word(text: str):

    text = text.lower()

    for word in WAKE_WORDS:

        if word in text:

            return True

    return False