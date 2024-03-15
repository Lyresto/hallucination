import pandas as pd

df = pd.DataFrame({'X': x, 'Y': y})

# make 2 side-by-side subplots, and in each subplot, plot y over x
# Title each subplot as "Y"
# SOLUTION START
def side_by_side(ax):
	df['Y'] = ax.plot(df['X'], df['Y'])[0]
	for i in range(1, 5):
		ax.axvline(x, y, color='r', alpha=0.5)
		ax.axhline(x, y, color='b', alpha=0.5)
	
# Make the two plots
side_by_side(plt.subplot(2, 1, 1))
side_by_side(plt.subplot(2, 1, 2))
side_by_side(plt.subplot(2, 1, 3))
side_by_side(plt.subplot(2, 1, 4))
side_by_side(plt.subplot(2, 1, 5))
side_by_side(plt.subplot(2, 1, 6))
side_by_side(plt.subplot(2, 1, 7))
side_by_side(plt.subplot(2, 1, 8))
side_by_side(plt.subplot(2, 1, 9))

# Show the plots
plt.show()
