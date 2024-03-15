# Convert array to list of unique IDs
unique_ids = np.unique(example_array)[1:]

# Create empty distance matrix
dist_matrix = np.zeros((len(unique_ids), len(unique_ids)))

# Loop through all unique ID pairs and calculate pairwise distances
for i in range(len(unique_ids)):
    for j in range(i+1, len(unique_ids)):
        # Get indices of cells with each ID
        idx_i = np.argwhere(example_array == unique_ids[i])
        idx_j = np.argwhere(example_array == unique_ids[j])
        # Calculate pairwise distances between all cells with each ID
        dists = scipy.spatial.distance.cdist(idx_i, idx_j, metric='euclidean')
        # Get minimum distance between all pairs of cells
        min_dist = np.min(dists)
        # Add minimum distance to distance matrix
        dist_matrix[i,j] = min_dist
        dist_matrix[j,i] = min_dist

# Create list of all unique ID pairs
id_pairs = [(unique_ids[i], unique_ids[j]) for i in range(len(unique_ids)) for j in range(i+1, len(unique_ids))]

# Create list of all pairwise distances
distances = [dist_matrix[i,j] for i in range(len(unique_ids)) for j in range(i+1, len(unique_ids))]

# Combine ID pairs and distances into final output array
output_array = np.column_stack((id_pairs, distances))

return output_array
### END SOLUTION