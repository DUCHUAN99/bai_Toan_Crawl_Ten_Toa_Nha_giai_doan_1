import requests
import time
import pandas as pd

def get_places_of_interest(latitude, longitude):
    url = f"https://nominatim.openstreetmap.org/reverse"
    params = {
        "format": "json",
        "lat": latitude,
        "lon": longitude,
        "addressdetails": 1,
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        print(data)
        places_of_interest = []
        for key in ['building', 'hospital', 'factory','apartments','office','residential','aeroway','healthcare','leisure', 'industrial','tourism']:
            if key in data['address']:
                places_of_interest.append(data['display_name'])
        return places_of_interest
    else:
        return "Không thể kết nối đến OpenStreetMap API."

# Nhập vào tọa độ latitude và longitude

a= '  21.055587	105.804871  '




b= a.split()
latitude =   b[0]
longitude =  	b[1]


places_of_interest = get_places_of_interest(latitude, longitude)
print(f"Các địa điểm quan tâm gần tọa độ {latitude}, {longitude}:")
for place in places_of_interest:
    print(place)