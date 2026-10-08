import pandas as pd

df = pd.DataFrame({"station": ["Raval"], "temperature_c": [12.1]})
new_row = pd.DataFrame({"station": ["Gracia"], "temperature_c": [10.9]})
df = df.append(new_row, ignore_index=True)
print(df)
