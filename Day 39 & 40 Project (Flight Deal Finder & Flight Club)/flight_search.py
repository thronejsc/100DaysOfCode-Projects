import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "SMnQKU9C9RTpcD8UdD3wskdf9_uwRS1W"


class FlightSearch:

    def __init__(self):
        self.url = TEQUILA_ENDPOINT
        self.headers = {
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

        response = requests.get(url=f"{self.url}/{endpoint}", params=params, headers=self.headers)
        data = response.json()
        code = data["locations"][0]["id"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=self.headers,
            params=query,
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data


