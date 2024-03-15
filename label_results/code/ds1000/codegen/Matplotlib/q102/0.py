xlim = [0, 5]
ylim = [1, 4]

plt.figure(figsize=(10, 10))
plt.imshow(data, cmap='hot', interpolation='nearest',
           extent=[xlim[0], xlim[1], ylim[0], ylim[1]], aspect='auto')
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Heatmap of data')
plt.show()
#