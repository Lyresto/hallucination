import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline

# Create a pipeline, where each estimator is a chain of steps
def create_clf(estimators):
	clf = Pipeline(steps=estimators)
	
	return clf
