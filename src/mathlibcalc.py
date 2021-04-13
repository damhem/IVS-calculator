# mathlibcalc.py
# Project IVS 2
# Author: Dalibor Králik, xkrali20
# Date: 2021-03-22





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
        return round(num1-num2, 8)

    ##
    # @brief Function for multiplying two numbers
    #
    # @param num1 First number
    # @param num2 Second number
    #
    # @return Multiple of two numbers
    @staticmethod
    def multiply(num1, num2):
        return round(num1*num2, 8)


    ##
    # @brief Function for dividing two numbers
    #
    # @param num1 First number
    # @param num2 Second number
    #
    # @exception ZeroDivisionError If num2 is equal to 0
    # @return Return division of two numbers
    @staticmethod
    def divide(num1, num2):
        if num2 == 0:
            raise ZeroDivisionError("Math Error - Dividing by zero")
        else:
            return round(num1/num2, 8)


    ##
    # @brief Function for absolute value
    #
    # @param num1  Number
    #
    # @return Absolute value of num1
    @staticmethod
    def operation_abs(num1):
        return round(abs(num1), 8)


    ##
    # @brief Function for factorial
    #
    # @param num1 Number
    #
    # @exception ValueError If num1 is less than 0 or if num1 is not integer
    # @return Factorial of num1
    @staticmethod
    def factorial(num1):
        result = 1
        if num1 < 0 or num1 % 1 != 0:
            raise ValueError("Math Error")
        else:
            num1 = int(num1)
            for i in range(1, num1+1):
                result*=i
            return result


    ##
    # @brief Function for exponentiation of a number
    #
    # @param num1 Number
    # @param expo Exponent
    #
    # @exception ValueError If num1 is equal to 0 and expo is equal to 0
    # @return Exponentiation the number of the exponent
    @staticmethod
    def exponent(num1, expo):
        if num1 == 0 and expo == 0:
            raise ValueError("Math Error")
        return round(num1 ** expo, 8)


    ##
    # @brief Root function
    #
    # @param num1 Number
    # @param expo Root number
    #
    # @exception ValueError If num1 is less then 0 and root number is even, or if root number is equal to 0
    # @return Root of num1
    @staticmethod
    def root(num1, expo):
        if (num1 < 0 and expo % 2 == 0) or expo == 0:
            raise ValueError("Math Error")
        elif num1 == 0:
            return 0
        elif num1 < 0 and expo % 2 == 1:
            return -1*round(((-1*num1) ** (1/expo)), 8)
        else:
            return round((num1 ** (1/expo)), 8)

