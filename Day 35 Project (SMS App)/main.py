import requests
from twilio.rest import Client

API_KEY = "40d0891809356b240fd16e4552d3ecf7"

account_sid = "ACc931465dae26952f7c1ec6001c7718c0"
auth_token = "b54cbc51e92a21cab923734d62d2992d"

parameters = {
    "lat": 14.676041,
    "lon": 121.043701,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
print(response.status_code)

weather_data = response.json()

will_rain = False
for i in weather_data["list"]:
    condition_code = i['weather'][0]['id']
    if condition_code < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body="Hi, It's going to rain today. Remember to bring an umbrella ☂️",
                         from_='+12019925595',
                         to='+639761214776'
                     )

    print(message.status)