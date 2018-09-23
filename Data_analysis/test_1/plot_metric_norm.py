import json
import matplotlib.pyplot as plt

JSON_FILE = "test1_values.json"
MS = "MS"
MI = "MI"

with open(JSON_FILE) as f:
    data = json.load(f)
    mutual_info_data = data[MI]
    mse_data = data[MS]
    f.close()

mutual_info_data_norm = [float(i)/min(mutual_info_data) for i in mutual_info_data]
mse_data_norm = [min(mse_data)/float(i) for i in mse_data]
print("{0}\n{1}".format(mutual_info_data_norm, mse_data_norm))

plt.plot(mutual_info_data_norm)
plt.plot(mse_data_norm)
plt.xticks(list(range(0, 20)))
plt.legend(["Mutual information", "MSE"])
plt.title("Metric experiment #1")
plt.show()
