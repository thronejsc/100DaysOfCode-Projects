import requests
import json


AUTHORIZATION = "[SHEETY AUTHORIZATION]"
USERNAME = "[SHEETY USERNAME]"
PASSWORD = "[SHEETY PASSWORD]"
PRICE_URL = "[SHEETY URL FOR DESTINATION PRICES]"
EMAILS_URL = "[SHEETY URL FOR LIST OF EMAILS]"


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, authorization, username, password):
        self.headers = {
            "Authorization": authorization,
            "Username": username,
            "Password": password
        }
        self.data = {}

    def get_data(self):
        response = requests.get(url=PRICE_URL, headers=self.headers)
        data = response.json()
        self.data = data["prices"]
        return self.data

    def update_city_code(self):
        for city in self.data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(url=f"{PRICE_URL}/{city['id']}", json=new_data, headers=self.headers)

    def post_city(self, city_name, iata, price):
        new_data = {
            "price": {
                "city": city_name,
                "iataCode": iata,
                "lowestPrice": price,
            }
        }

        response = requests.post(url=PRICE_URL, json=new_data, headers=self.headers)
        print(response.text)

    def update_city_price(self):
        for city in self.data:
            new_data = {
                "price": {
                    "lowestPrice": round(float(city["lowestPrice"]) * 1.27,2),
                }
            }
            response = requests.put(url=f"{PRICE_URL}/{city['id']}", json=new_data, headers=self.headers)
            print(response.text)

    def get_emails(self):
        customers_endpoint = EMAILS_URL
        response = requests.get(url=customers_endpoint, headers=self.headers)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data

