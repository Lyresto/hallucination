import tensorflow as tf

lengths = [4, 3, 5, 2]

max_length = max(lengths)
total_length = 8

mask = tf.sequence_mask(lengths, maxlen=max_length, dtype=tf.int32) # Create a mask of 1s and 0s
padding = tf.zeros([len(lengths), total_length - max_length], dtype=tf.int32) # Create padding of 1s

result = tf.concat([mask, padding], axis=1) # Concatenate mask and padding

print(result)
