import tensorflow as tf
def f(lengths=example_lengths):
	print(lengths)
	x = []
	for i in lengths:
		x.append([0]*i)
	res = []
	for i in x:
		res.append(i+(i%2==1))
	return res
