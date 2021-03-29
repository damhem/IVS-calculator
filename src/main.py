#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication
from calculator import Calculator

app = QApplication(sys.argv)

calculator = Calculator()

sys.exit(app.exec_())
