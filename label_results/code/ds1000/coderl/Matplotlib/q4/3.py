import numpy as np

def linear_line(x, y):
	return np.poly1d(np.polyfit(x, y, 1))

def multi_line(x, y):
	return np.polyfit(x, y, 2)

# draw a line (with random y) for each different line style
fig = plt.figure()
for _ in range(10):
	ax = fig.add_subplot(1, 10, 1)
	p = multi_line(x, np.random.randn(10))
	for i in range(10):
		ax.plot(x, p(x), color='r', linewidth=2)
	ax.plot(x, linear_line(x, y), color='b', linewidth=1)
	ax.set_xlabel('x', size=10)
	ax.set_ylabel('y', size=10)
	# draw a line (with random y) for each different line style
	ax = fig.add_subplot(1, 10, 2)
	p = multi_line(x, np.random.randn(10))
	for i in range(10):
		ax.plot(x, p(x), color='g', linewidth=2)
	ax.plot(x, linear_line(x, y), color='b', linewidth=1)
	ax.set_xlabel('x', size=10)
	ax.set_ylabel('y', size=10)
	# draw a line (with random y) for each different line style
	ax = fig.add_subplot(1, 10, 3)
	p = multi_line(x, np.random.randn(10))
	for i in range(10):
		ax.plot(x, p(x), color='b', linewidth=2)
	ax.plot(x, multi_line(x, y), color='g', linewidth=1)
	ax.set_xlabel('x', size=10)
	ax.set_ylabel('y', size=10)
	# draw a line (with random y) for each different line style
	ax = fig.add_subplot(1, 10, 4)
	p =