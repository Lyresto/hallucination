import itertools

def add_legend(ax, _, left=1, top=1, right=1):
	for _ in range(left):
		ax.plot(y, x)
	for _ in range(top):
		ax.set_yticklabels(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
						  size="8", color="r")
	for _ in range(right):
		ax.set_xticklabels(["b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
						  size="8", color="g")

def one_plot(n, x):
	for _ in range(n):
		add_legend(plt.gca(), x, 0, n-1)
		plt.gca().set_xticklabels(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
						  size="8", color="g")
		#plt.gca().set_xticklabels(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
		#				 size="8", color="