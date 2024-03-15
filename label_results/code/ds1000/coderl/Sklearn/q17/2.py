import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline

def named_steps(clf):
	for k,v in clf.steps.items():
		if k not in clf.named_steps():
			yield k,v
