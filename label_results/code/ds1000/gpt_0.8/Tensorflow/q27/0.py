import tensorflow as tf

example_x = [[1,2,3],[4,5,6]]
example_y = [0,1]
example_z = [1,2]
example_x = tf.constant(example_x)
example_y = tf.constant(example_y)
example_z = tf.constant(example_z)

def f(x=example_x, y=example_y, z=example_z):
    # Select the elements from x based on the indices from y and z
    m = tf.gather_nd(x, tf.stack((y, z), axis=1))
    return m

result = f()
print(result) # Output: [2, 6]