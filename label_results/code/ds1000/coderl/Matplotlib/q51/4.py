# x - int, y - int
# SOLUTION START
df = pd.DataFrame({'x': x, 'y': y})

# calculate mean of each column and add to the plot
mean = df.mean()
for i in range(10):
	df.plot('x', 'y', label=str(i))
	# add a line, and label by the y-value
	df.plot('x', mean.y + i * mean.x, 'o', color='r', label='mean')

# specify x & y limits
df.plot('x', 'y', xlim=(0, 10), ylim=(0, 10))

# specify x labels
df.plot('x', 'y', label='x')

# specify y-label
df.plot('y', 'x', label='y')

# no x labels and no y labels
df.plot('x', 'y', label='', x_label=None, y_label=None)

# show the plot
plt.show()
