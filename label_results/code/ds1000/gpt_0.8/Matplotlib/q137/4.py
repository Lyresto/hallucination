fig, axs = plt.subplots(4, 4, figsize=(5, 5), sharex=True, sharey=True)

for i in range(4):
    for j in range(4):
        axs[i, j].plot(x, y)
        axs[i, j].set_xticks(x)
        axs[i, j].set_yticks(y)
        axs[i, j].tick_params(axis='both', labelsize=8)
        axs[i, j].set_xlabel('X')
        axs[i, j].set_ylabel('Y')

plt.tight_layout()
plt.show()