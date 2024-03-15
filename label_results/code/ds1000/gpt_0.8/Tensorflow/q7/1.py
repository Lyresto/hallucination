ds = tf.data.Dataset.from_tensor_slices(input)
ds = ds.flat_map(lambda x: tf.data.Dataset.from_tensor_slices([x, x+1, x+2]))
result = list(ds.as_numpy_iterator())
