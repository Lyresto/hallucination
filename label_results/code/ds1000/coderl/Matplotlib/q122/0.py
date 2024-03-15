import numpy as np


x = np.arange(10)
y = np.arange(10)

df = pd.DataFrame({'x': x, 'y': y})

ax = df.plot.bar(y, x)
ax.set_yticklabels(['Line'])

plt.show()
