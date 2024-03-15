import tensorflow as tf
ds = tf.data.Dataset.from_tensor_slices(input)
ds = ds.flat_map(lambda i: [[i, i+1, i+2]] )
element = ds.get_next()
result = []
with tf.compat.v1.Session() as sess:
	for _ in range(9):
		result.append(sess.run(element))
print(result)
