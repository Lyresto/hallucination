fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 8))

ax1.plot(x, y)
ax1.set_title('Y')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')

ax2.plot(a, z)
ax2.set_title('Z')
ax2.set_xlabel('A')
ax2.set_ylabel('Z')

fig.suptitle('Y and Z')

plt.tight_layout()
plt.show()