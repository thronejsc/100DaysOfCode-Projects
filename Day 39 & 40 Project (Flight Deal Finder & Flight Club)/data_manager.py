import requests
import json


AUTHORIZATION = "Basic dHJhY3ltY2dyYXZ5OnRyYWN5MTIz"
USERNAME = "tracymcgravy"
PASSWORD = "tracy123"


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, authorization, username, password):
        self.url = "https://api.sheety.co/f57625631ad80981b7200df237468651/flightDeals/prices"
        self.headers = {
            "Authorization": authorization,
            "Username": username,
            "Password": password
        }
        self.data = {}

    def get_data(self):
        response = requests.get(url=self.url, headers=self.headers)
        data = response.json()
        self.data = data["prices"]
        return self.data

    def put_test_iata(self):
        for city in self.data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(url=f"{self.url}/{city['id']}", json=new_data, headers=self.headers)
            print(response.text)

    def post_city(self, city_name, iata, price):
        new_data = {
            "price": {
                "city": city_name,
                "iataCode": iata,
                "lowestPrice": price,
            }
        }

        response = requests.post(url=self.url, json=new_data, headers=self.headers)
        print(response.text)


# sheety = DataManager(AUTHORIZATION, USERNAME, PASSWORD)
# sheety.post_city("New York", "", price="150")
