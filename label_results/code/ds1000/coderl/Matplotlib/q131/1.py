def pseries(y, x):
	return pd.Series(y, x)

def plot(ax, x, y, y2):
	for i in range(x.size):
		ax.plot(y[i:y2], y2)

def subplot(x, y, i):
	y2 = y[i]
	i += 1
	return pseries(y, x)

for i in range(2, 5):
	for j in range(2, 5):
		if i == 2 or j == 2:
			continue
		x = subplot(i, j, j)
		y = subplot(i, j, i)
		pplot(x, y, i, j)

	
# your code here
