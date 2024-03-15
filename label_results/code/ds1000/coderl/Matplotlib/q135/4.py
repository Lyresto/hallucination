def bar(b, y, x, yerr=0, c='r'):
	for x1, y1 in zip(b, y):
		ax.fill_between(x, y1**x1, y1**y1, color=c[yerr])

bar([2, 3, 4, 5], [1, 1, 2, 1], yerr=1, c='b')
bar([2, 3, 4, 5], [2, 1, 2, 1], xerr=1, yerr=1, c='r')

# Plot y errors only
ax.fill_between(box_position, 0, box_errors, color='yellow', alpha=0.5)

# SOLUTION END
