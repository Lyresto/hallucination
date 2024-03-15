
import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default=1)
args = parser.parse_args()
import numpy as np
import scipy.spatial.distance
example_array = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))



def f(example_array):
    import numpy as np
    import scipy.spatial.distance
    
    


def f(example_array):
    # Find unique IDs in the array
    unique_ids = np.unique(example_array)

    # Create an empty array to store the pairwise distances
    pairwise_distances = np.zeros((len(unique_ids), len(unique_ids)))

    # Iterate over each unique ID
    for i, id1 in enumerate(unique_ids):
        # Get the indices where the ID occurs in the array
        indices1 = np.where(example_array == id1)

        # Iterate over each unique ID again
        for j, id2 in enumerate(unique_ids):
            # Get the indices where the ID occurs in the array
            indices2 = np.where(example_array == id2)

            # Calculate the pairwise Euclidean distance between the two sets of indices
            distance = scipy.spatial.distance.cdist(indices1, indices2, metric='euclidean').min()

            # Store the distance in the pairwise_distances array
            pairwise_distances[i, j] = distance

    # Create a list to store the results
    results = []

    # Iterate over each pair of unique IDs and their corresponding distances
    for i, id1 in enumerate(unique_ids):
        for j, id2 in enumerate(unique_ids):
            # Skip if the IDs are the same or the distance is zero
            if id1 == id2 or pairwise_distances[i, j] == 0:
                continue

            # Append the pair of IDs and the corresponding distance to the results list
            results.append([id1, id2, pairwise_distances[i, j]])

    return results

# Test the function with the given example array
result = f(example_array)

# Print the results
for pair in result:
    print(f"From ID: {pair[0]}, To ID: {pair[1]}, Distance: {pair[2]}")




result = f(example_array)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as file:
    pickle.dump(result, file)
