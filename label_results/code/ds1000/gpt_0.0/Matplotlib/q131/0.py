fig, axs = plt.subplots(2, 2, figsize=(15, 15))
for ax in axs.flatten():
    ax.plot(x, y)
plt.show()