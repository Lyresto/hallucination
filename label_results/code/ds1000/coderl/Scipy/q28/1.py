import itertools

def f(img = example_img):
	values = img.flatten()
	res = []
	for i, j in itertools.product(range(len(values)), range(len(values))):
		if values[i][j] > threshold:
			res.append(i * j)
	return len(res)
