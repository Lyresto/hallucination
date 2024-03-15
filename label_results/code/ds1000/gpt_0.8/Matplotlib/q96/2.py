fig, axes = plt.subplots(1, 2, figsize=(10, 5))
fig.suptitle('Figure')

axes[0].plot(x, y)
axes[0].set_title('Plot 1')

axes[1].plot(x, y)
axes[1].set_title('Plot 2')

plt.show()