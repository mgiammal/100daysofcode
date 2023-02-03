import os

from twilio.rest import Client
from dotenv import load_dotenv
from flight_data import FlightData

load_dotenv()
TWILIO_API_KEY = os.getenv("TWILIO_API_KEY")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
TO_NUMBER = os.getenv("TO_NUMBER")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_API_KEY)

    def send_message(self, flight_data: FlightData):
        message = self.client.messages.create(
            body=f"Low price alert! Only ${flight_data.price} to fly from {flight_data.origin_city}-"
                 f"{flight_data.origin_airport} to {flight_data.dest_city}-{flight_data.dest_airport}, from "
                 f"{flight_data.out_dt} to {flight_data.return_dt}.",
            from_=TWILIO_NUMBER,
            to=TO_NUMBER
        )
        return message.sid
