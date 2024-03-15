
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()

import numpy as np
from scipy import ndimage

def f(img):
    threshold = 0.75
    # Convert the image to a binary image based on the threshold
    binary_img = img > threshold
    
    # Label the connected regions in the binary image
    labeled_img, num_regions = ndimage.label(binary_img)
    
    # Return the number of regions
    return num_regions
    ### END SOLUTION
img = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
result = f(img)

with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
