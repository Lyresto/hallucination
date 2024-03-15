import pickle

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import tensorflow as tf

x,y,z = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))



def f(x,y,z):
    ### BEGIN SOLUTION
    import tensorflow as tf
    
    example_x = [[1,2,3],[4,5,6]]
    example_y = [0,1]
    example_z = [1,2]
    example_x = tf.constant(example_x)
    example_y = tf.constant(example_y)
    example_z = tf.constant(example_z)
    
    


def f(x=example_x, y=example_y, z=example_z):
    # Select the elements from x based on the indices from y and z
    m = tf.gather_nd(x, tf.stack((y, z), axis=1))
    return m

result = f()
print(result) # Output: [2, 6]


    ### END SOLUTION
result = f(x,y,z)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(result, f)