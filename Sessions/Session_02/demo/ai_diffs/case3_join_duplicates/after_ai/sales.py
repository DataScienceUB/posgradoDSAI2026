import pandas as pd

orders = pd.DataFrame({"customer_id": [1, 2, 3], "amount": [100, 50, 70]})
customers = pd.DataFrame({"customer_id": [1, 1, 2, 3], "city": ["BCN", "BCN", "Girona", "Lleida"]})  # id 1 appears twice!
merged = orders.merge(customers, on="customer_id")
print("Total sales:", merged["amount"].sum())
