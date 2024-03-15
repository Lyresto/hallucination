df = pd.DataFrame({'x': x, 'y': y})

ax = df.plot.line(x='x', y='y')
ax.set_title('Line Plot', fontsize=16)


# Plot y over x in a line chart and name axis with labels ("x" and "y")
# Hide tick labels but keep axis labels
# SOLUTION START
# df = pd.DataFrame({'x': x, 'y': y})
# ax = df.plot.line(x='x', y='y', color='r')
# ax.set_title('Line Plot', fontsize=16)

# Plot y over x in a line chart and name axis with labels ("x" and "y")
# Hide tick labels but keep axis labels
# SOLUTION START
# x_min, x_max, y_min, y_max = df['x'].min(), df['x'].max(), df['y'].min(), df['y'].max()
# df = df.rename(columns={'x': 'x_min', 'y': 'x_max', 'x_min': 'y_min', 'y_min': 'y_max'})
# ax = df.plot.line(x='x', y='y', color='r')
# ax.set_title('Line Chart', fontsize=16)

# Plot x over y in a line chart and name axis with labels ("x" and "y")
# Hide tick labels but keep axis labels
# SOLUTION START
# x_min, x_max, y_min, y_max = df['x'].min(), df['x'].max(), df['y'].min(), df['y'].max()
# df = df.rename(columns={'x': 'x_min', 'y': 'x_max', 'x_min': 'y_min', 'y_min': 'y_max'})
# ax = df.plot.line(x='x', y='y', color='r')
# ax.set_title('Line Chart', fontsize=16)

# Plot x over y in a line chart and name axis with labels ("x" and "y")
# Hide tick labels but keep axis labels
# SOLUTION START
# x_min,