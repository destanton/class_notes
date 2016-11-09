from twilio.rest import TwilioRestClient


class Messenger:
    account_sid = "ACfb38412eea26fff58e42231ca6ba3cd1"
    auth_token = "bf8d806303d1bfce96e889e23e4b6d34"

    def __init__(self):
        self.client = TwilioRestClient(self.account_sid, self.auth_token)

    def send(self, message):
        return self.client.messages.create(body=message, to="+18644989400", from_="+18643260365")
