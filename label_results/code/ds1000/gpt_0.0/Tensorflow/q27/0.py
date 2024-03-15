    indices = tf.stack([y,z], axis=1)
    m = tf.gather_nd(x, indices)
    return m
### END SOLUTION

print(f()) # Output: [2 6]