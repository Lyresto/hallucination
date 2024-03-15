import pandas as pd
import numpy as np

df = pd.DataFrame({'codes':[[71020], [77085], [36415], [99213, 99287], [99233, 99233, 99233]]})

# Get the maximum length of the lists
max_len = df['codes'].apply(len).max()

# Create empty columns with NaN values
columns = [f'code_{i}' for i in range(max_len)]
df[columns] = np.nan

# Fill the columns with values from the lists
for i in range(max_len):
    df[f'code_{i}'] = df['codes'].apply(lambda x: x[i] if len(x) > i else np.nan)

# Remove the original 'codes' column
df = df.drop('codes', axis=1)

result = df
END SOLUTION
print(result)