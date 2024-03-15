# Get the current x-axis tick labels
labels = [item.get_text() for item in ax.get_xticklabels()]

# Change the second tick label to "second"
labels[1] = "second"

# Set the new tick labels
ax.set_xticklabels(labels)
