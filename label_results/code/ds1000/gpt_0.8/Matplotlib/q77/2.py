fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))

# plot y over x in the first subplot
ax1.plot(x, y)
ax1.set_title('Y over X')

# plot z over a in the second subplot
ax2.plot(a, z)
ax2.set_title('Z over A')

# set main title
fig.suptitle('Y and Z')

plt.show()