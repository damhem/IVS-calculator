# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Calculator_ui(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(400, 550)
        Dialog.setMinimumSize(QtCore.QSize(400, 550))
        Dialog.setMaximumSize(QtCore.QSize(400, 550))
        Dialog.setAccessibleName("")
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("background-color: rgb(71, 71, 71);")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(2, 150, 76, 76))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(22)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("QPushButton{background-color: rgb(116, 116, 116);\n"
                                        "    color:white;\n"
                                        "    border: 2px solid;\n"
                                        "    border-radius: 8px;\n"
                                        "     border-bottom: 4px solid;\n"
                                        "    border-right: 4px solid }\n"
                                        "QPushButton:hover{\n"
                                        "    background-color:white;    \n"
                                        "     color: black;}\n"
                                        "QPushButton:pressed{\n"
                                        "     border-bottom: 2px solid;\n"
                                        "    border-right: 2px solid\n"
                                        "    }")
        self.pushButton.setAutoDefault(True)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(82, 150, 76, 76))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(22)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("QPushButton{background-color: rgb(116, 116, 116);\n"
                                        "    color:white;\n"
                                        "    border: 2px solid;\n"
                                        "    border-radius: 8px;\n"
                                        "     border-bottom: 4px solid;\n"
                                        "    border-right: 4px solid }\n"
                                        "QPushButton:hover{\n"
                                        "    background-color:white;    \n"
                                        "     color: black;}\n"
                                        "QPushButton:pressed{\n"
                                        "     border-bottom: 2px solid;\n"
                                        "    border-right: 2px solid\n"
                                        "    }")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(162, 150, 76, 76))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(22)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet("QPushButton{background-color: rgb(116, 116, 116);\n"
                                        "    color:white;\n"
                                        "    border: 2px solid;\n"
                                        "    border-radius: 8px;\n"
                                        "     border-bottom: 4px solid;\n"
                                        "    border-right: 4px solid }\n"
                                        "QPushButton:hover{\n"
                                        "    background-color:white;    \n"
                                        "     color: black;}\n"
                                        "QPushButton:pressed{\n"
                                        "     border-bottom: 2px solid;\n"
                                        "    border-right: 2px solid\n"
                                        "    }")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(242, 150, 76, 76))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(22)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet("QPushButton{background-color:rgb(255, 126, 14);\n"
                                        "    color:black;\n"
                                        "    border: 2px solid;\n"
                                        "    border-radius: 8px;\n"
                                        "    border-bottom: 4px solid;\n"
                                        "    border-right: 4px solid}\n"
                                        "QPushButton:hover{\n"
                                        "    background-color:rgb(213, 213, 213);    \n"
                                        "     color: rgb(255, 126, 14);}\n"
                                        "QPushButton:pressed{\n"
                                        "    border-bottom: 2px solid;\n"
                                        "    border-right: 2px solid}\n"
                                        "")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(322, 150, 76, 76))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(22)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setStyleSheet("QPushButton{background-color:rgb(255, 126, 14);\n"
                                        "    color:black;\n"
                                        "    border: 2px solid;\n"
                                        "    border-radius: 8px;\n"
                                        "    border-bottom: 4px solid;\n"
                                        "    border-right: 4px solid}\n"
                                        "QPushButton:hover{\n"
                                        "    background-color:rgb(213, 213, 213);    \n"
                                        "     color: rgb(255, 126, 14);}\n"
                                        "QPushButton:pressed{\n"
                                        "    border-bottom: 2px solid;\n"
                                        "    border-right: 2px solid}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(82, 230, 76, 76))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(22)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setStyleSheet("QPushButton{background-color: rgb(242, 242, 242);\n"
                                        "    color:black;\n"
                                        "    border: 2px solid;\n"
                                        "    border-radius: 8px;\n"
                                        "     border-bottom: 4px solid;\n"
                                        "    border-right: 4px solid}\n"
                                        "QPushButton:hover{\n"
                                        "    background-color:rgb(50, 50, 50);    \n"
                                        "     color: white;}\n"
                                        "QPushButton:pressed{\n"
                                        "     border-bottom: 2px solid;\n"
                                        "    border-right: 2px solid}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(322, 230, 76, 76))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(22)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setAutoFillBackground(False)
        self.pushButton_7.setStyleSheet("QPushButton{background-color: rgb(116, 116, 116);\n"
                                        "    color:white;\n"
                                        "    border: 2px solid;\n"
                                        "    border-radius: 8px;\n"
                                        "     border-bottom: 4px solid;\n"
                                        "    border-right: 4px solid }\n"
                                        "QPushButton:hover{\n"
                                        "    background-color:white;    \n"
                                        "     color: black;}\n"
                                        "QPushButton:pressed{\n"
                                        "     border-bottom: 2px solid;\n"
                                        "    border-right: 2px solid\n"
                                        "    }")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(162, 230, 76, 76))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(22)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setAutoFillBackground(False)
        self.pushButton_8.setStyleSheet("QPushButton{background-color: rgb(242, 242, 242);\n"
                                        "    color:black;\n"
                                        "    border: 2px solid;\n"
                                        "    border-radius: 8px;\n"
                                        "     border-bottom: 4px solid;\n"
                                        "    border-right: 4px solid}\n"
                                        "QPushButton:hover{\n"
                                        "    background-color:rgb(50, 50, 50);    \n"
                                        "     color: white;}\n"
                                        "QPushButton:pressed{\n"
                                        "     border-bottom: 2px solid;\n"
                                        "    border-right: 2px solid}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(2, 230, 76, 76))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(22)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setAutoFillBackground(False)
        self.pushButton_9.setStyleSheet("QPushButton{background-color: rgb(242, 242, 242);\n"
                                        "    color:black;\n"
                                        "    border: 2px solid;\n"
                                        "    border-radius: 8px;\n"
                                        "     border-bottom: 4px solid;\n"
                                        "    border-right: 4px solid}\n"
                                        "QPushButton:hover{\n"
                                        "    background-color:rgb(50, 50, 50);    \n"
                                        "     color: white;}\n"
                                        "QPushButton:pressed{\n"
                                        "     border-bottom: 2px solid;\n"
                                        "    border-right: 2px solid}\n"
                                        "")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(242, 230, 76, 76))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(22)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setAutoFillBackground(False)
        self.pushButton_10.setStyleSheet("QPushButton{background-color: rgb(170, 170, 170);\n"
                                                "    color:black;\n"
                                                "    border: 2px solid;\n"
                                                "    border-radius: 8px;\n"
                                                "     border-bottom: 4px solid;\n"
                                                "    border-right: 4px solid}\n"
                                                "QPushButton:hover{\n"
                                                "    background-color:rgb(50, 50, 50);    \n"
                                                "     color: white;}\n"
                                                "QPushButton:pressed{\n"
                                                "     border-bottom: 2px solid;\n"
                                                "    border-right: 2px solid}\n"
                                                "")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(Dialog)
        self.pushButton_11.setGeometry(QtCore.QRect(162, 390, 76, 76))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(22)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setAutoFillBackground(False)
        self.pushButton_11.setStyleSheet("QPushButton{background-color: rgb(242, 242, 242);\n"
                                                "    color:black;\n"
                                                "    border: 2px solid;\n"
                                                "    border-radius: 8px;\n"
                                                "     border-bottom: 4px solid;\n"
                                                "    border-right: 4px solid}\n"
                                                "QPushButton:hover{\n"
                                                "    background-color:rgb(50, 50, 50);    \n"
                                                "     color: white;}\n"
                                                "QPushButton:pressed{\n"
                                                "     border-bottom: 2px solid;\n"
                                                "    border-right: 2px solid}")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(Dialog)
        self.pushButton_12.setGeometry(QtCore.QRect(82, 390, 76, 76))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(22)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setAutoFillBackground(False)
        self.pushButton_12.setStyleSheet("QPushButton{background-color: rgb(242, 242, 242);\n"
                                                "    color:black;\n"
                                                "    border: 2px solid;\n"
                                                "    border-radius: 8px;\n"
                                                "     border-bottom: 4px solid;\n"
                                                "    border-right: 4px solid}\n"
                                                "QPushButton:hover{\n"
                                                "    background-color:rgb(50, 50, 50);    \n"
                                                "     color: white;}\n"
                                                "QPushButton:pressed{\n"
                                                "     border-bottom: 2px solid;\n"
                                                "    border-right: 2px solid}")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(Dialog)
        self.pushButton_13.setGeometry(QtCore.QRect(242, 310, 76, 76))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(22)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_13.setAutoFillBackground(False)
        self.pushButton_13.setStyleSheet("QPushButton{background-color: rgb(170, 170, 170);\n"
                                                "    color:black;\n"
                                                "    border: 2px solid;\n"
                                                "    border-radius: 8px;\n"
                                                "     border-bottom: 4px solid;\n"
                                                "    border-right: 4px solid}\n"
                                                "QPushButton:hover{\n"
                                                "    background-color:rgb(50, 50, 50);    \n"
                                                "     color: white;}\n"
                                                "QPushButton:pressed{\n"
                                                "     border-bottom: 2px solid;\n"
                                                "    border-right: 2px solid}\n"
                                                "")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(Dialog)
        self.pushButton_14.setGeometry(QtCore.QRect(322, 390, 76, 156))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(22)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_14.setAutoFillBackground(False)
        self.pushButton_14.setStyleSheet("QPushButton{background-color: rgb(75, 75, 75);\n"
                                                "    color:white;\n"
                                                "    border: 2px solid;\n"
                                                "    border-radius: 8px;\n"
                                                "    border-bottom: 4px solid;\n"
                                                "    border-right: 4px solid}\n"
                                                "QPushButton:hover{\n"
                                                "    background-color:white;    \n"
                                                "     color: black;}\n"
                                                "QPushButton:pressed{\n"
                                                "    border-bottom: 2px solid;\n"
                                                "    border-right: 2px solid}\n"
                                                "")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(Dialog)
        self.pushButton_15.setGeometry(QtCore.QRect(2, 390, 76, 76))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(22)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_15.setAutoFillBackground(False)
        self.pushButton_15.setStyleSheet("QPushButton{background-color: rgb(242, 242, 242);\n"
                                                "    color:black;\n"
                                                "    border: 2px solid;\n"
                                                "    border-radius: 8px;\n"
                                                "     border-bottom: 4px solid;\n"
                                                "    border-right: 4px solid}\n"
                                                "QPushButton:hover{\n"
                                                "    background-color:rgb(50, 50, 50);    \n"
                                                "     color: white;}\n"
                                                "QPushButton:pressed{\n"
                                                "     border-bottom: 2px solid;\n"
                                                "    border-right: 2px solid}")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(Dialog)
        self.pushButton_16.setGeometry(QtCore.QRect(82, 310, 76, 76))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(22)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_16.setAutoFillBackground(False)
        self.pushButton_16.setStyleSheet("QPushButton{background-color: rgb(242, 242, 242);\n"
                                                "    color:black;\n"
                                                "    border: 2px solid;\n"
                                                "    border-radius: 8px;\n"
                                                "     border-bottom: 4px solid;\n"
                                                "    border-right: 4px solid}\n"
                                                "QPushButton:hover{\n"
                                                "    background-color:rgb(50, 50, 50);    \n"
                                                "     color: white;}\n"
                                                "QPushButton:pressed{\n"
                                                "     border-bottom: 2px solid;\n"
                                                "    border-right: 2px solid}")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(Dialog)
        self.pushButton_17.setGeometry(QtCore.QRect(322, 310, 76, 76))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(22)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_17.setAutoFillBackground(False)
        self.pushButton_17.setStyleSheet("QPushButton{background-color: rgb(116, 116, 116);\n"
                                                "    color:white;\n"
                                                "    border: 2px solid;\n"
                                                "    border-radius: 8px;\n"
                                                "     border-bottom: 4px solid;\n"
                                                "    border-right: 4px solid }\n"
                                                "QPushButton:hover{\n"
                                                "    background-color:white;    \n"
                                                "     color: black;}\n"
                                                "QPushButton:pressed{\n"
                                                "     border-bottom: 2px solid;\n"
                                                "    border-right: 2px solid\n"
                                                "    }")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(Dialog)
        self.pushButton_18.setGeometry(QtCore.QRect(242, 390, 76, 76))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(22)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_18.setAutoFillBackground(False)
        self.pushButton_18.setStyleSheet("QPushButton{background-color: rgb(170, 170, 170);\n"
                                                "    color:black;\n"
                                                "    border: 2px solid;\n"
                                                "    border-radius: 8px;\n"
                                                "     border-bottom: 4px solid;\n"
                                                "    border-right: 4px solid}\n"
                                                "QPushButton:hover{\n"
                                                "    background-color:rgb(50, 50, 50);    \n"
                                                "     color: white;}\n"
                                                "QPushButton:pressed{\n"
                                                "     border-bottom: 2px solid;\n"
                                                "    border-right: 2px solid}\n"
                                                "")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(Dialog)
        self.pushButton_19.setGeometry(QtCore.QRect(162, 310, 76, 76))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(22)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_19.setAutoFillBackground(False)
        self.pushButton_19.setStyleSheet("QPushButton{background-color: rgb(242, 242, 242);\n"
                                                "    color:black;\n"
                                                "    border: 2px solid;\n"
                                                "    border-radius: 8px;\n"
                                                "     border-bottom: 4px solid;\n"
                                                "    border-right: 4px solid}\n"
                                                "QPushButton:hover{\n"
                                                "    background-color:rgb(50, 50, 50);    \n"
                                                "     color: white;}\n"
                                                "QPushButton:pressed{\n"
                                                "     border-bottom: 2px solid;\n"
                                                "    border-right: 2px solid}")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(Dialog)
        self.pushButton_20.setGeometry(QtCore.QRect(2, 310, 76, 76))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(22)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_20.setAutoFillBackground(False)
        self.pushButton_20.setStyleSheet("QPushButton{background-color: rgb(242, 242, 242);\n"
                                                "    color:black;\n"
                                                "    border: 2px solid;\n"
                                                "    border-radius: 8px;\n"
                                                "     border-bottom: 4px solid;\n"
                                                "    border-right: 4px solid}\n"
                                                "QPushButton:hover{\n"
                                                "    background-color:rgb(50, 50, 50);    \n"
                                                "     color: white;}\n"
                                                "QPushButton:pressed{\n"
                                                "     border-bottom: 2px solid;\n"
                                                "    border-right: 2px solid}")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(Dialog)
        self.pushButton_21.setGeometry(QtCore.QRect(242, 470, 76, 76))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(22)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_21.setAutoFillBackground(False)
        self.pushButton_21.setStyleSheet("QPushButton{background-color: rgb(170, 170, 170);\n"
                                                "    color:black;\n"
                                                "    border: 2px solid;\n"
                                                "    border-radius: 8px;\n"
                                                "     border-bottom: 4px solid;\n"
                                                "    border-right: 4px solid}\n"
                                                "QPushButton:hover{\n"
                                                "    background-color:rgb(50, 50, 50);    \n"
                                                "     color: white;}\n"
                                                "QPushButton:pressed{\n"
                                                "     border-bottom: 2px solid;\n"
                                                "    border-right: 2px solid}\n"
                                                "")
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(Dialog)
        self.pushButton_22.setGeometry(QtCore.QRect(82, 470, 76, 76))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(22)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_22.setAutoFillBackground(False)
        self.pushButton_22.setStyleSheet("QPushButton{background-color: rgb(242, 242, 242);\n"
                                                "    color:black;\n"
                                                "    border: 2px solid;\n"
                                                "    border-radius: 8px;\n"
                                                "     border-bottom: 4px solid;\n"
                                                "    border-right: 4px solid}\n"
                                                "QPushButton:hover{\n"
                                                "    background-color:rgb(50, 50, 50);    \n"
                                                "     color: white;}\n"
                                                "QPushButton:pressed{\n"
                                                "     border-bottom: 2px solid;\n"
                                                "    border-right: 2px solid}")
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_24 = QtWidgets.QPushButton(Dialog)
        self.pushButton_24.setGeometry(QtCore.QRect(2, 470, 76, 76))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(22)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_24.setAutoFillBackground(False)
        self.pushButton_24.setStyleSheet("QPushButton{background-color: rgb(116, 116, 116);\n"
                                                "    color:white;\n"
                                                "    border: 2px solid;\n"
                                                "    border-radius: 8px;\n"
                                                "     border-bottom: 4px solid;\n"
                                                "    border-right: 4px solid }\n"
                                                "QPushButton:hover{\n"
                                                "    background-color:white;    \n"
                                                "     color: black;}\n"
                                                "QPushButton:pressed{\n"
                                                "     border-bottom: 2px solid;\n"
                                                "    border-right: 2px solid\n"
                                                "    }")
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(Dialog)
        self.pushButton_25.setGeometry(QtCore.QRect(162, 470, 76, 76))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(22)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_25.setAutoFillBackground(False)
        self.pushButton_25.setStyleSheet("QPushButton{background-color: rgb(170, 170, 170);\n"
                                                "    color:black;\n"
                                                "    border: 2px solid;\n"
                                                "    border-radius: 8px;\n"
                                                "     border-bottom: 4px solid;\n"
                                                "    border-right: 4px solid}\n"
                                                "QPushButton:hover{\n"
                                                "    background-color:rgb(50, 50, 50);    \n"
                                                "     color: white;}\n"
                                                "QPushButton:pressed{\n"
                                                "     border-bottom: 2px solid;\n"
                                                "    border-right: 2px solid}\n"
                                                "")
        self.pushButton_25.setObjectName("pushButton_25")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(3, 58, 394, 82))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(28)
        font.setBold(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        " border-bottom-right-radius: 8px;\n"
                                        " border-bottom-left-radius: 8px;\n"
                                        "")
        self.lineEdit.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(3, 5, 394, 54))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "color:black;\n"
                                        " border-top-right-radius: 8px;\n"
                                        " border-top-left-radius: 8px;\n"
                                        "padding-bottom:5px")
        self.lineEdit_2.setMaxLength(256)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "n!"))
        self.pushButton_2.setText(_translate("Dialog", "("))
        self.pushButton_3.setText(_translate("Dialog", ")"))
        self.pushButton_4.setText(_translate("Dialog", "DEL"))
        self.pushButton_5.setText(_translate("Dialog", "CE"))
        self.pushButton_6.setText(_translate("Dialog", "8"))
        self.pushButton_7.setText(_translate("Dialog", "xⁿ"))
        self.pushButton_8.setText(_translate("Dialog", "9"))
        self.pushButton_9.setText(_translate("Dialog", "7"))
        self.pushButton_10.setText(_translate("Dialog", "+"))
        self.pushButton_11.setText(_translate("Dialog", "3"))
        self.pushButton_12.setText(_translate("Dialog", "2"))
        self.pushButton_13.setText(_translate("Dialog", "-"))
        self.pushButton_14.setText(_translate("Dialog", "="))
        self.pushButton_15.setText(_translate("Dialog", "1"))
        self.pushButton_16.setText(_translate("Dialog", "5"))
        self.pushButton_17.setText(_translate("Dialog", "ⁿ√x"))
        self.pushButton_18.setText(_translate("Dialog", "*"))
        self.pushButton_19.setText(_translate("Dialog", "6"))
        self.pushButton_20.setText(_translate("Dialog", "4"))
        self.pushButton_21.setText(_translate("Dialog", "/"))
        self.pushButton_22.setText(_translate("Dialog", "0"))
        self.pushButton_24.setText(_translate("Dialog", "|x|"))
        self.pushButton_25.setText(_translate("Dialog", ","))
        self.lineEdit.setText(_translate("Dialog", "0"))
        self.lineEdit_2.setText(_translate("Dialog", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()

    ui = Calculator_ui()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())