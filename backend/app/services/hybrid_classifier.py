EMERGENCY_KEYWORDS = {
    "road accident": [
        "accident",
        "crash",
        "collision",
        "highway",
        "truck hit",
        "bike slip"
    ],

    "fire emergency": [
        "fire",
        "smoke",
        "burning",
        "aag",
        "blast"
    ],

    "medical emergency": [
        "heart attack",
        "blood",
        "unconscious",
        "injured",
        "ambulance"
    ],

    "crime": [
        "robbery",
        "gun",
        "kidnap",
        "attack",
        "chor",
        "rob"
    ],

    "natural disaster": [
        "flood",
        "earthquake",
        "building collapse",
        "storm",
        "landslide"
    ]
}


def keyword_boost(emergency_text: str):

    text = emergency_text.lower()

    scores = {
        category: 0
        for category in EMERGENCY_KEYWORDS
    }

    for category, keywords in EMERGENCY_KEYWORDS.items():

        for keyword in keywords:

            if keyword in text:
                scores[category] += 1

    best_category = max(scores, key=scores.get)

    return {
        "keyword_prediction": best_category,
        "keyword_score": scores[best_category]
    }