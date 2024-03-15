# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

def load_data():
	return pd.read_csv('example.csv', header=None, sep=',')
