import requests
from pprint import pprint

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "SMnQKU9C9RTpcD8UdD3wskdf9_uwRS1W"

class FlightSearch:

    def __init__(self):
        self.url = TEQUILA_ENDPOINT
        self.header = {
            "apikey": TEQUILA_API_KEY,
        }


    def get_destination_code(self, city_name):
        endpoint = "locations/query"
        params = {
            "term": city_name,
            "locale": "en-US",
            "location_types": "airport",
            "active_only": "true",
            "limit": 1,

        }

        response = requests.get(url=f"{self.url}/{endpoint}", params=params, headers=self.header)
        data = response.json()
        print(data)
        return data["locations"][0]["id"]


flight_search = FlightSearch()
flight_search.get_destination_code(city_name="New York")
