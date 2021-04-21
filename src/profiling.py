#!usr/bin/python3
# -*- coding: utf-8 -*-

# profiling.py
# Project IVS 2
# Author: Patrik Sehnoutek, xsehno01
# Date: 2021-04-03

import random
from mathlibcalc import Calclib


##
#   @file profiling.py
#
#   @brief Contains algorithm for calculating the math expression with help of the mathlibcalc.py
#   @author Patrik Sehnoutek, xsehno01
#



##
# @brief Function for reading input from stdin
#
# @return Array of numbers from stdin
def read_from_stdin():
    input_numbers = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        input_numbers += line.split()
    return input_numbers


##
# @brief Function for generating random numbers
#
# @param n Number of generated numbers
#
# @return Array of generated numbers
def generate_random_numbers(n):
    str_numbers = ""
    for i in range(n):
        str_numbers += str(random.randrange(-1000000, 1000000))
        if (i < n-1):
            str_numbers += " "
    return str_numbers.split()


##
# @brief Function for calculating standard deviation
#
# @param numbers_arr Array of given numbers
#
# @return Result of standard deviation
def standard_deviation(numbers_arr):
    length = len(numbers_arr)

    if (length == 0):
        return "ERROR: Empty input."
    if (length == 1):
        return "ERROR: Cannot calculate standard deviation from one number."

    result = 0
    right_side = 0
    left_side = 0

    for i in range(length):
        tmp = Calclib.exponent(float(numbers_arr[i]), 2)
        left_side = Calclib.plus(left_side, tmp)
        right_side = Calclib.plus(right_side, float(numbers_arr[i]))

    right_side = Calclib.divide(right_side, length)
    right_side = Calclib.exponent(right_side, 2)
    right_side = Calclib.multiply(right_side, length)

    result = Calclib.minus(left_side, right_side)
    result = Calclib.divide(result, length-1)

    return Calclib.root(result, 2)


if __name__ == '__main__':
    input_numbers = read_from_stdin()
    print(standard_deviation(input_numbers))
    # numbers = generate_random_numbers(1000)
    # print(standard_deviation(numbers))
