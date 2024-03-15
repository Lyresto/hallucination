import numpy as np
import pandas as pd

def predict(X):
	#your code here
	weights = fitted_model.predict(X)
	means = fitted_model.mean(X)
	covs = fitted_model.cov(X)
	return (weights, means, covs)

def load_data():
	#your code here
	import numpy as np
	fitted_model = np.load('sklearn_model.npz')
	return fitted_model
