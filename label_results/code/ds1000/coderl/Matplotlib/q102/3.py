# https://www.matplotlib.org/examples/colormaps/colormap_reference.html

def heatmap(data):
	# Fill the diagonal with white
	data = np.fill_diagonal(data, value=0)
	# Set limits to be between 0 and 10
	xmax, xmin = min(data), max(data)
	ymax, ymin = min(data), max(data)
	# Plot the heatmap
	fig = plt.figure()
	ax = fig.add_axes([0, 0, 5, 5])
	ax.pcolormesh(data, cmap="jet", vmax=ymax, vmin=xmin)
	fig.savefig("colormap_example.png")

# Visualize the heatmap
heatmap(data)
