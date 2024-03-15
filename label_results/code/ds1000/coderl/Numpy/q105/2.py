import numpy as np
import math
def generate(min,max,size):
	total = 0
	samples = np.array([])
	for i in range(size):
		mean = min + (i+1)*min/size
		std = max + (i+1)*(max-min)/size
		samples.append(math.log(std/mean))
	return samples
