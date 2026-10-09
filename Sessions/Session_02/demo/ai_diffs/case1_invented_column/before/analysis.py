import pandas as pd

df = pd.read_csv("readings.csv")
print("Mean temperature:", df["temperature_c"].mean())
