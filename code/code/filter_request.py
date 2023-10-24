import pandas as pd
import re
# đọc dữ liệu từ file excel
df = pd.read_excel("4g_output1_use_libRequest.xlsx")
print(df.info())
df1 = df[df['Address1'].isna()]
print(df1.info())

df2 = df[df['Address1'].notna()]
print(df2.info())



df1.to_excel('4g_output1_use_request_fail.xlsx', index=False)
df2.to_excel('4g_output1_use_request_win.xlsx', index=False)