```python
def f(lengths=example_lengths):
    max_length = max(lengths)
    mask = tf.sequence_mask(lengths, max_length, dtype=tf.int32)
    padded_mask = tf.pad(mask, [[0, 0], [0, max_length - tf.shape(mask)[1]]])
    return padded_mask
```
### END SOLUTION
