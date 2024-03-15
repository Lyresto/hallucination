fig, axes = plt.subplots(4, 4, figsize=(5, 5))
for i in range(4):
    for j in range(4):
        axes[i, j].plot(x, y)
        axes[i, j].set_xticks([])
        axes[i, j].set_yticks([])
plt.subplots_adjust(hspace=0.5, wspace=0.5)
plt.show()