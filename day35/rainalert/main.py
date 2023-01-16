import requests
from twilio.rest import Client
import os

# You must set envs first.
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_API_KEY")
api_endpoint = "https://api.openweathermap.org/data/2.8/onecall"


parameters = {
    "lat": 46.056946,
    "lon": 14.505752,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
request = requests.get(api_endpoint, params=parameters).json()
hourly = request.get("hourly", [])
will_rain = False

for hour in hourly[:12]:
    weather = hour.get("weather", {})
    for forecast in weather:
        weather_code = forecast.get("id", None)
        if weather_code < 700:
            will_rain = True

# Replace from_ and to with your numbers
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_="TwilioPhoneNumber",
        to="YourNumber"
        )
    print(message.status)
