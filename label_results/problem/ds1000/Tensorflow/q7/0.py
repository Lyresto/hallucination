def my_map_func(i):
    return [i, i+1, i+2]
ds = tf.data.Dataset.from_tensor_slices(input)
ds = ds.interleave(lambda x: tf.data.Dataset.from_tensor_slices(my_map_func(x)), cycle_length=len(input), num_parallel_calls=tf.data.experimental.AUTOTUNE)
result = list(ds.as_numpy_iterator())
