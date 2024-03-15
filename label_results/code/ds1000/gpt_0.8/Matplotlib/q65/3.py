fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

ax1.plot(x, y)
ax1.set_title('Y')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')

ax2.plot(x, y)
ax2.set_title('Y')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')

plt.show()