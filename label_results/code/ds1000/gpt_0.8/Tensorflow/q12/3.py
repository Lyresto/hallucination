import tensorflow as tf

example_lengths = [4, 3, 5, 2]
def f(lengths=example_lengths):
    # Get the maximum length from the input lengths
    max_length = tf.reduce_max(lengths)
    
    # Create a tensor with the shape [batch_size, max_length]
    mask = tf.sequence_mask(lengths, maxlen=max_length, dtype=tf.int32)
    
    # Pad the mask tensor with 0s to a total length of 8
    padded_mask = tf.pad(mask, paddings=[[0, 0], [0, 8 - max_length]])
    
    return padded_mask

# Test the function
result = f()
print(result)