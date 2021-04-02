#!usr/bin/env python3
# -*- coding: utf-8 -*-

# profiling.py
# Project IVS 2
# Author: Patrik Sehnoutek, xsehno01
# Date: 2021-04-01

import random
from mathlibcalc import Calclib

def generate_random_numbers(n):
    str_numbers = ""
    for i in range(n):
        str_numbers += str(random.randrange(-1000000, 1000000))
        if (i < n-1):
            str_numbers += " "
    return str_numbers.split()


def standard_deviation(numbers_arr):
    length = len(numbers_arr)

    result = 0
    right_side = 0
    left_side = 0

    for i in range(length):
        tmp = Calclib.exponent(int(numbers_arr[i]), 2)
        left_side = Calclib.plus(left_side, tmp)
        right_side = Calclib.plus(right_side, int(numbers_arr[i]))

    right_side = Calclib.divide(right_side, length)
    right_side = Calclib.exponent(right_side, 2)
    right_side = Calclib.multiply(right_side, length)

    result = Calclib.minus(left_side, right_side)
    result = Calclib.divide(result, length-1)

    return Calclib.root(result, 2)


if __name__ == '__main__':
    #str_input = ""
    #str_input = input()
    #str_input = input().split()
    #print(str_input)
    numbers = generate_random_numbers(500000)
    print(standard_deviation(numbers))
