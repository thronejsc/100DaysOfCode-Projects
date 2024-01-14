import requests
from twilio.rest import Client

account_sid = "YOUR SID"
auth_token = "YOUR TOKEN"

class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_message(self, price, origin_city, origin_airport, destination_city,
                     destination_airport, out_date, return_date):
        message = self.client.messages \
            .create(
                body=f"Low Price Alert! Only ${price} to fly from {origin_city}-{origin_airport} to {destination_city}-{destination_airport}, from {out_date}-{return_date}",
                from_='+YOUR TWILIO NUMBER',
                to='+YOUR NUMBER',
            )
        print(message.body)
        print(message.status)



