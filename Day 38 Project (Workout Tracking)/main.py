import requests
from datetime import datetime
import json


APP_ID = "[YOUR API ID]"
APP_KEY = "[YOUR API KEY]"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

sheety_headers = {
    "Authorization": "[YOUR AUTHORIZATION]"
}

url = "https://trackapi.nutritionix.com"

query = input("Tell me which exercise you did: ")

data = {
    "query": query
}

nle_endpoint = f"{url}/v2/natural/exercise"

response = requests.post(url=nle_endpoint, json=data, headers=headers)
response_data = json.loads(response.text)

sheety_url = "[YOUR SHEETY URL]"

for i in response_data["exercises"]:

    exercise = i["name"]
    duration = i["duration_min"]
    calories = i["nf_calories"]

    time = datetime.now()

    workout_data = {
        "workout": {
            "date": time.strftime("%d/%m/%Y"),
            "time": time.strftime("%H:%M:%S"),
            "exercise": exercise.title(),
            "duration": duration,
            "calories": calories,
        }
    }

    response = requests.post(url=sheety_url, json=workout_data, headers=sheety_headers)
    print(response.text)
    print(response.status_code)





