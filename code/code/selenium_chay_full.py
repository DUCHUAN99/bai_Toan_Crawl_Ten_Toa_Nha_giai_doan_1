from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.options import Options
import pandas as pd
import pickle


try:
    df = pd.read_excel("4g_output1_use_request_fail.xlsx")
    address2 = []
    latitude = df["LATITUDE"]
    longitude = df["LONGITUDE"]
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options= chrome_options)
    time.sleep(0.1)
    driver.get("https://www.google.com/maps")
    driver.implicitly_wait(20)
    for i in range (950,len(latitude)):
        print(i+1)
        if(i%50 == 49):
            time.sleep(1)
            driver = webdriver.Chrome(options= chrome_options)
            driver.get("https://www.google.com/maps")
            driver.implicitly_wait(30)

# Tìm ô tìm kiếm bằng ID
        search_box = driver.find_element(By.ID, "searchboxinput")
# Nhập tọa độ vào ô tìm kiếm
        search_box.send_keys(f"{latitude[i]}, {longitude[i]}")
# Cách 1
# Tìm nút tìm kiếm bằng ID và bấm vào nó
#search_button = driver.find_element(By.ID, "searchbox-searchbutton")
#search_button.click()
# Cách 2 gửi yêu cầu truy cập trực tiếp bằng phím ENTER
        driver.implicitly_wait(30)
        search_box.send_keys(Keys.ENTER)

# Chờ cho kết quả xuất hiện (thời gian chờ có thể cần điều chỉnh)
        driver.implicitly_wait(30)
        time.sleep(0.1)
# Thu thập thông tin về địa chỉ từ trang tìm kiếm
        place_address = driver.find_element(By.CSS_SELECTOR, "#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div:nth-child(10) > div.Y4SsEe > div.LCF4w > span.JpCtJf > span").text
        driver.implicitly_wait(30)
        clear_box = driver.find_element(By.CSS_SELECTOR, "#searchbox > div.lSDxNd > button")
        clear_box.click()
        driver.implicitly_wait(30)
# In thông tin địa chỉ
        address2.append(place_address)
# Đóng trình duyệt
    driver.quit()

except Exception as e:
    # Xử lý lỗi (nếu cần)
    print("Xảy ra lỗi:", str(e))

finally:
    # Lưu danh sách thông tin thu thập được vào file pickle
    with open('address22.pkl', 'wb') as f:
        pickle.dump(address2, f)


print("_______________________________________________________________")
print("Completed")
# df["Address2"] = address2
# # Tên tệp Excel là 'output.xlsx', index=False để không bao gồm cột index
# df.to_excel('4g_output2_use_selenium.xlsx', index=False)