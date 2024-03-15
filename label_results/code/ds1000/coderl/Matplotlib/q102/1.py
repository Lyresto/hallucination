import numpy as np

N = 100
fig, ax = np.array([]).reshape(N, N), np.array([])
for x, y in data:
	ax[x, y] = np.array([i for i in range(x+1, x+5)]) + np.array([i for i in range(y+1, y+5)])
	fig.set_size_inches(5, 5)
	# SOLUTION END
