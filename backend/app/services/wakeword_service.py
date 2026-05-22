WAKE_WORDS = [

    # English
    "help",
    "emergency",
    "fire",
    "accident",
    "heart attack",
    "save me",
    "sos",

    # Hinglish
    "bachao",
    "bachaao",
    "aag",
    "takkar",
    "chor",

    # General distress
    "rakshak",
    "help",
    "emergency",
    "bachao",
    "bachaao",
    "save me",
    "sos",

    # Accident related
    "accident",
    "crash",
    "takkar",

    # Fire related
    "fire",
    "aag",

    # Medical
    "heart attack",
    "attack",
    "injured",
    "behosh",

    # Crime
    "robbery",
    "chor",
    "gun",
    "knife",

    # Disaster
    "flood",
    "earthquake",
    "bhukamp"
]


def detect_wake_word(text: str):

    text = text.lower()

    for word in WAKE_WORDS:

        if word in text:

            print(f"\nWake word detected: {word}")

            return True

    return False