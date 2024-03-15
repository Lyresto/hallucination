from math import factorial as fac

def line(x, y):
	return fac(x ** 2 + y ** 2) / (2 * fac(x))

df = pd.DataFrame({'x': x, 'y': y})

ax1 = df.plot.line(x='x', y='y')
ax2 = df.plot.line(x='y', y='x')

ax1.set_xlabel('x')
ax2.set_ylabel('y')

plt.show()
