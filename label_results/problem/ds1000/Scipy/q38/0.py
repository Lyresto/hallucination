# First, we need to create a list of all unique IDs in the array
unique_ids = np.unique(example_array)

# Then, we can create a dictionary to store the coordinates of each ID patch
id_coords = {}
for id in unique_ids:
    id_coords[id] = np.argwhere(example_array == id)

# Next, we can use the cdist function to calculate pairwise Euclidean distances between all patches
distances = scipy.spatial.distance.cdist(id_coords[unique_ids[0]], id_coords[unique_ids[1]], 'euclidean')

for i in range(1, len(unique_ids)):
    for j in range(i):
        new_distances = scipy.spatial.distance.cdist(id_coords[unique_ids[i]], id_coords[unique_ids[j]], 'euclidean')
        distances = np.vstack((distances, new_distances))

# Finally, we can create a N*N array in the form of "from ID, to ID, distance"
result = np.zeros((len(distances), 3))
count = 0
for i in range(len(unique_ids)):
    for j in range(i):
        result[count:count+len(id_coords[unique_ids[i]])*len(id_coords[unique_ids[j]]), 0] = unique_ids[i]
        result[count:count+len(id_coords[unique_ids[i]])*len(id_coords[unique_ids[j]]), 1] = unique_ids[j]
        result[count:count+len(id_coords[unique_ids[i]])*len(id_coords[unique_ids[j]]), 2] = distances[count:count+len(id_coords[unique_ids[i]])*len(id_coords[unique_ids[j]]), :].flatten()
        count += len(id_coords[unique_ids[i]])*len(id_coords[unique_ids[j]])

# Sort the results by distance
result = result[result[:, 2].argsort()]

# Print the results
print(result)
