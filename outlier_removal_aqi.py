import pandas as pd

# df = pd.read_csv("aqi.csv")
# print(df.shape)
# outlier = df[df["AQI"] > 600 ].index
# df.drop(outlier,inplace=True)
# print(df.shape)
# df.to_csv("outlier_aqi.csv",index=False)
df1 = pd.read_csv("outlier_aqi.csv")
print(df1.shape)
print(df1.City.unique())
bangalore = df1.loc[df1['City'] == "Bengaluru"]
chennai = df1.loc[df1['City'] == "Chennai"]
delhi = df1.loc[df1['City'] == "Delhi"]
hyderabad = df1.loc[df1['City'] == "Hyderabad"]
kolkata = df1.loc[df1['City'] == "Kolkata"]
mumbai = df1.loc[df1['City'] == "Mumbai"]

bangalore.to_csv("bangalore_aqi.csv",index=False)
chennai.to_csv("chennai_aqi.csv",index=False)
delhi.to_csv("delhi_aqi.csv",index=False)
hyderabad.to_csv("hyderabad_aqi.csv",index=False)
kolkata.to_csv("kolkata_aqi.csv",index=False)
mumbai.to_csv("mumbai_aqi.csv",index=False)

