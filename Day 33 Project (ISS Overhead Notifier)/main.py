import time

import requests
from datetime import datetime
import smtplib

MY_EMAIL = "tmacgravy21@gmail.com"
MY_PASSWORD = "qcvu ulxx qgds stqc"

PH_LAT = 12.879721
PH_LNG = 121.774017


def is_iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_data = iss_response.json()

    iss_lat = float(iss_data["iss_position"]["latitude"])
    iss_lng = float(iss_data["iss_position"]["longitude"])

    if PH_LAT-5 <= iss_lat <= PH_LAT+5 and PH_LNG-5 <= iss_lng <= PH_LNG+5:
        return True


def is_it_nighttime():
    parameters = {
        "lat": PH_LAT,
        "lng": PH_LNG,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)

    sunrise = int(response.json()["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(response.json()["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_it_nighttime() and is_iss_overhead():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:LOOK UP!\n\nThe ISS is above you!"
        )

