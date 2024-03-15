import numpy as np
import scipy.spatial.distance

def f(example_array):
    # Get the unique IDs in the array
    unique_ids = np.unique(example_array)
    
    # Initialize an empty array to store the pairwise distances
    distances = np.zeros((len(unique_ids), len(unique_ids)))
    
    # Iterate over the unique IDs
    for i, id1 in enumerate(unique_ids):
        for j, id2 in enumerate(unique_ids):
            # Get the coordinates of all cells with ID id1
            coords1 = np.argwhere(example_array == id1)
            
            # Get the coordinates of all cells with ID id2
            coords2 = np.argwhere(example_array == id2)
            
            # Calculate the pairwise distances between the two sets of coordinates
            pairwise_distances = scipy.spatial.distance.cdist(coords1, coords2, metric='euclidean')
            
            # Get the minimum distance
            min_distance = pairwise_distances.min()
            
            # Store the minimum distance in the distances array
            distances[i, j] = min_distance
    
    return distances

# Test the function
result = f(example_array)
print(result)