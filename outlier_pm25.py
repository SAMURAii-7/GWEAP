import pandas as pd

df = pd.read_csv("pm25_interpolate.csv")
df1 = df[df.groupby('Location')['Location'].transform('size') >= 25]
# df[df.groupby('Parameter')['Parameter'].transform('size') > 5]
print(df1.Location.unique())