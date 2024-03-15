import numpy as np


def plot(t, x):
	return np.concatenate((x[:3], x[3:8]), axis=1).T
	
def legend(t, x):
	n, y = len(x), np.array(t)
	return (np.concatenate((y[:-n], y[-n:]), axis=1).T -
			np.concatenate((y[:-n], y[-n:]), axis=1))

t = np.arange(0, 20)
x = plot(t, t)
# print(x)
legend(t, x)
plt.show()
