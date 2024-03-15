# IMPORTANT: y should be a column of x.
# Use the `matplotlib.colors` library to color the points.
# You can use any number of colors for x.

y_values = pd.Series(y).plot(x, color='#AAAAAA')

# Plot a line of x values with a legend.
# Use the `matplotlib.lines` library to draw lines.
x_lines = pd.DataFrame({'x': x})
y_lines = pd.DataFrame({'y': y})
x_lines.plot(x, y, linestyle='-', label='y')
y_lines.plot(x, y, linestyle='', label='x')

# Use `set_ylim` to set the y-axis limits.
y_lines['y'] = y_lines['y'].shift(1)
y_lines.set_ylim(0, 10)

# Use `set_xticks` to set the x-axis ticks.
x_lines['x'] = x_lines['x'].shift(1)
x_lines.set_xticks([0, 1])

# Add a legend with one line at a time.
ax = x_lines.plot(x_lines['x'], y_lines['y'], linewidth=2)

# Remove the axis line by default.
ax.set_xlabel('x')
ax.set_ylabel('y')

# Remove the legend by default.
ax.legend(loc='best')

# Show the plot.
plt.show()
