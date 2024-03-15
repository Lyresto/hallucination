y1 = np.random.randint(low=0, high=10, size=10)
y2 = np.random.randint(low=0, high=10, size=10)
y3 = np.random.randint(low=0, high=10, size=10)
y4 = np.random.randint(low=0, high=10, size=10)

plt.plot(x, y1, linestyle='-', label='solid')
plt.plot(x, y2, linestyle='--', label='dashed')
plt.plot(x, y3, linestyle='-.', label='dashdot')
plt.plot(x, y4, linestyle=':', label='dotted')

plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Line Plot with Different Line Styles')

plt.show()
