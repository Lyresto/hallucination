from itertools import zip_longest

fig, ax = plt.subplots()

for i, (label, h) in enumerate(zip_longest(labels, height)):
	ax.bar(i, h, label=label)

ax.set_ylim(0, 10)
ax.set_xticks(range(0, len(labels)))
ax.set_yticks(range(0, len(height)))

plt.show()
