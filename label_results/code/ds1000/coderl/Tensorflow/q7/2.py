def my_map_func(i):
	return [[i, i+1, i+2]]       # Fyi [[i], [i+1], [i+2]] throws an exception
ds = tf.data.Dataset.from_tensor_slices(input)
ds = ds.map(map_func=lambda input: tf.compat.v1.py_func(
  func=my_map_func, inp=[input], Tout=[tf.int64]
))
element = tf.compat.v1.data.make_one_shot_iterator(ds).get_next()
result = []
with tf.compat.v1.Session() as sess:
	for _ in range(9):
		result.append(sess.run(element))
print(result)
