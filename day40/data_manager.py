import os

import requests
from dotenv import load_dotenv

load_dotenv()
FLIGHT_DEAL_SHEET_TOKEN = os.getenv("FLIGHT_DEAL_SHEET_TOKEN")
FD_SHEETY_USR = os.getenv("FD_SHEETY_USR")
SHEETY_URL = "https://api.sheety.co"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_data = {}

    def get_sheet_data(self, sheet_name):
        header = {
            "Authorization": f"Bearer {FLIGHT_DEAL_SHEET_TOKEN}"
        }

        sheet_resp = requests.get(url=f"{SHEETY_URL}/{FD_SHEETY_USR}/flightDeals/{sheet_name}",
                                  headers=header)
        self.sheet_data = sheet_resp.json().get(sheet_name)
        return self.sheet_data

    def update_sheet_price(self, object_id, code):
        header = {
            "Authorization": f"Bearer {FLIGHT_DEAL_SHEET_TOKEN}"
        }
        params = {
            "price":
                {
                    "iataCode": code
                }
        }
        sheet_resp = requests.put(url=f"{SHEETY_URL}/{FD_SHEETY_USR}/flightDeals/prices/{object_id}",
                                  headers=header,
                                  json=params)
        print(sheet_resp.json())

    def insert_sheet_email(self, first_name, last_name, email, source_airport="JFK"):
        header = {
            "Authorization": f"Bearer {FLIGHT_DEAL_SHEET_TOKEN}"
        }
        params = {
            "user":
                {
                    "firstName": first_name,
                    "lastName": last_name,
                    "email": email,
                    "sourceAirport": source_airport
                }
        }
        sheet_resp = requests.post(url=f"{SHEETY_URL}/{FD_SHEETY_USR}/flightDeals/users",
                                   headers=header,
                                   json=params)
        print(sheet_resp.json())
