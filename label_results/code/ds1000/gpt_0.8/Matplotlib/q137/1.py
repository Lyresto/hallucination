fig, axes = plt.subplots(4, 4, figsize=(5, 5))

for i in range(4):
    for j in range(4):
        axes[i, j].plot(x, y)
        axes[i, j].set_xticks(np.arange(0, 10, 2))
        axes[i, j].set_yticks(np.arange(0, 10, 2))
        axes[i, j].set_xlim(0, 10)
        axes[i, j].set_ylim(0, 10)
        if i != 3:
            axes[i, j].set_xticklabels([])
        if j != 0:
            axes[i, j].set_yticklabels([])

plt.tight_layout()
plt.show()
