# Create an empty dataframe with all possible features
all_features = list(set([f for sublist in features for f in sublist]))
df = pd.DataFrame(columns=all_features)

# Fill in the dataframe with 1s and 0s
for i, sample in enumerate(features):
    row = np.zeros(len(all_features))
    for feature in sample:
        row[all_features.index(feature)] = 1
    df.loc[i] = row

# Convert dataframe to numpy array
new_features = df.to_numpy()
