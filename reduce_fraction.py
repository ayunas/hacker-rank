#https://www.hackerrank.com/challenges/reduce-function/problem
#take an array of pairs, reduce to a product for numerator and denominator

from fractions import Fraction
from functools import reduce
from random import randint

print(Fraction(2,5).numerator)


def reduce_fraction(count,fracs):
    print(fracs)
    numerators = [f.numerator for f in fracs]
    denominators = [f.denominator for f in fracs]
    numerator = reduce(lambda s,n: s*n, numerators)
    denominator = reduce(lambda s,n: s*n, denominators)
    low_frac = Fraction(numerator,denominator)
    print(f"{numerator}/{denominator}")
    return low_frac.numerator, low_frac.denominator

    

count = 3
# fractions = [(1,3),(2,6),(3,9)]
fractions = []
for _ in range(10):
    fractions.append(Fraction(randint(1,10),randint(9,20)))

x = reduce_fraction(count,fractions)
print(x)

    