
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()

import numpy as np
import scipy.ndimage
square = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
import numpy as np
from scipy.ndimage import label, generate_binary_structure

# Define a binary structure for labeling connected components
structure = generate_binary_structure(2, 2)

# Label connected components in the image array
labeled_array, num_features = label(square > 0, structure)

# Iterate over each connected component
for i in range(1, num_features + 1):
    # Find the coordinates of the connected component
    component_coords = np.argwhere(labeled_array == i)
    
    # Check if the connected component is completely surrounded by zeros
    surrounded_by_zeros = True
    for coord in component_coords:
        x, y = coord
        neighbors = labeled_array[x-1:x+2, y-1:y+2]
        if np.any(neighbors != i):
            surrounded_by_zeros = False
            break
    
    # If the connected component is completely surrounded by zeros, set it to zero in the original array
    if surrounded_by_zeros:
        square[component_coords[:, 0], component_coords[:, 1]] = 0




#print(square)


with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(square, f)
