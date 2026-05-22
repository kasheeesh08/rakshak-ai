WAKE_WORDS = [
    # Hinglish
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
    "skid",
    "crash",
    "takkar",

    # Fire related
    "fire",
    "aag",

    # Medical
    "heart attack",
    "unconscious",
    "not well",
    "panic attack",
    "injured",
    "behosh",
    "suffocate",
    "suffocation",
    "saans nhi aarhi",
    "not able to breath",

    # Crime
    "attack",
    "robbery",
    "thief",
    "chor",
    "chori",
    "gun",
    "knife",

    # Disaster
    "flood",
    "earthquake",
    "bhukamp",
    "tsunami",
]


def detect_wake_word(text: str):

    text = text.lower()

    for word in WAKE_WORDS:

        if word in text:

            print(f"\nWake word detected: {word}")

            return True

    return False