import requests

SHEET_ENDPOINT = "https://api.sheety.co/bbbc9c35647381e8005c192e85b42b82/копияFlightDeals/prices"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response_sheet = requests.get(url=SHEET_ENDPOINT)
        self.data = response_sheet.json()["price"]
        return self.data

    def update_destination_codes(self):
        for city in self.data:
            sheet_data = {
                "price": {
                    "iataCode": city["iataCode"],
                }
            }

            response = requests.put(
                url=f"{SHEET_ENDPOINT}/{city['id']}",
                json=sheet_data
            )
            # print(response.text)
