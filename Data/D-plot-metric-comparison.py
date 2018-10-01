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

mutual_info_data_norm = [float(i) / min(mutual_info_data) for i in mutual_info_data]
mse_data_norm = [min(mse_data) / float(i) for i in mse_data]

length = len(mse_data_norm)

mse_data_norm_organized = sorted(mse_data_norm, reverse=True)
order = [None] * length
for i in range(length):
    ref = mse_data_norm_organized[i]
    order[i] = mse_data_norm.index(ref)

mutual_info_data_norm_organized = [0] * length
for i in range(length):
    mutual_info_data_norm_organized[i] = mutual_info_data_norm[order[i]]

print(order)
print("{0}\n{1}".format(mutual_info_data_norm, mse_data_norm))

fig, ax = plt.subplots(1)

plt.plot(mutual_info_data_norm_organized)
plt.plot(mse_data_norm_organized)

ax.set_xlabel('Sample')
plt.xticks(list(range(0, 20)))
plt.legend(["Mutual information", "MSE"])
plt.title("Metric experiment comparison #1")
plt.ylim((0.2, 1.02))
fig.tight_layout()
plt.show()
