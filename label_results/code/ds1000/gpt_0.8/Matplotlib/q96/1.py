fig, axs = plt.subplots(1, 2, figsize=(10, 5))
fig.suptitle("Figure")

axs[0].plot(x, y)
axs[0].set_title("Subplot 1")
axs[0].set_xlabel("x")
axs[0].set_ylabel("y")

axs[1].plot(x, y)
axs[1].set_title("Subplot 2")
axs[1].set_xlabel("x")
axs[1].set_ylabel("y")

plt.show()
