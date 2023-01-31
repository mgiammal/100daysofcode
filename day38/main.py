import requests
from dotenv import load_dotenv
import os
from datetime import datetime as dt

load_dotenv()
API_KEY = os.environ.get("NUTRI_API_KEY")
APP_ID = os.environ.get("NUTRI_APP_ID")
NUTRI_ENDPOINT = "https://trackapi.nutritionix.com/v2"
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
SHEETY_ENDPOINT = "https://api.sheety.co"
SHEETY_USR = os.environ.get("SHEETY_USR")
SHEETY_PROJ = "workoutTracking"

nutri_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_param = {
    "query": input("Tell me which exercises you did: ")
}

record_exercise = requests.post(url=f"{NUTRI_ENDPOINT}/natural/exercise", headers=nutri_headers, json=exercise_param)
record_exercise_rsp = record_exercise.json()
exercises = record_exercise_rsp.get("exercises")

now = dt.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

for exercise in exercises:
    sheety_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise.get("name").title(),
            "duration": exercise.get("duration_min"),
            "calories": exercise.get("nf_calories")
        }
    }

    sheety_header = {
        "Authorization": f"Bearer {SHEETY_TOKEN}"
    }

    update_sheety = requests.post(url=f"{SHEETY_ENDPOINT}/{SHEETY_USR}/{SHEETY_PROJ}/workouts",
                                  headers=sheety_header,
                                  json=sheety_params)
    print(update_sheety.text)
