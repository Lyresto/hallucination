def proba(X,y,x_predict):
	print(X)
	print(y)
	print(x_predict)
	model=svm.LinearSVC(penalty='l1',C=1)
	proba=[]
	for i in range(len(x_predict)):
		predict=model.predict(x_predict[i])
		proba.append(1/(1+np.exp(-predict)))
	return proba
