import pickle
import numpy as np
import pandas as pd


df = pd.read_excel("4g_output1_use_request_fail.xlsx")

# Mở tệp pickle
with open('address2.pkl', 'rb') as file:
    data = pickle.load(file)
with open('address22.pkl', 'rb') as file:
    data1 = pickle.load(file)
merged_array = np.concatenate((data,data1 ))
df["Address2"] = merged_array
  # Tên tệp Excel là 'output.xlsx', index=False để không bao gồm cột index
df.to_excel('4g_output2_use_selenium.xlsx', index=False)