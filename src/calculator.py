from PyQt5 import QtWidgets, QtCore
from gui import Calculator_ui
from PyQt5 import QtGui
from PyQt5.QtGui import *
import os


class Calculator(QtWidgets.QMainWindow, Calculator_ui):
    last_button = ""

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon("cal.png"))
        self.setupUi(self)
        self.show()

        # numbers
        self.pushButton_6.clicked.connect(self.buttonNumber2_pressed)
        self.pushButton_8.clicked.connect(self.buttonNumber_pressed)
        self.pushButton_9.clicked.connect(self.buttonNumber_pressed)
        self.pushButton_11.clicked.connect(self.buttonNumber_pressed)
        self.pushButton_12.clicked.connect(self.buttonNumber_pressed)
        self.pushButton_15.clicked.connect(self.buttonNumber_pressed)
        self.pushButton_16.clicked.connect(self.buttonNumber_pressed)
        self.pushButton_19.clicked.connect(self.buttonNumber_pressed)
        self.pushButton_20.clicked.connect(self.buttonNumber_pressed)
        self.pushButton_22.clicked.connect(self.buttonNumber_pressed)

        # DEL
        self.pushButton_4.clicked.connect(self.buttonDelete1_pressed)
        # AC
        self.pushButton_5.clicked.connect(self.buttonDelete_pressed)
        # simple
        self.pushButton_21.clicked.connect(self.buttonSimple_pressed)
        self.pushButton_18.clicked.connect(self.buttonSimple_pressed)
        self.pushButton_25.clicked.connect(self.buttonSimple_pressed)
        self.pushButton_13.clicked.connect(self.buttonSimple_pressed)
        self.pushButton_10.clicked.connect(self.buttonSimple_pressed)
        # solve
        self.pushButton_14.clicked.connect(self.buttonSolve_pressed)
        # brackets
        self.pushButton_2.clicked.connect(self.buttonBrackets_pressed)
        self.pushButton_3.clicked.connect(self.buttonBrackets_pressed)
        # factorial
        self.pushButton.clicked.connect(self.buttonFactorial_pressed)
        # absolute
        self.pushButton_24.clicked.connect(self.buttonAbsolute_pressed)
        # square root
        self.pushButton_17.clicked.connect(self.buttonSquareroot_pressed)
        # power
        self.pushButton_7.clicked.connect(self.buttonPower_pressed)

    def buttonNumber_pressed(self):
        button = self.sender()
        expression = self.lineEdit.text()
        if expression == "0":
            expression = button.text()
        else:
            expression = self.lineEdit.text() + button.text()
        self.lineEdit.setText(expression)
        self.lineEdit.setFocus(False)
        Calculator.last_button = self.sender().text()

    def buttonNumber2_pressed(self):
        button = "⁸"
        expression = self.lineEdit.text()
        if expression == "0":
            expression = button
        else:
            expression = self.lineEdit.text() + button
        self.lineEdit.setText(expression)
        self.lineEdit.setFocus(False)
        Calculator.last_button = self.sender().text()

    def buttonDelete_pressed(self):
        expression = "0"
        if Calculator.last_button == "CE":
            self.lineEdit.setText(expression)
            self.lineEdit_2.setText("")
            self.lineEdit.setFocus(False)
        else:
            self.lineEdit.setText(expression)
            self.lineEdit.setFocus(False)

        Calculator.last_button = self.sender().text()

    def buttonDelete1_pressed(self):
        expression = self.lineEdit.text()
        if expression[:-1] == "":
            expression = "0"
        elif expression == "":
            expression = "0"
        else:
            expression = expression[:-1]

        self.lineEdit.setText(expression)
        self.lineEdit.setFocus(False)
        global last_button
        last_button = self.sender().text()
        Calculator.last_button = self.sender().text()

    def buttonSimple_pressed(self):
        button = self.sender()
        expression = self.lineEdit.text()
        if expression[-1] == button.text():
            expression = expression
        else:
            expression = self.lineEdit.text() + button.text()
        self.lineEdit.setText(expression)
        self.lineEdit.setFocus(False)
        Calculator.last_button = self.sender().text()

    def buttonSolve_pressed(self):
        expression = self.lineEdit.text()
        self.lineEdit_2.setText(expression)
        self.lineEdit.setText("0")
        self.lineEdit.setFocus(False)
        Calculator.last_button = self.sender().text()

    def buttonBrackets_pressed(self):
        button = self.sender()
        expression = self.lineEdit.text()
        if expression == "0":
            expression = button.text()
        else:
            expression = self.lineEdit.text() + button.text()
        self.lineEdit.setText(expression)
        self.lineEdit.setFocus(False)
        Calculator.last_button = self.sender().text()

    def buttonFactorial_pressed(self):
        button = "!"
        expression = self.lineEdit.text()
        if expression == "0":
            expression = button
        elif expression[-1] == button:
            expression = expression
        else:
            expression = self.lineEdit.text() + button
        self.lineEdit.setText(expression)
        self.lineEdit.setFocus(False)
        Calculator.last_button = self.sender().text()

    def buttonAbsolute_pressed(self):
        button = "|"
        expression = self.lineEdit.text()
        if expression[-1] == button:
            expression = expression
        else:
            expression = button + self.lineEdit.text() + button
        self.lineEdit.setText(expression)
        self.lineEdit.setFocus(False)
        Calculator.last_button = self.sender().text()

    def buttonSquareroot_pressed(self):
        button = "¹√"
        expression = self.lineEdit.text()
        if expression[-1] == button:
            expression = expression
        else:
            expression = button + self.lineEdit.text()
        self.lineEdit.setText(expression)
        self.lineEdit.setFocus(False)
        Calculator.last_button = self.sender().text()

    def buttonPower_pressed(self):
        button = "ⁿ"
        expression = self.lineEdit.text()
        if expression[-1] == button:
            expression = expression
        else:
            expression = self.lineEdit.text() +button
        self.lineEdit.setText(expression)
        self.lineEdit.setFocus(False)
        Calculator.last_button = self.sender().text()