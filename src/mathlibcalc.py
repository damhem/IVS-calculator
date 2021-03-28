# mathlibcalc.py
# Project IVS 2
# Author: Dalibor Králik, xkrali20
# Date: 2021-03-22

##
# @package merioneslib
# Merioneslib is a mathematical library for Meriones calculator.
#
# This mathematical library consists of basic mathematical operations
# such as sum, difference, multiplication or division, advanced mathematical
# operations such as power, root, natural logarithm. This library also
# includes some conversion functions such as convert_weight, convert_time
# convert_degrees, convert_lenght
#



##
# @brief Class Calclib for the Calculator, contains math functions
#
class Calclib:

    ##
    # @brief Function for the sum of two numbers
    #
    # @param num1 First number
    # @param num2 Second number
    #
    # @return Return sum of two numbers
    @staticmethod
    def plus(num1, num2):
        return num1 + num2

    ##
    # @brief Function for the difference of two numbers
    #
    # @param num1 First number
    # @param num2 Second number
    #
    # @return Difference of two numbers
    @staticmethod
    def minus(num1, num2):
        return num1 - num2

    ##
    # @brief Function for multiplying two numbers
    #
    # @param num1 First number
    # @param num2 Second number
    #
    # @return Multiple of two numbers
    @staticmethod
    def multiply(num1, num2):
        return num1*num2


    ##
    # @brief Function for dividing two numbers
    #
    # @param num1 First number
    # @param num2 Second number
    #
    # @throw ZeroDivisionError If num2 is equal to 0
    # @return Return division of two numbers
    @staticmethod
    def divide(num1, num2):
        if num2 == 0:
            raise ZeroDivisionError("Math Error - Dividing by zero")
        else:
            return num1/num2


    ##
    # @brief Function for absolute value
    #
    # @param num1  Number
    #
    # @return Absolute value of num1
    @staticmethod
    def operation_abs(num1):
        return abs(num1)


    ##
    # @brief Function for factorial
    #
    # @param num1 Number
    #
    # @throw ValueError If num1 is less than 0 or if num1 is not integer
    # @return Factorial of num1
    @staticmethod
    def factorial(num1):
        result = 1
        if num1 < 0 or num1 % 1 != 0:
            raise ValueError("Math Error")
            # treba sa dohodnut ako budeme brat zaporne cisla a kedy
        else:
            for i in range(1,num1+1):
                result*=i
            return result


    ##
    # @brief Function for exponentiation of a number
    #
    # @param num1 Number
    # @param expo Exponent
    #
    # @return Exponentiate the number of the exponent
    @staticmethod
    def exponent(num1, expo):
        if num1 == 0 and expo == 0:
            raise ValueError("Math Error")
        return num1 ** expo


    ##
    # @brief Root function
    #
    # @param num1 Number
    # @param expo Root number
    #
    # @throw ValueError If num1 is less then 0 and root number is even, or if root number is equal to 0
    # @return Root of num1
    @staticmethod
    def root(num1, expo):
        if (num1 < 0 and expo % 2 == 0) or expo == 0:
            raise ValueError("Math Error - Dividing by zero")
        elif num1 == 0:
            return 0
        elif num1 < 0 and expo % 2 == 1:
            return -1*round(((-1*num1) ** (1/expo)), 5)
        else:
            return round((num1 ** (1/expo)), 5)

