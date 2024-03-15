import numpy as np
def reduce_fractions(numerator, denominator):
	if numerator == 0 and denominator == 0:
		return (float("NaN"), float("NaN"))
	num, den = np.fractionalmod(numerator, denominator), np.fractionalmod(denominator, numerator)
	if abs(num) == abs(den):
		return (float("NaN"), float("NaN"))
	else:
		return (num, den)
