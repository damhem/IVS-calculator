#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication
from calculator import Calculator
##
#   @file main.py
#
#   @brief Launches the whole calculator
#   @author Daniel Čechák, xcecha06
#



app = QApplication(sys.argv)

calculator = Calculator()

sys.exit(app.exec_())
