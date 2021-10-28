# Python Fraction
Python has a data type called fractions. Unlike int and float, fractions are not a built in data type. To use fractions, need to import python module called *fractions*.

## Importing fractions module
*Fractions* module is already involved in python standard library. You don't need to install it separately. Imopot it using *import* keyword.
```
from fractions import Fraction
```
Import *Fraction* method from *fractions* class.

## Fraction without argumnts
Fraction can be used without passing any argument. It will return "0".
```
from fractions import Fraction
print(Fraction())
```
 ouput is *0*.

## Fraction with decimal arguments
By passing decimal number into *Fraction*, it will return the fraction of given decimal number.
```
from fractions import Fraction
print(Fraction(0.25))
```
output is *1/4*.

## Fraction with two arguments
By passing two numbers into *Fraction*, it will return the fraction of given two numbers. The first number will be numerator and the second number will be denominator.
```
from fractions import Fraction
print(Fraction(1, 2))
```
output is *1/2*.

## Greatet Common Divisor

Both magnitude get simplified by their Greatest Common Divisor(GCD). GCD of 14 is 2 and GCD of 49 is 7.
```
from fractions import Fraction
print(Fraction(14, 49))
```
output is *2/2*.

## Negative fractions 

You can put minus sign(-) at in front of constructor or in front of numerator or in front of denominator to get a negative fraction.
```
from fractions import Fraction
print(-Fraction(1, 2))
print(Fraction(-1, 2))
print(Fraction(1, -2)).
```
output of all code is *-1/2*.

## Adding, differening, multiplying and divising fractions 
You can add, difference, multiply, divide fractions with simple arithmetic operator.
```
from fractions import Fraction
one_half = Fraction(1, 2)
one_third = Fraction(1, 3)
print(one_half + one_third)
print(one_half - one_third)
print(one_half * one_third)
print(one_half / one_third)
```
output is *5/6, 1/6, 1/6, 3/2*.

## fractions with zero numerator
By putting 0 at the place numerator, the result will be zero since the division of zero by any number is zero.
```
from fractions import Fraction
print(Fraction(0, 5))
```
output is *o*.

## fractions with zero denominator
By placing 0 at the place of denominator, the result will be *ZeroDivisionError* since zero cannot divide any number.
```
from fractions import Fraction
try:
    print(Fraction(1, 0))
except ZeroDivisionError:
    print("ZeroDivisionError")
```
output is *ZeroDivisionError*.

You can get the code of this example at *fraction_tutorial.py*.

Contact me on [Facebook](https://www.facebook.com/zinyaw3063)

Contact me on [GitHub](https://www.github.com/aungnyeinchan351)

Contace me on [Email](aungnyeinchan3063@protonmail.com)
