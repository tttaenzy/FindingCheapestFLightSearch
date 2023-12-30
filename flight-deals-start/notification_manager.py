from twilio.rest import Client

TWILIO_SID = "AC6732f022baddf15356f59bc409a7254c"
TWILIO_AUTH_TOKEN = "c00ab06c243b18bb90952205a762d45d"
TWILIO_VIRTUAL_NUMBER = "+17086956184"
TWILIO_VERIFIED_NUMBER = "+917751002939"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
