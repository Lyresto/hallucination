import pandas as pd

def create_tup_frame(a, b):
	return tuple(zip(*zip(a, b)))
