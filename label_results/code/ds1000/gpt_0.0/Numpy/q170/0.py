# Convert strings to float values
A = [float(x) if x != 'np.inf' else np.inf for x in A]
# Calculate mean
AVG = np.mean(A)
