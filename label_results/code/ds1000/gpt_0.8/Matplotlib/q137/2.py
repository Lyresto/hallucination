fig, axes = plt.subplots(4, 4, figsize=(5, 5))

for i in range(4):
    for j in range(4):
        axes[i, j].plot(x, y)
        axes[i, j].set_xticks(x)
        axes[i, j].set_yticks(y)
        axes[i, j].set_xlabel('x')
        axes[i, j].set_ylabel('y')

plt.tight_layout()
plt.show()
