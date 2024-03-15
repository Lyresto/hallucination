import math

def reduce_fractions(numerator, denominator):
	num, den = str(numerator), str(denominator)
	if num[-1] == '0': num = num[:-1]
	if den[-1] == '0': den = den[:-1]
	num = math.floor(num)
	den = math.floor(den)
	s = ''
	if num!= 0:
		s = num
	else:
		s = 'NaN'
	if den!= 0:
		s = den
	else:
		s = 'NaN'
	return (s, s)
