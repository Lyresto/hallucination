result = tf.gather_nd(x, tf.stack((y, z), axis=1))
### END SOLUTION
    return result

m = f()
print(m)  # Output: [2 6]