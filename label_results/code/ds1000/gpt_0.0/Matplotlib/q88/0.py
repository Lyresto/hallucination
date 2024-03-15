# create a second x axis with the same range as the first one
ax2 = ax.twiny()
ax2.set_xlim(ax.get_xlim())

# set the tick positions and labels for the second x axis
ax2.set_xticks([2, 4, 6, 8])
ax2.set_xticklabels(["second", "4", "6", "8"])

# hide the first x axis ticks and labels
ax.tick_params(axis='x', which='both', length=0)

# add a label for the second x axis
ax2.set_xlabel("Time (seconds)")

# plot the data
ax.plot(y, x)

