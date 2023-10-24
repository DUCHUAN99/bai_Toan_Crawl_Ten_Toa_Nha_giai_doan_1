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
    data = response.json()
    places_of_interest = []
    for key in ['building', 'hospital', 'factory','apartments','office','residential','aeroway','shop','healthcare','leisure', 'amenity', 'industrial','tourism']:
        if key in data['address']:
            places_of_interest.append(data['display_name'])
            return places_of_interest
        else:
            continue

df = pd.read_csv("4g.csv")
address1 = []
latitude = df["LATITUDE"]
longitude = df["LONGITUDE"]
# Nhập vào tọa độ latitude và longitude
for i in range (0,len(latitude)):
    print(i)
    places_of_interest = get_places_of_interest(latitude[i], longitude[i])
    if places_of_interest:
        address1.append(places_of_interest[0])
        
    else:
        address1.append(places_of_interest)
print("_______________________________________________________________")
print("Completed")
df["Address1"] = address1
# Tên tệp Excel là 'output.xlsx', index=False để không bao gồm cột index
df.to_excel('4g_output1_use_libRequest.xlsx', index=False)
