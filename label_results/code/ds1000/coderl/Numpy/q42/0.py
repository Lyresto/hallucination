from fractions import Fraction
def reduce_fractions(numerator,denominator):
	f = Fraction(numerator,denominator)
	if f.numerator == 0 or f.denominator == 0:
		return (float("NaN"),float("NaN"))
	elif f.numerator % f.denominator == 0:
		ans = (f.numerator,f.denominator)
	else:
		ans = (f.numerator//f.denominator,f.denominator//f.numerator)
	return ans
