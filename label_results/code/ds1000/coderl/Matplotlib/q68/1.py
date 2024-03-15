def lol(x, y):
	print(x, y)
	return f'{y[1]-x[1]:.2f}'

def line(x, y):
	return f'{lol(x, y)}'

df = pd.DataFrame({'x': x, 'y': y})
df['line'] = line(df['x'], df['y'])
df.plot(kind='line')
ax = df.plot(linewidth=2)
ax.set_title(f'Line Chart with {line(df['x'], df['y'])}')
ax.legend(loc='upper right')

# Solved on 23 Mar 2019 at 02:30AM.
