fig, axs = plt.subplots(2, 2, figsize=(15, 15))

for ax in axs.flat:
    ax.plot(x, y)

plt.show()