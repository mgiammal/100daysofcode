import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}
request = requests.get("https://opentdb.com/api.php?amount=10&type=boolean", params=parameters)
question_data = request.json().get("results")
