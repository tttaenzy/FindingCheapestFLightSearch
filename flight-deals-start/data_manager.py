import requests
SHEETY_ENDPOINT="https://api.sheety.co/f78847236614167da59c54f05e021939/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.destination_data={}

    def get_destination_data(self):
        response=requests.get(SHEETY_ENDPOINT)
        data=response.json()
        self.destination_data=data["prices"]
        return self.destination_data

    def update_destination_data(self):
        for city in self.destination_data:
            new_data={
                "price":{
                    "iataCode":city["iataCode"]
                }
            }
            response=requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}",json=new_data)
            print(response.text)
