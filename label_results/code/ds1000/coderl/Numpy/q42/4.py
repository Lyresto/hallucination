from numpy import gcd, ceil
def reduce_fractions(numerator, denominator):
	f = gcd(numerator,denominator)
	return (round(numerator/f), round(denominator/f))
