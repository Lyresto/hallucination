plt.plot(x, x, 'o', color='red', label='Original')
plt.plot(x, x + np.random.randn(len(x)), '-', color='blue', label='Random')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Random line')
plt.show()
#