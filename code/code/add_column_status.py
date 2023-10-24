import pandas as pd

df = pd.read_excel("4g_win.xlsx")
print(len(df))
# df['status'] = 0  # Khởi tạo tất cả giá trị là 0
# df['status'].iloc[:2767] = 1  # Gán giá trị 1 cho 2767 hàng đầu tiên
# print(df)
# df.to_excel('4g_completeddd.xlsx', index=False)# 
