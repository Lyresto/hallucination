fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].plot(x, y, 'o', label='y')
ax[0].plot(x, z, 'o', label='z')
ax[0].set_title('Y and Z')
ax[0].legend()

ax[1].plot(x, a, 'o', label='a')
ax[1].set_title('A')
ax[1].legend()

#