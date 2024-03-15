import numpy as np
from pandas import pd
import torch


def tenzor_compose(a, lengths):
	batch_size, sentence_length, embedding_dim = len(a), len(lengths), len(a[0])
	t = a.reshape(batch_size, sentence_length, embedding_dim)
	t.fill_(0)
	return t
