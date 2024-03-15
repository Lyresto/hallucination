import polar_projection

fig, ax = plt.subplots()
polar_projection.polar_plot(ax, labels, height)

# plot several lines with different colors
ax.bar(2, 3, color='r', height=3)
ax.bar(1, 4, color='g', height=4)

# set x and y limits
ax.set_xbound(2, 2)
ax.set_ybound(1, 1)

# set plot title
ax.set_title('Polar Plot with Labels and Bar Height')

# show plot
plt.show()
