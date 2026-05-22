from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

candidate_labels = [
    "road accident",
    "fire emergency",
    "medical emergency",
    "crime",
    "natural disaster"
]


def classify_emergency(text: str):

    result = classifier(
        text,
        candidate_labels
    )

    return {
        "label": result["labels"][0],
        "score": round(result["scores"][0], 3)
    }