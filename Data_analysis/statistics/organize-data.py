import json

JSON_FILE = "Data_norm.json"
METHODS = ("Restrictive", "Displacement")
METRICS = ("MI", "MSE")
METHOD_KEY = METHODS[0]

with open(JSON_FILE) as f:
    data = json.load(f)
    f.close()

header = "img mi mse"

print(header)

for num in range(20):
    value_mi = data[METHOD_KEY][METRICS[0]][num]
    value_mi = round(value_mi, 3)
    value_mse = data[METHOD_KEY][METRICS[1]][num]
    value_mse = round(value_mse, 3)
    print(num, value_mi, value_mse)
