SEVERITY_KEYWORDS = {

    "critical": [

        "dead",
        "dying",
        "unconscious",
        "not breathing",
        "heavy bleeding",
        "blast",
        "building collapse",
        "trapped",
        "heart attack"
    ],

    "high": [

        "fire",
        "blood",
        "injured",
        "crash",
        "accident",
        "gun",
        "knife"
    ],

    "medium": [

        "help",
        "pain",
        "robbery",
        "smoke",
        "stolen"
    ],

    "low": [

        "minor",
        "small",
        "light injury"
    ]
}


def detect_severity(text: str):

    text = text.lower()

    for severity, keywords in SEVERITY_KEYWORDS.items():

        for keyword in keywords:

            if keyword in text:

                return severity

    return "unknown"