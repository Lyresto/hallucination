plt.figure(figsize=(6, 6))
ax = plt.subplot(111, projection='polar')
bars = ax.bar(labels, height)

# Add values above bars
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 0.1, height,
            ha='center', va='bottom')

plt.show()