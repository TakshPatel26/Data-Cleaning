import pandas as pd
import csv

df=pd.read_csv("total_stars.csv")
print(df.head())
print(df.columns)
print(df.shape)

del df["Star_name"]

print(df.shape)

df.to_csv('newcleaned.csv',index=False)