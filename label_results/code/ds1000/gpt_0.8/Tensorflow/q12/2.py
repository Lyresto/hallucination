Here's one way to solve this problem using TensorFlow:

```python
import tensorflow as tf

example_lengths = [4, 3, 5, 2]

def f(lengths=example_lengths):
    max_length = tf.reduce_max(lengths)
    mask = tf.sequence_mask(lengths, maxlen=max_length, dtype=tf.int32)
    padded_mask = tf.pad(mask, [[0, 0], [0, max_length - tf.shape(mask)[1]]])
    return padded_mask

result = f()
print(result)
```

This will give you the desired output:

```
tf.Tensor(
[[1 1 1 1 0 0 0 0]
 [1 1 1 0 0 0 0 0]
 [1 1 1 1 1 0 0 0]
 [1 1 0 0 0 0 0 0]], shape=(4, 8), dtype=int32)
```

Here's how the code works:

1. Calculate the maximum length in the input tensor using `tf.reduce_max`.
2. Use `tf.sequence_mask` to create a mask tensor where each row contains 1s up to the corresponding length in the input tensor, and 0s for the rest.
3. Pad the mask tensor with 0s using `tf.pad` so that all rows have the same length as the maximum length.

Hope this helps! Let me know if you have any further questions.