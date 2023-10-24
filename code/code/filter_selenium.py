import pandas as pd
import re
# đọc dữ liệu từ file excel
df = pd.read_excel("4g_output2_use_seleniumm.xlsx")
#Danh sách các từ bạn muốn tìm kiếm trong địa chỉ
desired_words = ['khu đô thị', 'tower', 'tòa', 'chung cư','building','vin', 'plaza', 'land', 'home','apartment', 'chung cu', 'căn hộ','center', 'nhà', 'KĐT',
                 'big c', 'văn phòng', 'bệnh viện', 'hotel','grand','khách sạn','trường','mall','bank','sun','garden','park','trung tâm','sky',
                 'pearl','công ty','ct','hh','win','house','town','holding','Riverside','department','mart','ngân hàng','cao ốc','Appartments','Khu thương mại',
                 'Tòa Nhà','Apartments','home','toa nha','celadon','block','gele','office','green','Tòa nhà' ]

# Tạo biểu thức chính quy với các từ bạn muốn tìm kiếm, kết hợp chúng bằng toán tử |
regex_pattern = '|'.join(map(re.escape, desired_words))
# Lọc các hàng trong đó cột 'Address' chứa ít nhất một từ trong danh sách
filtered_df_win = df[df['Address1'].str.contains(regex_pattern, case=False, na=False, regex=True)]
filtered_df_fail = df[~df['Address1'].str.contains(regex_pattern, case=False, na=False, regex=True)]
print(len(filtered_df_win))
print(len(df))
print(len(filtered_df_win)/len(df))
print(len(filtered_df_fail))

# filtered_df_win.to_excel('4g_output2_use_seleniumm_win.xlsx', index=False)
# filtered_df_fail.to_excel('4g_output2_use_seleniumm_fail.xlsx', index=False)