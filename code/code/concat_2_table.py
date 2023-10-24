import pandas as pd

df1 = pd.read_excel("4g_win.xlsx")
df2 = pd.read_excel("4g_output2_use_seleniumm_fail.xlsx")
# Ghép hai DataFrame thành một DataFrame mới với chỉ số dòng liên tục
merged_df = pd.concat([df1, df2], ignore_index=True)

# In kết quả
merged_df.to_excel('4g_complete.xlsx', index=False)
