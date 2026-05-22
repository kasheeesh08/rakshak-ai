import json
from datetime import datetime


LOG_FILE = "incident_logs.json"


def save_incident(data):

    try:

        with open(LOG_FILE, "r") as file:
            incidents = json.load(file)

    except:

        incidents = []

    incidents.append({

        "timestamp": str(datetime.now()),

        "transcription": data["transcription"],

        "emergency": data["emergency"],

        "severity": data["severity"],

        "location": data["location"]

    })

    with open(LOG_FILE, "w") as file:

        json.dump(
            incidents,
            file,
            indent=4
        )