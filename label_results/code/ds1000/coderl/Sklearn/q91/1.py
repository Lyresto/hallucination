import numpy as np
from sklearn.preprocessing import LabelEncoder
df = pd.read_csv('titanic.csv')
df['Sex'] = LabelEncoder.fit_transform(df['Sex'])
