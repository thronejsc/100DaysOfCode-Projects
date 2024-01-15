from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch

from notification_manager import NotificationManager

AUTHORIZATION = "YOUR SHEETY AUTHORIZATION"
USERNAME = "SHEETY USERNAME"
PASSWORD = "SHEETY PASSWORD"


ORIGIN_CITY_IATA = "MNL"

sheety_api = DataManager(AUTHORIZATION, USERNAME, PASSWORD)
flight_search = FlightSearch()
data_manager = DataManager(AUTHORIZATION, USERNAME, PASSWORD)

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

        if flight is None:
            continue

        if flight.price < destination['lowestPrice']:

            users = data_manager.get_emails()
            emails = [row["email"] for row in users]
            names = [row["fristName"] for row in users]

            notification = NotificationManager()

            message = f"Low Price Alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date}-{flight.return_date}"
            if flight.stop_overs > 0:
                message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

            notification.send_emails(message, emails)

    except AttributeError:
        print(f"No price found for {destination['iataCode']}.")