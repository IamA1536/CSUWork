# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SystemScheduling_UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import random

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QFont, QPalette, QColor
from PyQt5.QtWidgets import QMessageBox, QAbstractItemView, QFrame

from com.a.OperateSystem.CPU_Funtion.thread import timePass


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        self.setupUi(MainWindow)
        self.backList = []
        self.memoryList = []
        self.pcount = 0
        self.rcount = 0
        self.runPID = ""
        self.runName = ""
        self.totalTime = 0
        self.lastTime = 0
        self.pAddress = 0
        self.pMemory = 0
        self.setFunction()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(810, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(140, 10, 366, 58))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.runProgress = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.runProgress.setEnabled(False)
        self.runProgress.setMaximumSize(QtCore.QSize(100, 30))
        self.runProgress.setProperty("value", 0)
        self.runProgress.setTextVisible(False)
        self.runProgress.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.runProgress.setObjectName("runProgress")
        self.gridLayout.addWidget(self.runProgress, 0, 1, 1, 1)
        self.runEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.runEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runEdit.sizePolicy().hasHeightForWidth())
        self.runEdit.setSizePolicy(sizePolicy)
        self.runEdit.setMinimumSize(QtCore.QSize(300, 0))
        self.runEdit.setMaximumSize(QtCore.QSize(300, 30))
        self.runEdit.setObjectName("runEdit")
        self.gridLayout.addWidget(self.runEdit, 0, 0, 1, 1)
        self.ableTV = QtWidgets.QTableView(self.centralwidget)
        self.ableTV.setGeometry(QtCore.QRect(40, 100, 250, 400))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ableTV.sizePolicy().hasHeightForWidth())
        self.ableTV.setSizePolicy(sizePolicy)
        self.ableTV.setObjectName("ableTV")
        self.blockTV = QtWidgets.QTableView(self.centralwidget)
        self.blockTV.setGeometry(QtCore.QRect(360, 100, 250, 400))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blockTV.sizePolicy().hasHeightForWidth())
        self.blockTV.setSizePolicy(sizePolicy)
        self.blockTV.setObjectName("blockTV")
        self.BlockBt = QtWidgets.QPushButton(self.centralwidget)
        self.BlockBt.setGeometry(QtCore.QRect(290, 200, 71, 23))
        self.BlockBt.setObjectName("BlockBt")
        self.resumeBt = QtWidgets.QPushButton(self.centralwidget)
        self.resumeBt.setGeometry(QtCore.QRect(290, 360, 71, 23))
        self.resumeBt.setObjectName("resumeBt")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(130, 540, 440, 51))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pTimetextEdit = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.pTimetextEdit.setMaximumSize(QtCore.QSize(50, 30))
        self.pTimetextEdit.setObjectName("pTimetextEdit")
        self.gridLayout_2.addWidget(self.pTimetextEdit, 0, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit.setMaximumSize(QtCore.QSize(240, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.acceptBt = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.acceptBt.setMaximumSize(QtCore.QSize(75, 30))
        self.acceptBt.setObjectName("acceptBt")
        self.gridLayout_2.addWidget(self.acceptBt, 0, 3, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMaximumSize(QtCore.QSize(50, 30))
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 0, 2, 1, 1)
        self.Memorylabel = QtWidgets.QLabel(self.centralwidget)
        self.Memorylabel.setGeometry(QtCore.QRect(700, 80, 40, 15))
        self.Memorylabel.setObjectName("Memorylabel")
        self.nameLabl = QtWidgets.QLabel(self.centralwidget)
        self.nameLabl.setGeometry(QtCore.QRect(240, 520, 54, 12))
        self.nameLabl.setObjectName("nameLabl")
        self.timeLabel = QtWidgets.QLabel(self.centralwidget)
        self.timeLabel.setGeometry(QtCore.QRect(380, 520, 54, 12))
        self.timeLabel.setObjectName("timeLabel")
        self.memoryLabel = QtWidgets.QLabel(self.centralwidget)
        self.memoryLabel.setGeometry(QtCore.QRect(440, 520, 54, 12))
        self.memoryLabel.setObjectName("memoryLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.runProgress.setFormat(_translate("MainWindow", "%p%"))
        self.BlockBt.setText(_translate("MainWindow", "Block"))
        self.resumeBt.setText(_translate("MainWindow", "Resume"))
        self.acceptBt.setText(_translate("MainWindow", "Accept"))
        self.Memorylabel.setText(_translate("MainWindow", "Memory"))
        self.nameLabl.setText(_translate("MainWindow", "Name:"))
        self.timeLabel.setText(_translate("MainWindow", "Time"))
        self.memoryLabel.setText(_translate("MainWindow", "Memory"))

    def setFunction(self):
        self.setMemory()
        self.runEdit.setFont(QFont("Timers", 9))

        self.aModel = QStandardItemModel()
        self.bModel = QStandardItemModel()
        self.setHeader(self.aModel)
        self.setHeader(self.bModel)
        self.ableTV.setModel(self.aModel)
        self.blockTV.setModel(self.bModel)
        self.ableTV.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ableTV.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ableTV.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.blockTV.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.blockTV.setSelectionMode(QAbstractItemView.SingleSelection)
        self.blockTV.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.acceptBt.clicked.connect(self.accept)
        self.BlockBt.clicked.connect(self.toBlock)
        self.resumeBt.clicked.connect(self.resumeFromBlock)

        self.changeStatus = timePass()
        self.changeStatus.msg.connect(self.change)
        self.changeStatus.start()

    def setMemory(self):
        for i in range(16):
            mLabel = QtWidgets.QLabel(self.centralwidget)
            mLabel.setGeometry(QtCore.QRect(695, 95 + i * 25, 50, 25))
            mLabel.setText(str(i))
            mLabel.setFrameShape(QFrame.Box)
            pal = QPalette()
            pal.setColor(QPalette.Background, QColor(255, 255, 255))
            mLabel.setPalette(pal)
            mLabel.setAutoFillBackground(True)
            self.memoryList.append([mLabel, True])

    def change(self):
        self.scheldue()
        self.timechange()

    def scheldue(self):
        self.memoryAvaliableList = []
        i = 0
        maxm = 0
        while i < 15:
            c = 0
            while self.memoryList[i][1] and i < 15:
                c += 1
                i += 1
                maxm = max(maxm, c)
            self.memoryAvaliableList.append([i - c, c])
            i += 1
        self.memoryAvaliableList.sort(key=lambda x: x[1])
        if self.aModel.rowCount() > 0 and self.runProgress.value() == 0:
            self.runPID = self.aModel.item(0, 0).text()
            self.runName = self.aModel.item(0, 1).text()
            self.totalTime = int(self.aModel.item(0, 2).text())
            self.lastTime = self.totalTime
            self.pAddress = int(self.aModel.item(0, 4).text())
            self.pMemory = int(self.aModel.item(0, 5).text())
            self.runEdit.setPlainText(
                "{0}({1}) is running, the last time is {2}".format(self.runPID, self.runName, self.lastTime))
            self.runProgress.setValue(100)
            self.aModel.removeRow(0)
        elif self.runProgress.value() != 0:
            self.runProgress.setValue(int(100 * (1.0 * self.lastTime / self.totalTime)))
        elif self.aModel.rowCount() == 0 and self.runProgress.value() == 0:
            self.runEdit.setPlainText("")
        if self.runEdit == "":
            isRun = 0
        else:
            isRun = 1
        t = len(self.backList)
        for i in range(len(self.backList)):
            if self.backList[i][3] <= maxm:
                t = i
                break
        if self.aModel.rowCount() + self.bModel.rowCount() + isRun < 5 and len(self.backList) > 0 and t != len(
                self.backList):
            for i in range(len(self.memoryAvaliableList)):
                if self.memoryAvaliableList[i][1] >= self.backList[t][3]:
                    a = self.memoryAvaliableList[i][0]
                    break
            rows = self.aModel.rowCount()
            pal = QPalette()
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            pal.setColor(QPalette.Background, QColor(r, g, b))
            for i in range(a, a + self.backList[t][3]):
                self.useMemory(i, pal)

            for i in range(2):
                self.aModel.setItem(rows, i, QStandardItem(self.backList[t][i]))
            item = QStandardItem()
            item.setData(self.backList[t][2], 2)
            self.aModel.setItem(rows, 2, item)
            self.aModel.setItem(rows, 3, QStandardItem("Ready"))
            item2 = QStandardItem()
            item2.setData(a, 2)

            self.aModel.setItem(rows, 4, item2)
            item3 = QStandardItem()
            item3.setData(self.backList[t][3], 2)
            self.aModel.setItem(rows, 5, item3)
            self.aModel.sort(2)
            del (self.backList[t])

    def useMemory(self, n, pal):
        self.memoryList[n][0].setPalette(pal)
        self.memoryList[n][1] = False

    def timechange(self):
        self.lastTime -= 1
        if self.runProgress.value() != 0:
            self.runEdit.setPlainText(
                "{0}({1}) is running, the last time is {2}".format(self.runPID, self.runName, self.lastTime))
        else:
            self.runEdit.setPlainText("System Performance ......")
            pal = QPalette()
            pal.setColor(QPalette.Background, QColor(255, 255, 255))
            for i in range(self.pAddress, self.pAddress + self.pMemory):
                self.memoryList[i][0].setPalette(pal)
                self.memoryList[i][1] = True

    def setHeader(self, QStandardItemModels):
        QStandardItemModels.setHorizontalHeaderItem(0, QStandardItem("PID"))
        QStandardItemModels.setHorizontalHeaderItem(1, QStandardItem("Name"))
        QStandardItemModels.setHorizontalHeaderItem(2, QStandardItem("RunTime"))
        QStandardItemModels.setHorizontalHeaderItem(3, QStandardItem("Status"))
        QStandardItemModels.setHorizontalHeaderItem(4, QStandardItem("Address"))
        QStandardItemModels.setHorizontalHeaderItem(5, QStandardItem("Memory"))

    def accept(self):
        if self.lineEdit.text() == "":
            QMessageBox(QMessageBox.Warning, "Error", "Please input the ID").exec()
        elif self.pTimetextEdit.toPlainText() == "":
            QMessageBox(QMessageBox.Warning, "Error", "Please input the time").exec()
        elif self.textEdit.toPlainText() == "":
            QMessageBox(QMessageBox.Warning, "Error", "Please input the memory").exec()
        else:
            PID = "p{0}".format(self.pcount)
            self.pcount += 1
            name = self.lineEdit.text()
            runtime = int(self.pTimetextEdit.toPlainText())
            memory = int(self.textEdit.toPlainText())
            str = "{0} {1} {2} {3}".format(PID, name, runtime, memory)
            self.backList.append([i for i in str.split(" ")])
            self.backList[len(self.backList) - 1][2] = int(self.backList[len(self.backList) - 1][2])
            self.backList[len(self.backList) - 1][3] = int(self.backList[len(self.backList) - 1][3])
            self.backList.sort(key=lambda x: (x[2], x[3]))
            self.lineEdit.setText("")
            self.pTimetextEdit.setPlainText("")
            self.textEdit.setText("")
            QMessageBox(QMessageBox.Information, "Success!", "Succeed to creat a progress!").exec()

    def toBlock(self):
        if len(self.ableTV.selectedIndexes()) != 0:
            self.move(self.aModel, self.bModel, self.ableTV)
        else:
            if self.runProgress.value() != 0:
                rows = self.bModel.rowCount()
                self.bModel.setItem(rows, 0, QStandardItem(self.runPID))
                self.bModel.setItem(rows, 1, QStandardItem(self.runName))
                self.bModel.setItem(rows, 2, QStandardItem(str(self.lastTime)))
                self.bModel.setItem(rows, 3, QStandardItem("Blocked"))
                self.bModel.setItem(rows, 4, QStandardItem(str(self.pAddress)))
                self.bModel.setItem(rows, 5, QStandardItem(str(self.pMemory)))
                self.runProgress.setValue(0)
                self.runEdit.setPlainText("System Performance ......")

    def resumeFromBlock(self):
        if len(self.blockTV.selectedIndexes()) != 0:
            self.move(self.bModel, self.aModel, self.blockTV)

    def move(self, MODEL1, MODEL2, TABLE):
        row = TABLE.currentIndex().row()
        NAME = MODEL1.item(row, 0).text()
        PID = MODEL1.item(row, 1).text()
        TIME = int(MODEL1.item(row, 2).text())
        ADDRESS = int(MODEL1.item(row, 4).text())
        MEMORY = int(MODEL1.item(row, 5).text())
        MODEL1.removeRow(row)
        Item_TIME = QStandardItem()
        Item_TIME.setData(TIME, 2)
        Item_ADDRESS = QStandardItem()
        Item_ADDRESS.setData(ADDRESS, 2)
        Item_Memroy = QStandardItem()
        Item_Memroy.setData(MEMORY, 2)
        countRow = MODEL2.rowCount()
        MODEL2.setItem(countRow, 0, QStandardItem(NAME))
        MODEL2.setItem(countRow, 1, QStandardItem(PID))
        MODEL2.setItem(countRow, 2, Item_TIME)
        MODEL2.setItem(countRow, 4, Item_ADDRESS)
        MODEL2.setItem(countRow, 5, Item_Memroy)
        if MODEL2 == self.bModel:
            MODEL2.setItem(countRow, 3, QStandardItem("Blocked"))
        elif MODEL2 == self.aModel:
            MODEL2.setItem(countRow, 3, QStandardItem("Ready"))
            self.aModel.sort(2)
        TABLE.clearSelection()
