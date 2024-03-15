from sklearn.pipeline import Pipeline

def pipeline_named_steps(clf):
	return {k: v for k, v in clf.steps.items() if k in clf.steps}
