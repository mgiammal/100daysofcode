# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from data_manager import DataManager
from day39.notification_manager import NotificationManager
from flight_search import FlightSearch

dm = DataManager()
f_search = FlightSearch()
notify = NotificationManager()

sheet_data = dm.get_sheet_data()
for locale in sheet_data:
    iata_code = locale.get("iataCode")
    if not iata_code:
        iata_code = f_search.get_locale_iata(locale.get("city")).get("code")
        dm.update_sheet(locale.get("id"), iata_code)

    flight = f_search.search_flights("MIA", iata_code)
    if flight and flight.price < locale.get("lowestPrice"):
        print(f"{flight.dest_airport} for ${flight.price}")
        notify.send_message(flight)


