import pandas as pd
df1 = pd.read_csv("globalTemp_ip.csv")
# print(df1.describe()['LandAvgTemp'])
df2 = df1.copy()
df2['LandAvgTemp'] = df1['LandAvgTemp'].diff()
print(df2.shape)
outliers = df2[(df2['LandAvgTemp'] >= 5) | (df2['LandAvgTemp'] <= -5)].index
df2.drop(outliers,inplace=True)
print(df2.shape)

df2.to_csv("final_globalTemp.csv",index=False)