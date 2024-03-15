import math
def f(img = example_img):
	return math.floor((img * 255).sum(1))
