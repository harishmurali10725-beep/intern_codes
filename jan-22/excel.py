
import pandas as pd
import json

with open('input.json', 'r') as file:
    data = json.load(file)
rows = data["inputs"]
columns = {key for row in rows for key in row.keys()}
output = {col: [] for col in columns}
for row in rows:
    for col in columns:
        output[col].append(row.get(col, " "))
df = pd.DataFrame(output)
try:
    df.to_excel("output2.xlsx", index=False)
    print("DataFrame successfully saved to 'output2.xlsx'")
except PermissionError:
    print("Error: The file is open in another program. Please close it and try again.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
