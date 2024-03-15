import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the data
df = pd.read_csv('data.csv')

# Create an instance of LabelEncoder
le = LabelEncoder()

# Fit and transform the 'Sex' column
df['Sex'] = le.fit_transform(df['Sex'])

# Print the transformed dataframe
print(df)
