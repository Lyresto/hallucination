import argparse
import pickle


parser = argparse.ArgumentParser()
parser.add_argument("--test_case", type=int, default="1")
args = parser.parse_args()
import pandas as pd
import numpy as np
import sklearn

features = pickle.load(open(f"input/input{args.test_case}.pkl", "rb"))
def solve(features):
### BEGIN SOLUTION
    # Create a set of all unique features
    unique_features = set()
    for sample in features:
        unique_features.update(sample)
    
    # Create a dictionary to map each feature to a column index
    feature_to_index = {feature: i for i, feature in enumerate(sorted(unique_features))}
    
    # Create an empty 2D-array to store the one-hot encoded features
    num_samples = len(features)
    num_features = len(unique_features)
    one_hot_features = np.zeros((num_samples, num_features))
    
    # Fill in the one-hot encoded features
    for i, sample in enumerate(features):
        for feature in sample:
            j = feature_to_index[feature]
            one_hot_features[i, j] = 1
    
    # Convert the one-hot encoded features to a pandas DataFrame
    df = pd.DataFrame(one_hot_features, columns=sorted(unique_features))
    
    # Return the DataFrame as a numpy array
    return df.to_numpy()
    ### END SOLUTION
### END SOLUTION
new_features = solve(features)
with open('result/result_{}.pkl'.format(args.test_case), 'wb') as f:
    pickle.dump(new_features, f)
