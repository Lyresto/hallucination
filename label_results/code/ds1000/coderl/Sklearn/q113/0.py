import numpy as np
import pandas as pd

def isit(X, Y, model):
	return np.sum((Y - model.predict(X)) ** 2, axis = 0)

def save_data():
	return pd.Series({'weights':isit(X,Y,fitted_model),'means':isit(X,Y,fitted_model.mean()),'covs':isit(X,Y,fitted_model.cov())})
