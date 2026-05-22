import re


LOCATION_PATTERNS = [

    r"near ([a-zA-Z ]+)",
    r"at ([a-zA-Z ]+)",
    r"in ([a-zA-Z ]+)",
    r"on ([a-zA-Z ]+)"
]


def extract_location(text: str):

    text = text.lower()

    for pattern in LOCATION_PATTERNS:

        match = re.search(pattern, text)

        if match:

            return match.group(1).strip()

    return None