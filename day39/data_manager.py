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

    def get_sheet_data(self):
        header = {
            "Authorization": f"Bearer {FLIGHT_DEAL_SHEET_TOKEN}"
        }

        sheet_resp = requests.get(url=f"{SHEETY_URL}/{FD_SHEETY_USR}/flightDeals/prices",
                                  headers=header)
        self.sheet_data = sheet_resp.json().get("prices")
        return self.sheet_data

    def update_sheet(self, object_id, code):
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
