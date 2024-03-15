import numpy as np
import seaborn as sns

df = pd.read_csv('penguins.csv')
df['bill_length_mm'] = df['bill_length_mm'] * 1000
df['bill_depth_mm'] = df['bill_depth_mm'] * 1000
df['flipper_length_mm'] = df['flipper_length_mm'] * 1000
df['body_mass_g'] = df['body_mass_g'] * 1000

sns.pointplot(x='bill_length_mm', y='bill_depth_mm', hue='body_mass_g')
