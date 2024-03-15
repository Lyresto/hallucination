import tensorflow as tf
ds = tf.data.Dataset.from_tensor_slices([0, 0, 0])
ds = ds.map(lambda x: [i for i in range(x)])
element = ds.make_one_shot_iterator().get_next()
result =... # put solution in this variable
