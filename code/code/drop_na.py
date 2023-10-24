import pandas as pd

df = pd.read_csv("4g.csv")
df.dropna(how = "all", inplace= True)
print(df.head(10))
df.to_csv('4gg.csv', index=False)
