# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Exercise4.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        self.setupUi(MainWindow)
        self.setFuction()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 150, 251, 31))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.canelBT = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canelBT.sizePolicy().hasHeightForWidth())
        self.canelBT.setSizePolicy(sizePolicy)
        self.canelBT.setMaximumSize(QtCore.QSize(70, 23))
        self.canelBT.setObjectName("canelBT")
        self.gridLayout.addWidget(self.canelBT, 0, 1, 1, 1)
        self.okBt = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okBt.sizePolicy().hasHeightForWidth())
        self.okBt.setSizePolicy(sizePolicy)
        self.okBt.setMaximumSize(QtCore.QSize(70, 23))
        self.okBt.setObjectName("okBt")
        self.gridLayout.addWidget(self.okBt, 0, 0, 1, 1)
        self.applyBT = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.applyBT.sizePolicy().hasHeightForWidth())
        self.applyBT.setSizePolicy(sizePolicy)
        self.applyBT.setMaximumSize(QtCore.QSize(70, 23))
        self.applyBT.setObjectName("applyBT")
        self.gridLayout.addWidget(self.applyBT, 0, 2, 1, 1)
        self.hourLabel = QtWidgets.QLabel(self.centralwidget)
        self.hourLabel.setGeometry(QtCore.QRect(43, 60, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(36)
        self.hourLabel.setFont(font)
        self.hourLabel.setObjectName("hourLabel")
        self.minLabel = QtWidgets.QLabel(self.centralwidget)
        self.minLabel.setGeometry(QtCore.QRect(133, 60, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(36)
        self.minLabel.setFont(font)
        self.minLabel.setObjectName("minLabel")
        self.secLabel = QtWidgets.QLabel(self.centralwidget)
        self.secLabel.setGeometry(QtCore.QRect(220, 60, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(36)
        self.secLabel.setFont(font)
        self.secLabel.setObjectName("secLabel")
        self.hourPlus = QtWidgets.QPushButton(self.centralwidget)
        self.hourPlus.setGeometry(QtCore.QRect(90, 60, 20, 20))
        self.hourPlus.setObjectName("hourPlus")
        self.hourMius = QtWidgets.QPushButton(self.centralwidget)
        self.hourMius.setGeometry(QtCore.QRect(90, 80, 20, 20))
        self.hourMius.setObjectName("hourMius")
        self.minPlus = QtWidgets.QPushButton(self.centralwidget)
        self.minPlus.setGeometry(QtCore.QRect(180, 60, 20, 20))
        self.minPlus.setObjectName("minPlus")
        self.minMinus = QtWidgets.QPushButton(self.centralwidget)
        self.minMinus.setGeometry(QtCore.QRect(180, 80, 20, 20))
        self.minMinus.setObjectName("minMinus")
        self.secPlus = QtWidgets.QPushButton(self.centralwidget)
        self.secPlus.setGeometry(QtCore.QRect(270, 60, 20, 20))
        self.secPlus.setObjectName("secPlus")
        self.secMinus = QtWidgets.QPushButton(self.centralwidget)
        self.secMinus.setGeometry(QtCore.QRect(270, 80, 20, 20))
        self.secMinus.setObjectName("secMinus")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.canelBT.clicked.connect(MainWindow.close)
        self.okBt.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Exercise 4"))
        self.canelBT.setText(_translate("MainWindow", "Cancel"))
        self.okBt.setText(_translate("MainWindow", "OK"))
        self.applyBT.setText(_translate("MainWindow", "Apply"))
        self.hourLabel.setText(_translate("MainWindow", "00"))
        self.minLabel.setText(_translate("MainWindow", "00"))
        self.secLabel.setText(_translate("MainWindow", "00"))
        self.hourPlus.setText(_translate("MainWindow", "+"))
        self.hourMius.setText(_translate("MainWindow", "-"))
        self.minPlus.setText(_translate("MainWindow", "+"))
        self.minMinus.setText(_translate("MainWindow", "-"))
        self.secPlus.setText(_translate("MainWindow", "+"))
        self.secMinus.setText(_translate("MainWindow", "-"))

    def setFuction(self):
        self.hourPlus.clicked.connect(self.Addhour)
        self.hourMius.clicked.connect(self.Dechour)
        self.minPlus.clicked.connect(self.Addmin)
        self.minMinus.clicked.connect(self.Decmin)
        self.secPlus.clicked.connect(self.Addsec)
        self.secMinus.clicked.connect(self.Decsec)

    def Addhour(self):
        hour = int(self.hourLabel.text())
        hour += 1
        if hour > 23:
            hour = 0
        if hour < 10:
            hour = "0" + str(hour)
        else:
            hour = str(hour)
        self.hourLabel.setText(hour)

    def Dechour(self):
        hour = int(self.hourLabel.text())
        hour -= 1
        if hour < 0:
            hour = 23
        if hour < 10:
            hour = "0" + str(hour)
        else:
            hour = str(hour)
        self.hourLabel.setText(str(hour))

    def Addmin(self):
        min = int(self.minLabel.text())
        min += 1
        if min > 60:
            min = 0
            self.Addhour()
        if min < 10:
            min = "0" + str(min)
        else:
            min = str(min)
        self.minLabel.setText(str(min))

    def Decmin(self):
        min = int(self.minLabel.text())
        min -= 1
        if min < 0:
            min = 59
            self.Dechour()
        if min < 10:
            min = "0" + str(min)
        else:
            min = str(min)
        self.minLabel.setText(str(min))

    def Addsec(self):
        sec = int(self.secLabel.text())
        sec += 1
        if sec > 60:
            sec = 0
            self.Addmin()
        if sec < 10:
            sec = "0" + str(sec)
        else:
            sec = str(sec)
        self.secLabel.setText(str(sec))

    def Decsec(self):
        sec = int(self.secLabel.text())
        sec -= 1
        if sec < 0:
            sec = 59
            self.Decmin()
        if sec < 10:
            sec = "0" + str(sec)
        else:
            sec = str(sec)
        self.secLabel.setText(str(sec))
    #改变数值的方法

if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QMainWindow()  # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = Ui_MainWindow(MainWindow)  # ui是Ui_MainWindow()类的实例化对象
    MainWindow.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出QApplication
