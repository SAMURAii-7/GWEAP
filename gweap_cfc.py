import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt

og_df = pd.read_csv("filt_cfc-11 conc.csv")
# og_df = og_df.head(10)
print(og_df)
df = og_df.copy()
ix = [(row, 1) for row in range(df.shape[0]) for col in range(df.shape[1])]
for row, col in random.sample(ix, int(round(0.2*len(ix)))):
    df.iat[row, 1] = np.nan
newdf = df.interpolate()
if newdf["CFC-11 measurement"].isnull().values.any():
    newdf = newdf.fillna(method='bfill')
newdf.to_csv("new_cfc11.csv",sep=",",index=False)
newset2 = df.fillna(method='ffill')
if newset2["CFC-11 measurement"].isnull().values.any():
    newset2 = newset2.fillna(method='bfill')
newset3 = df.fillna(method='bfill')
if newset3["CFC-11 measurement"].isnull().values.any():
    newset3 = newset3.fillna(method='ffill')
meanFill = df.fillna(value=df["CFC-11 measurement"].mean())
medianFill = df.fillna(value=df["CFC-11 measurement"].median())
modeFill = df.fillna(value=df["CFC-11 measurement"].mode()[0])

def Euclidean_Dist(df1, df2, cols="CFC-11 measurement"):
    return np.linalg.norm(df1[cols].values - df2[cols].values)
data = {
    "Linear Interpolation": Euclidean_Dist(og_df, newdf),
    "Forward Fill": Euclidean_Dist(og_df, newset2),
    "Backward Fill": Euclidean_Dist(og_df, newset3),
    "Mean": Euclidean_Dist(og_df, meanFill),
    "Median": Euclidean_Dist(og_df, medianFill),
    "Mode": Euclidean_Dist(og_df, modeFill)
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