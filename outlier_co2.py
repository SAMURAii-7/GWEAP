import pandas as pd

df = pd.read_csv("co2data_interpolate.csv")
df1 = df[df.groupby('country')['country'].transform('size') >= 150]
# df[df.groupby('Parameter')['Parameter'].transform('size') > 5]
final_df = df1.sort_values("country")
# final_df.to_csv("final_co2.csv",index=False)
print(df.shape)
print(final_df.shape)