#Importing fractions module
from fractions import Fraction

#using Fraction class with zero constructor
print(Fraction())

#using Fraction with decimal numbers
print(Fraction(0.25))

#using Fraction with two constructor
print(Fraction(1, 2))

#Greatest Common Divisor(GCD)
print(Fraction(14, 49))

#negative fractions
print(-Fraction(1, 2))
print(Fraction(-1, 2))
print(Fraction(1, -2))

#fraction in a fraction
one_half = Fraction(1, 2)
print(Fraction(one_half, 6))

#adding fractions
one_third = Fraction(1, 3)
print(one_half + one_third)

#difference between fractions
print(one_half - one_third)

#mutplying fractions
print(one_half * one_third)

#dividing fractions
print(one_half / one_third)

#fractions with zero numerator
print(Fraction(0, 5))

#fractions with zero denominator
try:
    print(Fraction(1, 0))
except ZeroDivisionError:
    print("ZeroDivisionError")