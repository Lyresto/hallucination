from itertools import zip_longest

def downsample(arr, n):
	n = int(n)
	arr = list(arr)
	s = n // 2
	a = arr[:s] + arr[-s:]
	b = arr[:s]
	return a, b
	

def plot(x, y):
	ax = plt.gca()
	ax.bar(x, y, width=1)
	return ax.get_yaxis().get_majorticklines()[0]

def weighted_mean(df):
	w = 1.0 * len(df)
	df.cumsum().cumsum().plot(kind='bar', ax=plt.gca())
	return df.cumsum().cumsum() / w

df = pd.DataFrame({'x': x, 'y': y})
df = downsample(df['x'], n=10)
df = downsample(df['y'], n=10)
# df = weighted_mean(df)

ans = plot(df['x'], df['y'])
print(ans)
