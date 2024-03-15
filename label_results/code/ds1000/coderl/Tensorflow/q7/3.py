import tensorflow as tf
ds = tf.data.Dataset.from_tensor_slices([10, 20, 30]).map(my_map_func=lambda i: [[i, i+1, i+2]])
ds = ds.flat_map(lambda x: [i for i in x])
element = ds.get_next()
result = []
with tf.compat.v1.Session() as sess:
	for _ in range(9):
		result.append(sess.run(element))
print(result)
