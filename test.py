import pandas as pd

data = pd.read_excel('./cache/cars.xlsx', sheet_name="Sheet1")

print(data)