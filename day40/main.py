# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from data_manager import DataManager
from notification_manager import NotificationManager
from flight_search import FlightSearch

SOURCE_AIRPORT = "JFK"
dm = DataManager()
f_search = FlightSearch()
notify = NotificationManager()


print("Welcome to Mikes Flight Club\nWe find the best flight deals and email you.")
choice = input("What would you like to do? (join/search)\n")

if choice == "join":
    first_n = input("What is your first name?\n")
    last_n = input("What is your last name?\n")
    source_airport = input("Set your source Airport (this must be an airport code (e.g. JFK)\n")
    email_1 = input("What is your email?\n")
    email = input("Type your email again.\n")

    if email == email_1:
        print("You're in the club!")
        # TODO: replace default source airport with user entered airport in sheet.
        dm.insert_sheet_email(first_n, last_n, email)

if choice == "search":
    price_data = dm.get_sheet_data("prices")
    users = dm.get_sheet_data("users")

    for locale in price_data:
        iata_code = locale.get("iataCode")
        if not iata_code:
            iata_code = f_search.get_locale_iata(locale.get("city")).get("code")
            dm.update_sheet_price(locale.get("id"), iata_code)

        # TODO: add functionality to replace SOURCE_AIRPORT with airport codes users are interested in
        flight = f_search.search_flights(SOURCE_AIRPORT, iata_code)
        if flight and flight.price < locale.get("lowestPrice"):

            print(f"{flight.dest_airport} for ${flight.price}")

            msg = f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-" \
                  f"{flight.origin_airport} to {flight.dest_city}-{flight.dest_airport}, from " \
                  f"{flight.out_dt} to {flight.return_dt}."

            link = f"https://www.google.com/flights?hl=en#flt={flight.origin_airport}.{flight.dest_airport}." \
                   f"{flight.out_dt}*{flight.dest_airport}.{flight.origin_airport}.{flight.return_dt}"

            if flight.stop_overs > 0:
                msg += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

            if users:
                emails = [user.get("email") for user in users]
                notify.send_message(msg, link, emails)
