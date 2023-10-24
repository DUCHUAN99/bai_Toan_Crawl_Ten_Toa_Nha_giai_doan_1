import pandas as pd
import re
# đọc dữ liệu từ file excel
df = pd.read_excel("4g_output2_use_selenium.xlsx")
print(df)
df1 = df.drop(columns=['Address1'])
df1.columns = ['LATITUDE','LONGITUDE','CI','TAC','LCRID','ENODEB_ID','IBS_STATUS','Address1']
print(df1)
df1.to_excel('4g_output2_use_seleniumm.xlsx', index=False)

