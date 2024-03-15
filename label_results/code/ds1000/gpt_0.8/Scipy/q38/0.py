import numpy as np
import scipy.spatial.distance

# Convert the array into a set of unique values
unique_values = np.unique(example_array)

# Create a list to store the pairwise distances
distances = []

# Calculate the pairwise distances between all unique values
for i in range(len(unique_values)):
    for j in range(i+1, len(unique_values)):
        # Get the indices of the current unique values
        indices_i = np.where(example_array == unique_values[i])
        indices_j = np.where(example_array == unique_values[j])
        
        # Get the coordinates of the current unique values
        coordinates_i = np.column_stack((indices_i[0], indices_i[1]))
        coordinates_j = np.column_stack((indices_j[0], indices_j[1]))
        
        # Calculate the pairwise distances between the coordinates
        pairwise_distances = scipy.spatial.distance.cdist(coordinates_i, coordinates_j, metric='euclidean')
        
        # Get the minimum distance from the pairwise distances
        min_distance = np.min(pairwise_distances)
        
        # Add the minimum distance to the distances list
        distances.append((unique_values[i], unique_values[j], min_distance))

# Convert the distances list into a numpy array
result = np.array(distances)
