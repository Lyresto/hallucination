fig, axs = plt.subplots(1, 2, figsize=(10, 4))
fig.suptitle('Y', fontsize=14)

axs[0].plot(x, y)
axs[0].set_title('Subplot 1')

axs[1].plot(x, y)
axs[1].set_title('Subplot 2')

plt.show()