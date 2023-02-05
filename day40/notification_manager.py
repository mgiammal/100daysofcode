import os
import smtplib

from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()
TWILIO_API_KEY = os.getenv("TWILIO_API_KEY")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
TO_NUMBER = os.getenv("TO_NUMBER")
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_API_KEY)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_NUMBER,
            to=TO_NUMBER,
        )
        print(message.sid)

    def send_message(self, msg, link, emails):

        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{msg}\n{link}".encode('utf-8')
                )
