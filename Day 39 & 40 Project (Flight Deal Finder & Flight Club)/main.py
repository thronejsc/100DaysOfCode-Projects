from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch

from notification_manager import NotificationManager

AUTHORIZATION = "Basic dHJhY3ltY2dyYXZ5OnRyYWN5MTIz"
USERNAME = "tracymcgravy"
PASSWORD = "tracy123"


ORIGIN_CITY_IATA = "MNL"

sheety_api = DataManager(AUTHORIZATION, USERNAME, PASSWORD)
flight_search = FlightSearch()

sheet_data = sheety_api.get_data()

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    sheety_api.destination_data = sheet_data
    sheety_api.update_city_code()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    try:
        flight = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today
        )

        if flight.price < destination['lowestPrice']:
            notification = NotificationManager()
            notification.send_message(flight.price, flight.origin_city, flight.origin_airport, flight.destination_city,
                                      flight.destination_airport, flight.out_date, flight.return_date)


    except AttributeError:
        print(f"No price found for {destination['iataCode']}.")



