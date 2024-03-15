import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel
import numpy as np
X, y = load_data()
clf = ExtraTreesClassifier(random_state=42)
clf = clf.fit(X, y)
