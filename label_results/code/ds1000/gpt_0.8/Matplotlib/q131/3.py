fig, axs = plt.subplots(2, 2, figsize=(15, 15))

for i in range(2):
    for j in range(2):
        axs[i, j].plot(x, y)
        axs[i, j].set_title(f"Subplot {i+1}-{j+1}")

plt.show()