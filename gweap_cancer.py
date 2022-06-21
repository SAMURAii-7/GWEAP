import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt

og_df = pd.read_csv("filt_cancer.csv")
df = og_df.copy()
ix = [(row, 1) for row in range(df.shape[0]) for col in range(df.shape[1])]
for row, col in random.sample(ix, int(round(0.2*len(ix)))):
    df.iat[row, 1] = np.nan
newdf = df.interpolate()
if newdf["Modeled Rate (Trend Line)"].isnull().values.any():
    newdf = newdf.fillna(method='bfill')
# print(newdf)
newdf.to_csv("cancer_rate_new.csv",sep=",",index=False)
newset2 = df.fillna(method='ffill')
if newset2["Modeled Rate (Trend Line)"].isnull().values.any():
    newset2 = newset2.fillna(method='bfill')
newset3 = df.fillna(method='bfill')
if newset3["Modeled Rate (Trend Line)"].isnull().values.any():
    newset3 = newset3.fillna(method='ffill')
meanFill = df.fillna(value=df["Modeled Rate (Trend Line)"].mean())
medianFill = df.fillna(value=df["Modeled Rate (Trend Line)"].median())
modeFill = df.fillna(value=df["Modeled Rate (Trend Line)"].mode()[0])

def Euclidean_Dist(df1, df2, cols="Modeled Rate (Trend Line)"):
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
