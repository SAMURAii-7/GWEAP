import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt

og_df = pd.read_csv("filt_aqi.csv")
# og_df = og_df.iloc[79:89]
print(og_df)
df = og_df.copy()
ix = [(row, 1) for row in range(df.shape[0]) for col in range(df.shape[1])]
for row, col in random.sample(ix, int(round(0.2*len(ix)))):
    df.iat[row, 2] = np.nan
print(df)
newdf = df.interpolate()
if newdf["AQI"].isnull().values.any():
    newdf = newdf.fillna(method='bfill')
newdf.loc[newdf['AQI']>=300, 'AQI_Bucket'] = "Very Poor"
newdf.loc[(newdf['AQI']>=200) & (newdf['AQI']<300), 'AQI_Bucket'] = "Poor"
newdf.loc[(newdf['AQI']>=100) & (newdf['AQI']<200), 'AQI_Bucket'] = "Moderate"
newdf.loc[(newdf['AQI']>=50) & (newdf['AQI']<100), 'AQI_Bucket'] = "Satisfactory"
newdf.loc[newdf['AQI']<50 , 'AQI_Bucket'] = "Good"
newdf.to_csv("aqi.csv",sep=",",index=False)

newset2 = df.fillna(method='ffill')
if newset2["AQI"].isnull().values.any():
    newset2 = newset2.fillna(method='bfill')
newset3 = df.fillna(method='bfill')
if newset3["AQI"].isnull().values.any():
    newset3 = newset3.fillna(method='ffill')
# newset3.to_csv("aqi.csv",sep=",",index=False)
meanFill = df.fillna(value=df["AQI"].mean())
medianFill = df.fillna(value=df["AQI"].median())
modeFill = df.fillna(value=df["AQI"].mode()[0])

def Euclidean_Dist(df1, df2, cols="AQI"):
    return np.linalg.norm(df1[cols].values - df2[cols].values)
data = {
    "Linear Interpolation": round(Euclidean_Dist(og_df, newdf), 3),
    "Forward Fill": round(Euclidean_Dist(og_df, newset2), 3),
    "Backward Fill": round(Euclidean_Dist(og_df, newset3), 3),
    "Mean": round(Euclidean_Dist(og_df, meanFill), 3),
    "Median": round(Euclidean_Dist(og_df, medianFill), 3),
    "Mode": round(Euclidean_Dist(og_df, modeFill), 3)
}
x = list(data.keys())
y = list(data.values())
plt.xlabel('Data Filling Method', labelpad=15, fontdict={'size': 12})
plt.ylabel('Euclidean Distance', labelpad=10, fontdict={'size': 12})
plt.title('Distance from Original', fontdict={'fontsize': 16})
ax = plt.subplot()
plt.bar(x, y)
plt.setp(ax.get_xticklabels(), rotation=30, ha='right')
plt.show()
