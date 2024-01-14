import requests
from twilio.rest import Client

account_sid = "ACc931465dae26952f7c1ec6001c7718c0"
auth_token = "fd479c2fafb43bfc019a0eaa07af0f73"



class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_message(self, price, origin_city, origin_airport, destination_city,
                     destination_airport, out_date, return_date):
        message = self.client.messages \
            .create(
                body=f"Low Price Alert! Only ${price} to fly from {origin_city}-{origin_airport} to {destination_city}-{destination_airport}, from {out_date}-{return_date}",
                from_='+12019925595',
                to='+639761214776',
            )
        print(message.body)
        print(message.status)



