fig, ax = plt.subplots(1, 2, figsize=(5, 5))

ax[0].plot(x, y, 'o')
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')
ax[0].set_title('Plot 1')

ax[1].plot(x, y, 'o')
ax[1].set_xlabel('x')
ax[1].set_ylabel('y')
ax[1].set_title('Plot 2')

plt.show()
#