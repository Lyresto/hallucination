y1 = np.random.randint(0, 10, 10)
y2 = np.random.randint(0, 10, 10)
y3 = np.random.randint(0, 10, 10)

plt.plot(x, y1, linestyle='-', label='solid')
plt.plot(x, y2, linestyle='--', label='dashed')
plt.plot(x, y3, linestyle=':', label='dotted')

plt.legend()
plt.show()
