import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
df = pd.read_csv('titanic.csv')
df['Sex'] = LabelEncoder.fit_transform(df['Sex'])
