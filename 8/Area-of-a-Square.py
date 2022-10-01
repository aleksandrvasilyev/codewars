# https://www.codewars.com/kata/5748838ce2fab90b86001b1a/train/python

import math


def square_area(A):
    p = A * 4
    r = p / (2 * math.pi)
    res = r ** 2
    return round(res, 2)


print(square_area(2))
