import pandas as pd

orders = pd.DataFrame({"customer_id": [1, 2, 3], "amount": [100, 50, 70]})
print("Total sales:", orders["amount"].sum())
