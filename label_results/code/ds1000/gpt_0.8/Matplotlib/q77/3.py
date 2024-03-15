fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

ax1.plot(x, y)
ax1.set_title('Y')

ax2.plot(z, a)
ax2.set_title('A')

fig.suptitle('Y and Z')

plt.tight_layout()
plt.show()