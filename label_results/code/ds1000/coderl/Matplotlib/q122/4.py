# SOLUTION END

# SOLUTION START
from itertools import chain

# Get x and y
x, y = np.array(zip(*[iter(x)]*10))

# Get the line by index
# Line by index is a line plot of y values from 0 to 10.
line, = plt.plot(y, x)
legend = ['Line']

# Adjust the line width
def adjust_len(lh):
	lh.set_linewidth(0.3)

# Add the line to the legend
def add_line(ax):
	ax.lines.append(line)

# Add a legend containing the line
def add_legend(ax):
	ax.legend([lh.line, line], ['Line', 'Line'])

# Add the legend to the current figure
def update_line(idx, val):
	ax.lines[idx].set_ydata(val)

# Update the y-data of the legend
def update_legend(idx, val):
	ax.legend([ax.lines[idx], ax.lines[idx].get_ydata()], ['Line', 'Line'])

# Update the x-data of the legend
def update_legend_x(idx, val):
	ax.legend([ax.lines[idx], ax.lines[idx].get_xdata()], ['Line', 'Line'])
	
# SOLUTION END

# Add the line and legend to the current figure
def plot_multiple(xs, ys):
	for idx, (x, y) in enumerate(zip(xs, ys)):
		add_line(ax=ax[idx])
		add_legend(ax=ax[idx])
		update_line(idx, y)
		update_legend(idx, y)

# Plot the y-data over the x-data
def plot(xs, ys):
	plot_multiple(xs, ys)
	return plt.gcf()

# Plot the legend
def legend(ax):
	ax.legend([line, line.get_ydata()], ['Line', 'Line'])
	return ax.legend(['Line', line.get_xdata()], ['Line', line.get