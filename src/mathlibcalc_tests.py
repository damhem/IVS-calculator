#!usr/bin/python3
# -*- coding: utf-8 -*-

# mathlibcalc_tests.py
# Project IVS 2
# Author: Patrik Sehnoutek, xsehno01
# Date: 2021-03-19

import unittest
from mathlibcalc import Calclib

##
#   @file mathlibcalc_tests.py
#
#   @brief Contains tests for the mathlibcalc.py
#   @author Patrik Sehnoutek, xsehno01
#


##
# @brief Class MathLibCalcAddTests contains tests for method Plus in mathlicalc.py
#
class MathLibCalcAddTests(unittest.TestCase):
    def setUp(self):
        self.calclib = Calclib()

    def test_add_positive_numbers(self):
        self.assertEqual(self.calclib.plus(3, 2), 5)
        self.assertEqual(self.calclib.plus(11, 158), 169)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calclib.plus(-1, -4), -5)
        self.assertEqual(self.calclib.plus(-10, -7), -17)

    def test_add_positive_and_negative_number(self):
        self.assertEqual(self.calclib.plus(2, -4), -2)
        self.assertEqual(self.calclib.plus(-8, 11), 3)

    def test_add_zero(self):
        self.assertEqual(self.calclib.plus(-1, 0), -1)
        self.assertEqual(self.calclib.plus(0, 0), 0)

    def test_add_decimal_numbers(self):
        self.assertEqual(self.calclib.plus(-1.2, 4.5), 3.3)
        self.assertEqual(self.calclib.plus(0.3, 0.87), 1.17)


##
# @brief Class MathLibCalcSubTests contains tests for method Minus in mathlicalc.py
#
class MathLibCalcSubTests(unittest.TestCase):
    def setUp(self):
        self.calclib = Calclib()

    def test_sub_positive_numbers(self):
        self.assertEqual(self.calclib.minus(3, 2), 1)
        self.assertEqual(self.calclib.minus(11, 158), -147)

    def test_sub_negative_numbers(self):
        self.assertEqual(self.calclib.minus(-1, -4), 3)
        self.assertEqual(self.calclib.minus(-10, -7), -3)

    def test_sub_positive_and_negative_number(self):
        self.assertEqual(self.calclib.minus(2, -4), 6)
        self.assertEqual(self.calclib.minus(-8, 11), -19)

    def test_sub_zero(self):
        self.assertEqual(self.calclib.minus(-1, 0), -1)
        self.assertEqual(self.calclib.minus(0, 0), 0)

    def test_sub_decimal_numbers(self):
        self.assertEqual(self.calclib.minus(-1.2, 4.5), -5.7)
        self.assertAlmostEqual(self.calclib.minus(0.90, 0.80), 0.10, 4)


##
# @brief Class MathLibCalcMulTests contains tests for method Multiply in mathlicalc.py
#
class MathLibCalcMulTests(unittest.TestCase):
    def setUp(self):
        self.calclib = Calclib()

    def test_mul_positive_numbers(self):
        self.assertEqual(self.calclib.multiply(3, 4), 12)
        self.assertEqual(self.calclib.multiply(4, 5), 20)
   
    def test_mul_negative_numbers(self):
        self.assertEqual(self.calclib.multiply(-3, -5), 15)
        self.assertEqual(self.calclib.multiply(-7, -8), 56)
    
    def test_mul_positive_and_negative_number(self):
        self.assertEqual(self.calclib.multiply(-1, 5), -5)
        self.assertEqual(self.calclib.multiply(78, -2), -156)

    def test_mul_by_zero(self):
        self.assertEqual(self.calclib.multiply(-1, 0), 0)
        self.assertEqual(self.calclib.multiply(0, 5), 0)

    def test_mul_decimal_numbers(self):
        self.assertEqual(self.calclib.multiply(2.0, 0.5), 1)
        self.assertEqual(self.calclib.multiply(5.5, 3.2), 17.6)


##
# @brief Class MathLibCalcDivTests contains tests for method Divide in mathlicalc.py
#
class MathLibCalcDivTests(unittest.TestCase):
    def setUp(self):
        self.calclib = Calclib()

    def test_div_positive_numbers(self):
        self.assertEqual(self.calclib.divide(12, 5), 2.4)
        self.assertEqual(self.calclib.divide(25, 8), 3.125)

    def test_div_negative_numbers(self):
        self.assertEqual(self.calclib.divide(-100, -25), 4)
        self.assertEqual(self.calclib.divide(-15, -5), 3)
    
    def test_div_positive_and_negative_number(self):
        self.assertEqual(self.calclib.divide(10, -2), -5)
        self.assertEqual(self.calclib.divide(-30, 6), -5)
    
    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calclib.divide(10, 0)
    
    def test_div_decimal_numbers(self):
        self.assertAlmostEqual(self.calclib.divide(0.2, 0.5), 0.4, 4)
        self.assertAlmostEqual(self.calclib.divide(0.7, -0.4), -1.75, 4)


##
# @brief Class MathLibCalcAbs contains tests for method Operation_abs in mathlicalc.py
#
class MathLibCalcAbs(unittest.TestCase):
    def setUp(self):
        self.calclib = Calclib()

    def test_abs_from_positive_numbers(self):
        self.assertEqual(self.calclib.operation_abs(10), 10)
        self.assertEqual(self.calclib.operation_abs(20), 20)
    
    def test_abs_from_negative_numbers(self):
        self.assertEqual(self.calclib.operation_abs(-10), 10)
        self.assertEqual(self.calclib.operation_abs(-20), 20)
    
    def test_abs_from_zero(self):
        self.assertEqual(self.calclib.operation_abs(0), 0)


##
# @brief Class MathLibCalcFactorial contains tests for method Factorial in mathlicalc.py
#
class MathLibCalcFactorial(unittest.TestCase):
    def setUp(self):
        self.calclib = Calclib()
    
    def test_fac_zero(self):
        self.assertEqual(self.calclib.factorial(0), 1)

    def test_fac_results(self):
        self.assertEqual(self.calclib.factorial(1), 1)
        self.assertEqual(self.calclib.factorial(5), 120)
        self.assertEqual(self.calclib.factorial(2), 2)

    def test_fac_forbidden_numbers(self):
        with self.assertRaises(ValueError):
            self.calclib.factorial(-1)
        with self.assertRaises(ValueError):
            self.calclib.factorial(-20)
        with self.assertRaises(ValueError):
            self.calclib.factorial(1.1)
        with self.assertRaises(ValueError):
            self.calclib.factorial(-0.5)


##
# @brief Class MathLibCalcExponentTests contains tests for method Exponent in mathlicalc.py
#
class MathLibCalcExponentTests(unittest.TestCase):
    def setUp(self):
        self.calclib = Calclib()

    def test_exponent_positive_numbers(self):
        self.assertEqual(self.calclib.exponent(2, 2), 4)
        self.assertEqual(self.calclib.exponent(3, 1), 3)
        self.assertEqual(self.calclib.exponent(3, 0), 1)

    def test_exponent_negative_numbers(self):
        self.assertEqual(self.calclib.exponent(-2, -2), 0.25)
        self.assertEqual(self.calclib.exponent(-3, 0), 1)
    
    def test_exponent_positive_and_negative_numbers(self):
        self.assertEqual(self.calclib.exponent(2, -3), 0.125)
        self.assertEqual(self.calclib.exponent(-2, 2), 4)
        self.assertEqual(self.calclib.exponent(-2, 3), -8)

    def test_exponent_decimal_numbers(self):
        self.assertEqual(self.calclib.exponent(0.04, 0.5), 0.2)
    
    def test_exponent_forbidden_numbers(self):
        with self.assertRaises(ValueError):
            self.calclib.exponent(0,0)


##
# @brief Class MathLibCalcRootTests contains tests for method Root in mathlicalc.py
#
class MathLibCalcRootTests(unittest.TestCase):
    def setUp(self):
        self.calclib = Calclib()  

    def test_root_even(self):
        self.assertEqual(self.calclib.root(0, 2), 0)
        self.assertEqual(self.calclib.root(4, 2), 2)
        self.assertEqual(self.calclib.root(625, 4), 5)
    
    def test_root_odd(self):
        self.assertEqual(self.calclib.root(0, 3), 0)
        self.assertEqual(self.calclib.root(10, 1), 10)
        self.assertEqual(self.calclib.root(8, 3), 2)
        self.assertEqual(self.calclib.root(32, 5), 2)
        self.assertEqual(self.calclib.root(-32, 5), -2)

    def test_root_forbbiden_numbers(self):
        with self.assertRaises(ValueError):
            self.calclib.root(2, 0)     
        with self.assertRaises(ValueError):
            self.calclib.root(-3, 2)     
        with self.assertRaises(ValueError):
            self.calclib.root(-5, 4)     
    
    
if __name__ == '__main__':
    unittest.main()
