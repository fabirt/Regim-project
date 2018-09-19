import json
import numpy as np
import matplotlib.pyplot as plt

JSON_FILE = "values.json"
CO = "CO"
MSE = "MS"
MI = "MI"

with open(JSON_FILE) as f:
    data = json.load(f)
    correlation_data = data[CO]
    mutual_info_data = data[MI]
    mse_data = data[MSE]
    f.close()

correlation_data_norm = [float(i)/min(correlation_data) for i in correlation_data]
mutual_info_data_norm = [float(i)/min(mutual_info_data) for i in mutual_info_data]
mse_data_norm = [min(mse_data)/float(i) for i in mse_data]
print("{0}\n{1}\n{2}".format(correlation_data_norm, mutual_info_data_norm, mse_data_norm))

plt.plot(correlation_data_norm)
plt.plot(mutual_info_data_norm)
plt.plot(mse_data_norm)
plt.xticks([0, 1, 2, 3, 4])
plt.legend(["Correlation", "Mutual information", "MSE"])
plt.title("Metric linearity")
plt.show()
