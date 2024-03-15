from numpy import mean, std
from scipy.sparse import csr_matrix

sA = csr_matrix(arr)
mean, standard_deviation = mean(sA.data), std((sA.data ** 2).sum(1))
