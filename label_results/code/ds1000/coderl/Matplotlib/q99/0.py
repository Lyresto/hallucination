def scatter_plot(x, y, color='r', marker='.'):
	# scatter_plot(x, y, color=color, marker='D')
	# scatter_plot(x, y, marker='^', color=color)
	# scatter_plot(x, y, marker='*', color=color)
	
	p = pd.Series([x, y], index=x)
	p.plot(marker=marker, color=color, lw=2)
	
	return p.plot(color=color)

# make a scatter plot with x and y and remove the edge of the marker.
# Use vertical line hatch to mark the marker

# SOLUTION START
import numpy as np

x = np.arange(10)
y = np.arange(10)
c = np.array([1,1,2,2,3])

p = scatter_plot(x, y, c, 'D')

# p = scatter_plot(x, y, c, 'x')
# p = scatter_plot(x, y, c, 'y')

# p = scatter_plot(x, y, c, '.')
# p = scatter_plot(x, y, c, '*')

# p = scatter_plot(x, y, c, 'r')
# p = scatter_plot(x, y, c, 'y')

# p = scatter_plot(x, y, c, '.')
# p = scatter_plot(x, y, c, 'x^')

# p = scatter_plot(x, y, c, '^')

# p = scatter_plot(x, y, c, 'D')

# p = scatter_plot(x, y, c, '^')
