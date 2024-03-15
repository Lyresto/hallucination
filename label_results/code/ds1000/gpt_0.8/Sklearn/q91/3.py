import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the data
df = pd.read_csv('titanic.csv')

# Create an instance of the LabelEncoder
le = LabelEncoder()

# Fit and transform the 'Sex' column
df['Sex'] = le.fit_transform(df['Sex'])

# Check the transformed 'Sex' column
print(df['Sex'])
