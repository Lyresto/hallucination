import numpy as np

def scatter(x, y, z, a):
	f1, f2 = np.meshgrid(x, y, z, a)
	return (f1**2 + f2**2).reshape(10, 10)

df = pd.DataFrame({'x': x, 'y': y, 'z': z, 'a': a})
# plot first axis
ax1 = df['y'].plot.barh(z=0)
# plot second axis
ax2 = df['z'].plot.barh(x=0)
ax1.set_title('Z')
ax2.set_title('X')


# SOLUTION END
