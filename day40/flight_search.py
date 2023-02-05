import os
from pprint import pprint

import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta
from flight_data import FlightData

load_dotenv()
FAPI_KEY = os.getenv("FAPI_KEY")
FAPI_URL = "https://api.tequila.kiwi.com"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.flight_detail = {}

    def get_locale_iata(self, city):
        header = {
            "apiKey": FAPI_KEY
        }
        params = {
            "term": city,
            "location_types": "airport"
        }
        locale_resp = requests.get(url=f"{FAPI_URL}/locations/query", params=params, headers=header)
        self.flight_detail = locale_resp.json().get("locations")[0]
        return self.flight_detail

    def search_flights(self, start_city, destination):
        tomorrow = datetime.now() + timedelta(days=1)
        six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

        header = {
            "apiKey": FAPI_KEY
        }
        params = {
            "fly_from": start_city,
            "fly_to": destination,
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": six_month_from_today.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "curr": "USD",
            "max_stopovers": 0
        }
        fl_search_resp = requests.get(url=f"{FAPI_URL}/v2/search", headers=header, params=params).json()
        try:
            fl_data = fl_search_resp.get("data")[0]
        except IndexError:
            params["max_stopovers"] = 1
            fl_search_resp = requests.get(url=f"{FAPI_URL}/v2/search", headers=header, params=params).json()
            try:
                fl_data = fl_search_resp.get("data")[0]
            except IndexError:
                print(f"There are no direct or single stop flights from {start_city} to {destination} for your search")
                return None
            pprint(fl_data)
            fl_obj = FlightData(
                price=fl_data.get("price"),
                origin_city=fl_data.get("cityFrom"),
                origin_airport=fl_data.get("flyFrom"),
                dest_city=fl_data.get("cityTo"),
                dest_airport=fl_data.get("flyTo"),
                out_dt=fl_data.get("route")[0].get("local_departure").split("T")[0],
                return_dt=fl_data.get("route")[1].get("local_departure").split("T")[0],
                stop_overs=1,
                via_city=fl_data.get("route")[0].get("cityTo")
            )
            return fl_obj
        else:

            fl_obj = FlightData(
                price=fl_data.get("price"),
                origin_city=fl_data.get("cityFrom"),
                origin_airport=fl_data.get("flyFrom"),
                dest_city=fl_data.get("cityTo"),
                dest_airport=fl_data.get("flyTo"),
                out_dt=fl_data.get("route")[0].get("local_departure").split("T")[0],
                return_dt=fl_data.get("route")[1].get("local_departure").split("T")[0]
            )
            return fl_obj
