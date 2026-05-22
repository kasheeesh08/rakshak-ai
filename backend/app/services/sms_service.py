from twilio.rest import Client


ACCOUNT_SID = "YOUR_ACCOUNT_SID"

AUTH_TOKEN = "YOUR_AUTH_TOKEN"

TWILIO_PHONE = "YOUR_TWILIO_PHONE"

TARGET_PHONE = "YOUR_PHONE_NUMBER"


client = Client(
    ACCOUNT_SID,
    AUTH_TOKEN
)


def send_emergency_sms(

    emergency_type,

    location,

    severity

):

    message = f"""

EMERGENCY ALERT

Type: {emergency_type}

Location: {location}

Severity: {severity}

Rakshak AI detected an emergency.
"""

    client.messages.create(

        body=message,

        from_= "YOUR_TWILIO_PHONE",

        to = "YOUR_PHONE_NUMBER"
    )