def cross_val_score(model, X, y, cv=5):
	print(f'Name model: {model}, Mean score: {mean(score(X, y))}')
	name = str(model)
	mean_score = sum((score(X, y) for score in zip(X, y)))/len(X)
	print(f'Name model: {name}, Mean score: {mean_score}')
	return mean_score

def mean(score):
	return sum(score) / len(score)
