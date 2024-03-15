fig, axs = plt.subplots(2, 2, figsize=(15, 15))

for ax in axs.flat:
    ax.plot(x, y)
    ax.set_xlabel('x')
    ax.set_ylabel('y')

plt.show()