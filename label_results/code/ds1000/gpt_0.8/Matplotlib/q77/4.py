fig, axs = plt.subplots(2, 1)
fig.suptitle("Y and Z")

axs[0].plot(x, y)
axs[0].set_title("Y")

axs[1].plot(z, a)
axs[1].set_title("Z")

plt.show()