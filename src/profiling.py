#!usr/bin/env python3

# profiling.py
# Project IVS 2
# Author: Patrik Sehnoutek, xsehno01
# Date: 2021-04-01

import random
from mathlibcalc import Calclib

str_input = ""
str_input = input("Enter numbers separated with space: ").split()
print(str_input)


def arithmetic_average(numbers_arr, n):
    sum = 0
    for i in range(n):
        sum = Calclib.plus(sum, int(numbers_arr[i]))

    return Calclib.divide(sum, n)


def generate_random_numbers(n):
    str_numbers = ""
    for i in range(n):
        str_numbers += str(random.randrange(-1000, 1000))
        if (i < n-1):
            str_numbers += " "
    return str_numbers.split()


def standard_deviation(numbers_arr):
    length = len(numbers_arr)
    print(length)

    average = arithmetic_average(numbers_arr, length)
    print(average)

    result = 0

    right_side = Calclib.exponent(average, 2)
    right_side = Calclib.multiply(right_side, length)

    for i in range(length):
        left_side = Calclib.exponent(int(numbers_arr[i]) , 2)
        tmp = Calclib.minus(left_side, right_side)
        result = Calclib.plus(result, tmp)

    result = Calclib.divide(result, length-1)
    return Calclib.root(result, 2)

# Random numbers in range 10, 100 and 1000 to profiling
numbers = generate_random_numbers(10)
print(numbers)
print(standard_deviation(numbers))

#numbers = generate_random_numbers(100)
#print(arithmetic_average(numbers, 100))

#numbers = generate_random_numbers(1000)
#print(arithmetic_average(numbers, 1000))

"""if __name__ == 'main':
    str_input = ""
    str_input = input()
    str_input = input().split()
    print(str_input)"""
