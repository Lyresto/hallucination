import pandas as pd

# Group the DataFrame by UserId
grouped = df.groupby('UserId')

# Initialize an empty list to store the altered rows
altered_rows = []

# Iterate through each group
for _, group in grouped:
    # Randomly select 20% of rows in the group
    sample_rows = group.sample(frac=0.2, random_state=0)
    
    # Set the Quantity column of the selected rows to zero
    sample_rows['Quantity'] = 0
    
    # Append the altered rows to the list
    altered_rows.append(sample_rows)
    
# Concatenate the altered rows back into a single DataFrame
df = pd.concat([df] + altered_rows)

# Sort the DataFrame by the index to restore the original order
df = df.sort_index()

# Reset the index
df = df.reset_index(drop=True)
