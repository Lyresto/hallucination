ds = tf.data.Dataset.from_tensor_slices(input)
ds = ds.flat_map(lambda x: tf.data.Dataset.from_tensor_slices(my_map_func(x)))
element = ds.make_one_shot_iterator().get_next()
result = []
with tf.compat.v1.Session() as sess:
  for _ in range(9):
    result.append(sess.run(element))
