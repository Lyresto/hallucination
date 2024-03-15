fig = plt.figure(figsize=(6, 6), dpi=80)
ax = fig.add_subplot(111, polar=True)
ax.bar(labels, height)
