from itertools import chain

def p(*args):
	return chain.from_iterable(zip(*args))

df = pd.DataFrame({'X': x, 'Y': y})
ax = df.plot(x='X', y='Y', color='R')
ax.set_title('Two variables')
