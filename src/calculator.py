## File: calculator.py
# Project IVS 2
# Author: Daniel Čechák, xcecha06
# Date: 2021-03-22
# File includes methods for button pushes and processing calculations
from PyQt5 import QtWidgets, QtCore
from gui import Calculator_ui
from PyQt5 import QtGui
from mathlibcalc import Calclib
import math
from PyQt5.QtGui import *
import os

##
# @brief Class Calculator contains initialization and button methods
#
class Calculator(QtWidgets.QMainWindow, Calculator_ui):
    last_button = ""
    operatorbool = False

    ## Method __init__
    # @brief Function for initialization
    #
    # @param self The object pointer.
    def __init__(self):
        # initialization
        super().__init__()

        self.setWindowIcon(QtGui.QIcon("cal.png"))
        self.setupUi(self)
        self.show()

        # Reacting on button pushes
        # Buttons for numbers
        self.pushButton_15.clicked.connect(self.buttonNumber_pressed)
        self.pushButton_15.setShortcut("1")
        self.pushButton_12.clicked.connect(self.buttonNumber_pressed)
        self.pushButton_12.setShortcut("2")
        self.pushButton_11.clicked.connect(self.buttonNumber_pressed)
        self.pushButton_11.setShortcut("3")
        self.pushButton_20.clicked.connect(self.buttonNumber_pressed)
        self.pushButton_20.setShortcut("4")
        self.pushButton_16.clicked.connect(self.buttonNumber_pressed)
        self.pushButton_16.setShortcut("5")
        self.pushButton_19.clicked.connect(self.buttonNumber_pressed)
        self.pushButton_19.setShortcut("6")
        self.pushButton_9.clicked.connect(self.buttonNumber_pressed)
        self.pushButton_9.setShortcut("7")
        self.pushButton_6.clicked.connect(self.buttonNumber_pressed)
        self.pushButton_6.setShortcut("8")
        self.pushButton_8.clicked.connect(self.buttonNumber_pressed)
        self.pushButton_8.setShortcut("9")
        self.pushButton_22.clicked.connect(self.buttonNumber_pressed)
        self.pushButton_22.setShortcut("0")

        # Button DEL for deleting 1 char
        self.pushButton_4.clicked.connect(self.buttonDelete1_pressed)
        self.pushButton_4.setShortcut("Backspace")

        # Button DE for deleting line
        self.pushButton_5.clicked.connect(self.buttonDelete_pressed)
        self.pushButton_5.setShortcut("delete")

        # Buttons for simple operators
        self.pushButton_21.clicked.connect(self.buttonSimple_pressed)
        self.pushButton_21.setShortcut("/")
        self.pushButton_18.clicked.connect(self.buttonSimple_pressed)
        self.pushButton_18.setShortcut("*")
        self.pushButton_13.clicked.connect(self.buttonSimple_pressed)
        self.pushButton_13.setShortcut("-")
        self.pushButton_10.clicked.connect(self.buttonSimple_pressed)
        self.pushButton_10.setShortcut("+")

        # Button for float
        self.pushButton_25.clicked.connect(self.buttonFloat_pressed)
        self.pushButton_25.setShortcut(",")

        # Button = for solving
        self.pushButton_14.clicked.connect(self.buttonSolve_pressed)
        self.pushButton_14.setShortcut("enter")

        # Buttons for constants
        self.pushButton_2.clicked.connect(self.buttonE_pressed)
        self.pushButton_2.setShortcut("e")
        self.pushButton_3.clicked.connect(self.buttonPi_pressed)
        self.pushButton_3.setShortcut("p")

        # Button for factorial
        self.pushButton.clicked.connect(self.buttonFactorial_pressed)
        self.pushButton.setShortcut("!")

        # Button for absolute value
        self.pushButton_24.clicked.connect(self.buttonAbsolute_pressed)
        self.pushButton_24.setShortcut("|")

        # Button for square root
        self.pushButton_17.clicked.connect(self.buttonSquareroot_pressed)
        # Button for power
        self.pushButton_7.clicked.connect(self.buttonPower_pressed)

        # Reaction on lineedit/input
        # self.lineEdit.textChanged.connect(self.textChanged)

    ## Method keyPressEvent
    # @brief Function reaction on ESC key being clicked
    # closes the window after ESC key is pressed
    # @param self The object pointer.
    # @param event event whats happening in the moment
    def keyPressEvent(self, event):
        # Did the user press the Escape key?
        if event.key() == QtCore.Qt.Key_Escape:  # QtCore.Qt.Key_Escape is a value for escape key being pressed.
            self.close()  # Close the window

    #################### start #############################################################################
    ## Method convertIndex
    # @brief Function convert index to the integer
    #
    # @param num1 as a string
    def convertIndex(self, num1):
        expression = ''
        array = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
        for i in num1:
            expression = expression + str(array.index(i))
        return int(expression)



    ## Method expSolving
    # @brief Function solve expression
    #
    # @param self The object pointer.
    def expSolving(self):
        expression = self.lineEdit.text()
        self.lineEdit_2.setText(expression)
        exponentbool = False
        array = {'+', '√', '-', '*', '/', '!'}
        for i in array:
            # if first number is negative, we don't want to deal with it as a operator but as a negative number
            # if first character in string is '√', we want exponent set to ² after press = or next operator
            if (expression.rfind(i) > 0 and i != '√') or (expression.rfind(i) >= 0 and i == '√'):
                exponentbool = True
                # if last character is operator, add 0 to the end of expression
                if expression[-1] == i:
                    expression = expression + '0'

                # if ³√-6, than don't deal with operator '-'
                if i == '-' and expression[expression.find(i) - 1] == '√':
                    continue
                # if negative number occurs as a first number
                if expression[0] == '-':
                    expression = expression[1:]
                    numbers = expression.split(i)
                    numbers[0] = '-' + numbers[0]
                elif expression[0] == '√':  # index processing
                    expression = expression[1:]
                    numbers = ['', '']
                    numbers[0] = '²'
                    numbers[1] = expression
                else:
                    numbers = expression.split(i)

                num1 = numbers[0]
                num2 = numbers[1]

                # cases when e, PI or float number is in expression
                if num1 == 'e' or num1 == 'ͤ':
                    num1 = math.e
                elif num1 == 'π' or num1 == ' ⷫ':
                    num1 = math.pi
                elif num1.find('.') != -1:
                    num1 = float(num1)
                elif i == '√': # index processing
                    num1 = self.convertIndex(num1)
                else:
                    num1 = int(num1)

                if num2 == 'e':
                    num2 = math.e
                elif num2 == 'π':
                    num2 = math.pi
                elif num2.find('.') != -1:
                    num2 = float(num2)
                else:
                    num2 = int(num2)

                # sending to the mathlibcalc functions
                if i == '+':
                    expression = str(Calclib.plus(num1,num2))
                elif i == '-' and expression[expression.find(i) - 1] != '√':
                    expression = str(Calclib.minus(num1, num2))
                elif i == '*':
                    expression = str(Calclib.multiply(num1, num2))
                elif i == '/':
                    try:
                        expression = str(Calclib.divide(num1, num2))
                    except ZeroDivisionError:
                        # Throw error message when num2 = 0 -> dividing by zero
                        self.lineEdit_2.setText("Math Error - Dividing by zero")
                        self.lineEdit.setText("0")
                        return
                elif i == '!':
                    try:
                        expression = str(Calclib.factorial(num1))
                    except ValueError:
                        # Throw error message when negative or float number occurs
                        self.lineEdit_2.setText("Math Error")
                        self.lineEdit.setText("0")
                        return
                elif i == '√':
                    try:
                        expression = str(Calclib.root(num2, num1))
                    except ValueError:
                        # Throw error message when exponent = 0
                        self.lineEdit_2.setText("Math Error - Exponent = 0")
                        self.lineEdit.setText("0")
                        return

        # Solving exponent (power) function
        array1 = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹', 'ⷫ', 'ͤ']
        if not exponentbool and expression[-1] in array1:
            for i in expression:
                if i in array1:
                    numbers = expression.split(i)
                    num1 = numbers[0]
                    num2 = i+numbers[1]

                    if num1 == 'e':
                        num1 = math.e
                    elif num1 == 'π':
                        num1 = math.pi
                    elif num1.find('.') != -1:
                        num1 = float(num1)
                    else:
                        num1 = int(num1)

                    if num2 == 'ͤ':
                        num2 = math.e
                    elif num2 == 'ⷫ':
                        num2 = math.pi
                    else:
                        num2 = self.convertIndex(num2)

                    expression = str(Calclib.exponent(num1, num2))
                    break

        self.lineEdit.setText(expression)
        self.operatorbool = False

    ###################### end ###########################################################################

    ## Method buttonSolve_pressed
    # @brief Function reaction on Solve button being clicked
    #
    # @param self The object pointer.
    def buttonSolve_pressed(self):
        expression = self.lineEdit.text()  # getting value from lineEdit(calculator input) in the moment
        ############ start #####################################################################################
        self.lineEdit_2.setText(expression)
        self.expSolving()
        self.operatorbool = False
        ############ end #####################################################################################
        self.lineEdit.setFocus(False)
        Calculator.last_button = "="

    ## Method number
    # @brief Function converting numbers to upper indexes
    #
    # @param self The object pointer.
    # @param i Number being converted.
    def number(self, i):
        switcher = {
            0: '⁰',
            1: '¹',
            2: '²',
            3: '³',
            4: '⁴',
            5: '⁵',
            6: '⁶',
            7: '⁷',
            8: '⁸',
            9: '⁹'
        }
        return switcher.get(i, "")

    ## Method buttonNumber_pressed
    # @brief Function reaction on any number button being clicked
    #
    # @param self The object pointer.
    def buttonNumber_pressed(self):
        button = self.sender()  # getting value from button clicked in the moment
        button = button.text()
        array = {'⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹'}
        expression = self.lineEdit.text()  # getting value from lineEdit(calculator input) in the moment
        if expression[-1] == "ͤ" or expression[-1] == "ⷫ":
            expression = expression
        # reacting if last button is Square root
        elif str(Calculator.last_button) == "√":
            # transforming number to upper index
            button = self.number(int(button))
            help = self.lineEdit.text()
            # editing lineEdit result
            position = help.index("√")
            expression = help[:position] + button + help[position:]
            # printing result into lineEdit
            self.lineEdit.setText(expression)
            self.lineEdit.setFocus(False)
            Calculator.last_button = str(Calculator.last_button)

        # reacting if last button is power
        elif str(Calculator.last_button) in array or str(Calculator.last_button) == "ⁿ":
            # transforming number to upper index
            button = self.number(int(button))
            # editing lineEdit result
            expression = self.lineEdit.text() + button
            # printing result into lineEdit
            self.lineEdit.setText(expression)
            self.lineEdit.setFocus(False)
            Calculator.last_button = button
        elif expression[-1] == "ͤ" or expression[-1] == " ⷫ":
            expression = expression
        elif expression[-1] == "e" or expression[-1] == "π":
            expression = expression
        else:
            if expression == "0":
                expression = button
            else:
                expression = self.lineEdit.text() + button

            # printing result into lineEdit
            self.lineEdit.setText(expression)
            self.lineEdit.setFocus(False)
            Calculator.last_button = button

    ## Method buttonDelete_pressed
    # @brief Function reaction on CE button being clicked
    # Deletes whole line
    # @param self The object pointer.
    def buttonDelete_pressed(self):
        expression = "0"
        if Calculator.last_button == "CE":
            # printing result into lineEdit
            self.lineEdit.setText(expression)
            self.lineEdit_2.setText("")
            self.lineEdit.setFocus(False)
        else:
            # printing result into lineEdit
            self.lineEdit.setText(expression)
            self.lineEdit.setFocus(False)
        ############ start #####################################################################################
        self.operatorbool = False
        ############ end #####################################################################################
        Calculator.last_button = self.sender().text()

    ## Method buttonDelete1_pressed
    # @brief Function reaction on DEL button being clicked
    # Deletes 1 char
    # @param self The object pointer.
    def buttonDelete1_pressed(self):
        expression = self.lineEdit.text()  # getting value from lineEdit(calculator input) in the moment
        if expression[:-1] == "":
            expression = "0"
        elif expression == "":
            expression = "0"
        else:
            ############ start #####################################################################################
            if expression[-1] == "+" or expression[-1] == "-" or expression[-1] == "*" or expression[-1] == "/" \
                    or expression[-1] == "!":
                self.operatorbool = False
            ############ end #####################################################################################
            expression = expression[:-1]
        # printing result into lineEdit
        self.lineEdit.setText(expression)
        self.lineEdit.setFocus(False)
        Calculator.last_button = self.sender().text()

    ## Method buttonSimple_pressed
    # @brief Function reaction on simple operations button being clicked
    #
    # @param self The object pointer.
    def buttonSimple_pressed(self):
        button = self.sender()  # getting value from button clicked in the moment
        expression = self.lineEdit.text()  # getting value from lineEdit(calculator input) in the moment
        # if last char is simple operator just change it
        if expression[-1] == "+" or expression[-1] == "-" or expression[-1] == "*" or expression[-1] == "/" \
                or expression[-1] == ".":
            expression = expression[:-1]
            expression = expression + button.text()

            ############ start #####################################################################################
            self.operatorbool = True
            ############ end #####################################################################################

        else:
            ############ start #####################################################################################
            if self.operatorbool:
                self.expSolving()
            self.operatorbool = True
            ############ end #####################################################################################

            expression = self.lineEdit.text() + button.text()

        self.lineEdit.setText(expression)
        self.lineEdit.setFocus(False)
        Calculator.last_button = self.sender().text()

    ## Method buttonFloat_pressed
    # @brief Function reaction on float button being clicked
    #
    # @param self The object pointer.
    def buttonFloat_pressed(self):
        button = self.sender()  # getting value from button clicked in the moment
        expression = self.lineEdit.text()  # getting value from lineEdit(calculator input) in the moment
        # if last char is simple operator just change it
        if expression[-1] == "+" or expression[-1] == "-" or expression[-1] == "*" or expression[-1] == "/"\
                or expression[-1] == ".":
            # check if float is correct
            helper = expression[:-1].split(".")

            if helper[-1] != "":
                if "+" in helper[-1] or "-" in helper[-1] or "*" in helper[-1] or "/" in helper[-1] or expression.isnumeric():
                    expression = expression[:-1]
                    expression = expression + button.text()
                else:
                    expression = expression
            else:
                expression = expression[:-1]
                expression = expression + button.text()
        # if last char is constant no change
        elif expression[-1] == "π" or expression[-1] == "e":
            expression = expression
        else:
            # check if float is correct
            helper = expression.split(".")

            if helper[-1] != "":
                if "+" in helper[-1] or "-" in helper[-1] or "*" in helper[-1] or "/" in helper[-1] or expression.isnumeric():
                    expression = self.lineEdit.text() + button.text()
                else:
                    expression = expression
            else:
                expression = self.lineEdit.text() + button.text()
        # printing result into lineEdit
        self.lineEdit.setText(expression)
        self.lineEdit.setFocus(False)
        Calculator.last_button = self.sender().text()

    ## Method buttonFactorial_pressed
    # @brief Function reaction on factorial button being clicked
    #
    # @param self The object pointer.
    def buttonFactorial_pressed(self):
        button = "!"
        expression = self.lineEdit.text()  # getting value from lineEdit(calculator input) in the moment
        if expression == "0":
            expression = expression + button
        elif expression[-1] == button or expression[-1] == "+" or expression[-1] == "-" or expression[-1] == "*" \
                or expression[-1] == "/" or expression[-1] == ".":
            expression = expression[:-1]
            expression = expression + button
            ############ start #####################################################################################
            self.operatorbool = True
            ############ end #####################################################################################
        else:
            ############ start #####################################################################################
            if self.operatorbool:
                self.expSolving()
            self.operatorbool = True
            ############ end #####################################################################################

            expression = self.lineEdit.text() + button

        self.lineEdit.setText(expression)
        self.lineEdit.setFocus(False)
        Calculator.last_button = self.sender().text()

    ## Method buttonE_pressed
    # @brief Function reaction on euler number button being clicked
    #
    # @param self The object pointer.
    def buttonE_pressed(self):
        button = "e"  # ᵉ
        expression = self.lineEdit.text()  # getting value from lineEdit(calculator input) in the moment
        if Calculator.last_button == "ⁿ":
            expression = expression + "ͤ"
        elif expression[-1] == "ͤ" or expression[-1] == "ⷫ":
            expression = expression
        elif Calculator.last_button == "√":
            expression = "ͤ" + expression
        elif expression == "0":
            expression = button
        elif expression[-1] == button or expression[-1] == "π" or expression[-1] == "." or expression[-1].isnumeric():

            expression = expression

        else:
            expression = self.lineEdit.text() + button
        # printing result into lineEdit
        self.lineEdit.setText(expression)
        self.lineEdit.setFocus(False)
        Calculator.last_button = self.sender()

    ## Method buttonPi_pressed
    # @brief Function reaction on Pi number button being clicked
    #
    # @param self The object pointer.
    def buttonPi_pressed(self):
        button = "π"  #    ⷫ
        expression = self.lineEdit.text()  # getting value from lineEdit(calculator input) in the moment
        if Calculator.last_button == "ⁿ":
            expression = expression + " ⷫ"
        elif expression[-1] == "ͤ" or expression[-1] == "ⷫ":
            expression = expression
        elif Calculator.last_button == "√":
            expression = " ⷫ" + expression
        elif expression == "0":
            expression = button

        elif expression[-1] == button or expression[-1] == "e" or expression[-1] == "." or expression[-1].isnumeric():

            expression = expression
        else:
            expression = self.lineEdit.text() + button
        # printing result into lineEdit
        self.lineEdit.setText(expression)
        self.lineEdit.setFocus(False)
        Calculator.last_button = self.sender()

    ## Method buttonAbsolute_pressed
    # @brief Function reaction on Absolute value button being clicked
    #
    # @param self The object pointer.
    def buttonAbsolute_pressed(self):
        button = "|"
        expression = self.lineEdit.text()  # getting value from lineEdit(calculator input) in the moment

        ############ start #####################################################################################
        negativebool = False  # bool value for know if num1 is negative or not
        if self.operatorbool == False:  # if is not any operator in expression string
            # convert expression to the float or integer depends on decimal point
            if expression.find('.') != -1:
                num1 = float(expression)
            elif expression == 'e':
                num1 = math.e
            elif expression == 'π':
                num1 = math.pi
            else:
                num1 = int(expression)

            if num1 < 0:
                negativebool = True

            expression = str(Calclib.operation_abs(num1))
        else:  # if is any operator in expression string, solve it and then do absolute value from the result
            self.expSolving()
            expression = self.lineEdit.text()
            # convert expression to the float or integer depends on decimal point
            if expression.find('.') != -1:
                num1 = float(expression)
            else:
                num1 = int(expression)

            if num1 < 0:
                negativebool = True

            expression = str(Calclib.operation_abs(num1))

        self.lineEdit.setText(expression)
        if negativebool: # if num1 was negative, add '-' to expression for self.lineEdit_2.setText()
            expression = '-'+expression
        ############ end #####################################################################################


        if expression[-1] == button:
            expression = expression
        elif Calculator.last_button == ".":
            expression = expression[:-1]
            expression = button + expression + button
        else:
            #changed self.lineEdit.text to expression
            expression = button + expression + button

        ############ start #####################################################################################
        self.lineEdit_2.setText(expression)
        self.operatorbool = False  # none operator should be in expression after abs function
        ############ end #####################################################################################

        self.lineEdit.setFocus(False)
        Calculator.last_button = self.sender().text()

    ## Method buttonSquareroot_pressed
    # @brief Function reaction on square root button being clicked
    #
    # @param self The object pointer.
    def buttonSquareroot_pressed(self):
        button = "√"
        expression = self.lineEdit.text()  # getting value from lineEdit(calculator input) in the moment
        if expression[-1] == button:
            expression = expression
        # if last char is simple operator or float get rid of it
        elif expression[-1] == button or expression[-1] == "+" or expression[-1] == "-" or expression[-1] == "*" \
                or expression[-1] == "/" or expression[-1] == ".":
            expression = expression[:-1]
            expression = button + expression

            ############ start #####################################################################################
            self.operatorbool = True
            ############ end #####################################################################################
        else:
            ############ start #####################################################################################
            if self.operatorbool:
                self.expSolving()
            self.operatorbool = True
            ############ end #####################################################################################
            expression = button + self.lineEdit.text()

        # printing result into lineEdit
        self.lineEdit.setText(expression)
        self.lineEdit.setFocus(False)
        Calculator.last_button = str(button)

    ## Method buttonPower_pressed
    # @brief Function reaction on power button being clicked
    #
    # @param self The object pointer.
    def buttonPower_pressed(self):
        button = "ⁿ"
        expression = self.lineEdit.text()  # getting value from lineEdit(calculator input) in the moment

        ############ start #####################################################################################
        if self.operatorbool:
            self.expSolving()
            expression = self.lineEdit.text()
        self.operatorbool = True
        ############ end #####################################################################################

        # if last char is simple operator or float get rid of it
        if expression[-1] == button or expression[-1] == "+" or expression[-1] == "-" or expression[-1] == "*" \
                or expression[-1] == "/" or expression[-1] == ".":
            expression = expression[:-1]

        self.lineEdit.setText(expression)
        self.lineEdit.setFocus(False)
        Calculator.last_button = str(button)

