from twilio.rest import Client
import smtplib

account_sid = "YOUR SID"
auth_token = "YOUR TOKEN"
TWILIO_VIRTUAL_NUMBER = 'YOUR TWILIO NUMBER'
TWILIO_VERIFIED_NUMBER = 'YOUR TWILIO NUMBER'
FROM_EMAIL = "SMTP EMAIL"
PASSWORD = "SMTP PASSWORD"

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

    def send_emails(self, message, emails):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(
                user=FROM_EMAIL,
                password=PASSWORD
            )
            for email in emails:
                connection.sendmail(
                    from_addr=FROM_EMAIL,
                    to_addrs=email,
                    msg=message
                )


