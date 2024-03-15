from sklearn.preprocessing import LabelEncoder
import numpy as np
from pandas import DataFrame
df = pd.read_csv('data.csv')
df['Sex'] = LabelEncoder.fit_transform(df['Sex'])
