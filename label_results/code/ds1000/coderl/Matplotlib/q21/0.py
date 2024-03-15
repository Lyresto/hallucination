import numpy as np

def sin(x):
	x = np.radians(x)
	return np.sin(x)

def cos(x):
	x = np.radians(x)
	return np.cos(x)

df = pd.DataFrame({'x': [0, 0, 2 * np.pi, 2 * np.pi * 2], 'y': [1, 1, sin(1), sin(2)]})
df.plot(kind='line', x='x', y='y', label='sin')
df.plot(kind='scatter', x='x', y='y', color='y', marker='o')
df.plot(kind='line', x='x', y='sin(x)', label='sin')
df.plot(kind='scatter', x='x', y='cos(x)', label='cos')
df.plot(kind='line', x='x', y='sin(2x)', label='sin')

df.x = df.x.rolling(2).mean()
df.y = df.y.rolling(2).mean()

df.x.plot(kind='line', x='x', y='y', label='sin')
df.y.plot(kind='scatter', x='x', y='sin(2x)', label='sin')

df.x = sin(df.x)
df.y = cos(df.x)

df.x.plot(kind='line', x='x', y='y', label='sin')
df.y.plot(kind='scatter', x='x', y='sin(2x)', label='sin')

df.x = sin(df.x)
df.y = cos(df.x)

df.x.plot(kind='line', x='x', y='y', label='sin')
df.y.plot(kind='scatter', x='x', y='cos(2x)', label='cos')

df.x = sin(df.x)
df.y = cos(df.x)

df.x.grid(True, which='minor')

df.y.grid(True, which='minor')

df.y