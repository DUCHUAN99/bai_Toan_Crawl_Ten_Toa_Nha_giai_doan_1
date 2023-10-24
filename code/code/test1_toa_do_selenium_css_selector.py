from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.options import Options
import pandas as pd


#lấy 10 dòng đầu của cột vĩ độ và kinh độ
latitude = 21.0074
longitude = 105.79317
# Tạo các tùy chọn cho trình duyệt Chrome
#chrome_options = Options()
 # Thêm tùy chọn headless cho trình duyệt google chrome chạy ẩn chứ ko hiện
#chrome_options.add_argument("--headless") 
# Khởi tạo trình duyệt Chrome
driver = webdriver.Chrome()

# Điều hướng đến trang chủ của Google Maps
driver.get("https://www.google.com/maps")
# Chờ cho trang web tải hoàn tất
driver.implicitly_wait(10)
# Tọa độ (vĩ độ và kinh độ) bạn muốn tìm kiếm

# Tìm ô tìm kiếm bằng ID
search_box = driver.find_element(By.ID, "searchboxinput")
# Nhập tọa độ vào ô tìm kiếm

search_box.send_keys(f"{latitude}, {longitude}")
# Cách 1
# Tìm nút tìm kiếm bằng ID và bấm vào nó
#search_button = driver.find_element(By.ID, "searchbox-searchbutton")
#search_button.click()
# Cách 2 gửi yêu cầu truy cập trực tiếp bằng phím ENTER
search_box.send_keys(Keys.ENTER)

# Chờ cho kết quả xuất hiện (thời gian chờ có thể cần điều chỉnh)
driver.implicitly_wait(10)
# Lấy thông tin của tòa nhà/chung cư gần nhất từ trang kết quả
building_name = driver.find_element(By.CSS_SELECTOR,"#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div:nth-child(10) > div.Y4SsEe").text
#building_address = driver.find_element_by_css_selector("span.section-result-location").text
driver.implicitly_wait(10)
# In ra thông tin của tòa nhà/chung cư gần nhất
print("Tên tòa nhà/chung cư gần nhất:", building_name)
#print("Địa chỉ:", building_address)

driver.implicitly_wait(10)
time.sleep(3)
# Đóng trình duyệt
driver.quit()

