ds = tf.data.Dataset.from_tensor_slices(input)

def my_map_func(i):
  return [i, i+1, i+2]

ds = ds.flat_map(lambda x: tf.data.Dataset.from_tensor_slices(my_map_func(x)))

result = []
with tf.compat.v1.Session() as sess:
  for _ in range(9):
    result.append(sess.run(element))
