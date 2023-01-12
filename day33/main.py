import smtplib

import requests
from datetime import datetime
import time

MY_LAT = 30.507351  # Your latitude
MY_LONG = 20.127758  # Your longitude
my_email = "REPLACE_ME"
to_email = "REPLACE_ME"


def is_iss_nearby():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        print("nearby")
        return True
    return False


def send_email():
    pw = "REPLACE_ME"
    gmail_smtp = "smtp.gmail.com"

    with smtplib.SMTP(gmail_smtp) as new_connection:
        new_connection.starttls()
        new_connection.login(user=my_email, password=pw)
        new_connection.sendmail(from_addr=my_email,
                                to_addrs=to_email,
                                msg=f"Subject:ISS Overhead!\n\nLook UP!")


# Your position is within +5 or -5 degrees of the ISS position.


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True
    return False


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if is_night() and is_iss_nearby():
        print("night time")
        send_email()

