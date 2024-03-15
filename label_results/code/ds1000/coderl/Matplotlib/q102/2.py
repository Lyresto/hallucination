import numpy as np
import itertools as it


def plot(data, x_min, x_max, y_min, y_max, figsize):
	# Set the colors.
	# (1) Left edge is gray (0) and right edge is black
	# (2) Top edge is white (1) and bottom edge is grey (2)
	# (3) Bottom edge is black (3) and left edge is grey (4)
	# SOLUTION START
	colors = np.ones((10, 10))
	# Draw the heatmap.
	for i, j in it.product(range(0, 10), range(0, 10)):
		# Draw a rectangle.
		x, y = i * x_min, j * y_min
		colors[i, j] = 0 if i == j else 4
		colors[i, j] = 4 if i == j == 4 else 3
		colors[i, j] = 3 if i == j == 3 else 2
		# Draw a vertical line.
		colors[i, j] = 1 if i == j == 2 else 0
		colors[i, j] = 1 if i == j == 0 else 2
		# Save the image.
		plt.imshow(colors, interpolation='nearest', extent=(x, y, x_max, y_max),
					cmap='YlGnBu_r')
	# Set the width and height of the plots.
	plt.suptitle(' heatmap'+ str(x_min) +'' + str(y_min) +'' + str(x_max) +'' + str(y_max),
				size=figsize)
	# Show the plots.
	plt.show()
