y1 = np.random.randint(0, 10, size=10)
y2 = np.random.randint(0, 10, size=10)
y3 = np.random.randint(0, 10, size=10)
y4 = np.random.randint(0, 10, size=10)

plt.plot(x, y1, linestyle="-", label="Solid Line")
plt.plot(x, y2, linestyle="--", label="Dashed Line")
plt.plot(x, y3, linestyle="-.", label="Dash-dot Line")
plt.plot(x, y4, linestyle=":", label="Dotted Line")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Different Line Styles")
plt.legend()

plt.show()
