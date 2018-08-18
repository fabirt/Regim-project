import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple


n_groups = 10

means_men = [20, 35, 30, 35, 27, 20, 35, 30, 35, 27]

means_women = [25, 32, 34, 20, 25, 25, 32, 34, 20, 25]

means_ex = [30, 10, 25, 40, 20, 30, 10, 25, 15, 20]

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.15

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = ax.bar(index, means_men, bar_width,
                alpha=opacity, color='b',
                error_kw=error_config,
                label='Men')

rects2 = ax.bar(index + bar_width, means_women, bar_width,
                alpha=opacity, color='r',
                error_kw=error_config,
                label='Women')

rects3 = ax.bar(index + bar_width*2, means_ex, bar_width,
                alpha=opacity, color='g',
                error_kw=error_config,
                label='Other')

ax.set_xlabel('Sample')
ax.set_ylabel('Scores')
ax.set_title('Image registration metric analysis')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'))
ax.legend()

fig.tight_layout()
plt.show()
