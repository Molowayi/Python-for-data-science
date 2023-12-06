#%%
import pandas as pd
import numpy as np

s = pd.Series([10, 30, np.nan, None, 62, 18])
print(s[2:4])

dates = pd.date_range("2023-11-29", periods=6, freq="D")
print(dates)

timeseries = pd.Series(s.values, index=dates)
print(timeseries)

data = np.random.randn(6, 4)
df = pd.DataFrame(data, columns=["Area", "Birth rate", "Country", "Dynamite blasts"], index=dates)
print(df)
print(df.loc[:, ["Area", "Country"]])
print(df.loc[["2023-11-29", "2023-11-30"], ["Area", "Country"]])
print(df.loc[["2023-11-29", "2023-11-30"], "Area":"Country"])
print(df.loc["2023-11-29":"2023-12-02", "Area":"Country"])

print("------------")

print(df.iloc[-1, [1, 3]])

# plot = df.plot()

print(df[df["Area"] > 0])
print((df["Area"] > 0) & (df["Country"] > 0))
print(df[(df["Area"] > 0) & (df["Country"] > 0)])



