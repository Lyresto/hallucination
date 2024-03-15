fig, axs = plt.subplots(4, 4, figsize=(5, 5))

for i in range(4):
    for j in range(4):
        axs[i, j].plot(x, y)
        axs[i, j].set_xticks([])
        axs[i, j].set_yticks([])
        axs[i, j].set_xlim(0, 9)
        axs[i, j].set_ylim(0, 9)

plt.subplots_adjust(hspace=0.5, wspace=0.5)
plt.show()
