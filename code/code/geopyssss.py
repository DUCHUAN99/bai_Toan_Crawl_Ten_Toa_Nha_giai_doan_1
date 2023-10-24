
import time
import pandas as pd
from geopy.geocoders import Nominatim


# df = pd.read_excel("4G_IBS.xlsx")
# address1 = []
# latitude = df["LATITUDE"]
# longitude = df["LONGITUDE"]


a= '     10.77365	106.70123'

b= a.split()
latitude =   b[0]
longitude =  	b[1]
#Khởi tạo đối tượng geolocator của OpenStreetMap Nominatim API
geolocator = Nominatim(user_agent="my_geocoder")

    # Gửi yêu cầu tìm kiếm dựa trên tọa độ và một từ khóa liên quan đến tòa nhà, chung cư hoặc trung tâm thương mại
location = geolocator.reverse((latitude, longitude), exactly_one=True, addressdetails=True, zoom=18, namedetails=True )

    #location = geolocator.reverse((latitude[i], longitude[i]), exactly_one=True, addressdetails=True, zoom=18, namedetails=True)
    # Lấy địa chỉ gần nhất từ kết quả tìm kiếm
print(location.raw.get('display_name'))

nearest_building_address = location.address

    # In ra địa chỉ của tòa nhà/chung cư gần nhất
    #print(i+1)
print(nearest_building_address)
    #address1.append(nearest_building_address)
# print("_______________________________________________________________")
# print("Completed")
# df["Address1"] = address1
# # Tên tệp Excel là 'output.xlsx', index=False để không bao gồm cột index
# df.to_excel('output_use_geopy.xlsx', index=False)