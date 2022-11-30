import pandas as pd

df1 = pd.read_csv("india.csv")
# print(df1)
df2 = df1.copy()
df2['AverageTemperature'] = df1['AverageTemperature'].diff()
print(df2.shape)
outliers = df2[(df2['AverageTemperature'] >= 5) | (df2['AverageTemperature'] <= -5)].index
df2.drop(outliers,inplace=True)
print(df2.shape)

df2.to_csv("final_india.csv",index=False)