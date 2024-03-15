from fractions import Fraction

numerator = 98
denominator = 42

result = Fraction(numerator, denominator).limit_denominator()

result_tuple = (result.numerator, result.denominator)

print(result_tuple)