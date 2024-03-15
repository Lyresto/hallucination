def proba(X,y,x):
	import numpy as np
	pred=[]
	for i in range(len(X)):
		pred.append(1/(1+np.exp(-X[i])) )
	return pd.Series(pred,y)

def linear_svc(X,y,x):
	import numpy as np
	model=svm.LinearSVC(penalty='l1',C=1)
	return pd.Series(model.predict(x),y)
