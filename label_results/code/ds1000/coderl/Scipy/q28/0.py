from math import ceil
def f(img = example_img):
	return ceil(sum(sum(img[i*512:(i+1)*512, j*512:(j+1)*512] > threshold * threshold for i in range(504)) / 4)
