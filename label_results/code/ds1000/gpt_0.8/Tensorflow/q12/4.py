import tensorflow as tf

example_lengths = [4, 3, 5, 2]

def f(lengths=example_lengths):
    max_length = max(lengths)
    mask = tf.sequence_mask(lengths, maxlen=max_length)
    padded_mask = tf.pad(mask, [[0, 0], [0, 8 - max_length]])
    return padded_mask

result = f()
print(result)