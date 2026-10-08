import pandas as pd

df = pd.read_csv("readings.csv")
print("Mean temperature:", df["temp_avg"].mean())
print("Hottest day:", df.loc[df["temp_avg"].idxmax(), "date"])
