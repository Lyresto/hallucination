import math

# Calculate the number of NaN values to fill with 0 and 1
num_nan = df['Column_x'].isna().sum()
num_fill_0 = math.floor(num_nan/2)
num_fill_1 = math.ceil(num_nan/2)

# Fill the NaN values with 0 and 1
df['Column_x'].fillna(0, limit=num_fill_0, inplace=True)
df['Column_x'].fillna(1, limit=num_fill_1, inplace=True)
