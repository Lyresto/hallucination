import pandas as pd

# x: number of x-axis
# y: number of y-axis
x_axis = pd.Series(x)
y_axis = pd.Series(y)

# calculate the difference between x-axis and y-axis
diffs = x_axis - y_axis

# plot the difference
plt.plot(diffs)

# show the plot
plt.show()
