import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import tensorflow as tf

x = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))



def f(x):
    ### BEGIN SOLUTION
    import tensorflow as tf
    
    example_x=[b'\xd8\xa8\xd9\x85\xd8\xb3\xd8\xa3\xd9\x84\xd8\xa9',
        b'\xd8\xa5\xd9\x86\xd8\xb4\xd8\xa7\xd8\xa1',
        b'\xd9\x82\xd8\xb6\xd8\xa7\xd8\xa1',
        b'\xd8\xac\xd9\x86\xd8\xa7\xd8\xa6\xd9\x8a',
        b'\xd8\xaf\xd9\x88\xd9\x84\xd9\x8a']
    
    


def f(x=example_x):
    # Convert the list of bytes to TensorFlow strings
    tf_strings = tf.constant(x, dtype=tf.string)

    # Decode the TensorFlow strings to Unicode strings
    decoded_strings = tf.strings.decode(tf_strings, encoding='utf-8')

    # Return the result as a Python list
    return list(decoded_strings.numpy())

# Test the function
result = f()
print(result)



    ### END SOLUTION
result = f(x)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)