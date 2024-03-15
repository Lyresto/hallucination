def my_map_func(i):
  return [i, i+1, i+2]

ds = tf.data.Dataset.from_tensor_slices(input)
ds = ds.flat_map(lambda x: tf.data.Dataset.from_tensor_slices(my_map_func(x)))
element = tf.compat.v1.data.make_one_shot_iterator(ds).get_next()
result = []
with tf.compat.v1.Session() as sess:
  for _ in range(9):
    result.append(sess.run(element))
