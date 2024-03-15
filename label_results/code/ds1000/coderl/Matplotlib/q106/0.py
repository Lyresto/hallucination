from itertools import zip_longest

fig, ax = plt.subplots()
ax.bar(zip_longest(range(len(labels)), height, labels=labels, color='r'))
ax.grid(True)

# Plot different bar positions
# ax.plot(zip_longest(range(len(labels)), height, label='a')
# ax.plot(zip_longest(range(len(labels)), height, label='b')
#... by using polar projection, each bar will have different x-coordinates.

# plot another bar with different x-coordinates, coloring each bar according to height
ax.bar(zip_longest(range(len(labels)), (height[0] + 1), color='g'), zip_longest(range(len(labels)), height, color='b'), label='a')
ax.bar(zip_longest(range(len(labels)), (height[1] + 1), color='r'), zip_longest(range(len(labels)), height, color='g'), label='b')

# Remove y-axis labels
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

# Add x-axis title and tick labels
ax.set_xlabel('Bar Height')
ax.set_ylabel('Label')

# Show plot
plt.show()
