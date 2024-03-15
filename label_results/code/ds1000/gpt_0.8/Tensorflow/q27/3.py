m = tf.gather_nd(x, tf.stack((y, z), axis=1))
    ### END SOLUTION
    return m

print(f())