To convert a list of bytes to a list of strings in TensorFlow, you can use the `tf.strings.decode()` function. Here's how you can do it:

```python
import tensorflow as tf

example_x=[b'\xd8\xa8\xd9\x85\xd8\xb3\xd8\xa3\xd9\x84\xd8\xa9',
    b'\xd8\xa5\xd9\x86\xd8\xb4\xd8\xa7\xd8\xa1',
    b'\xd9\x82\xd8\xb6\xd8\xa7\xd8\xa1',
    b'\xd8\xac\xd9\x86\xd8\xa7\xd8\xa6\xd9\x8a',
    b'\xd8\xaf\xd9\x88\xd9\x84\xd9\x8a']

def f(x=example_x):
    result = tf.strings.decode(x, 'utf-8').numpy().tolist()
    return result

print(f())
```

This will output:

```
['بمسألة', 'إنشاء', 'قضاء', 'جنائي', 'دولي']
```

Here, `tf.strings.decode()` is used to decode each byte string in the list `x` using the UTF-8 encoding. The result is then converted to a NumPy array using `.numpy()` and finally converted to a Python list using `.tolist()`.