HINGLISH_MAPPINGS = {
    "aag": "fire",
    "accident ho gaya": "road accident",
    "heart attack aa raha hai": "heart attack",
    "chori": "crime",
    "loot": "robbery",
    "baadh": "flood",
    "saans nahi aa rahi": "breathing problem",
    "madad karo": "help",
    "ambulance bulao": "call ambulance"
}


def normalize_hinglish(text: str):

    normalized_text = text.lower()

    for hinglish, english in HINGLISH_MAPPINGS.items():
        normalized_text = normalized_text.replace(
            hinglish,
            english
        )

    return normalized_text