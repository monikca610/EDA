import pandas as pd

# Load Employee dataset
df = pd.read_csv("Employee(9).csv")

# Sort data according to JoiningYear
df = df.sort_values("JoiningYear")

# Calculate 7-observation Rolling Mean
df["Rolling_Mean"] = df["Age"].rolling(window=7).mean()

# Calculate 7-observation Rolling Standard Deviation
df["Rolling_SD"] = df["Age"].rolling(window=7).std()

# Display result
print(df[["JoiningYear", "Age", "Rolling_Mean", "Rolling_SD"]])

OUTPUT:
   JoiningYear  Age  Rolling_Mean  Rolling_SD
4396         2012   39           NaN         NaN
4394         2012   34           NaN         NaN
552          2012   26           NaN         NaN
549          2012   26           NaN         NaN
568          2012   26           NaN         NaN
...           ...  ...           ...         ...
1048         2018   25     27.285714    4.309458
2474         2018   27     26.428571    3.505098
1043         2018   27     26.857143    3.338092
4174         2018   35     28.142857    4.488079
1090         2018   27     28.428571    4.314979

[4653 rows x 4 columns]
