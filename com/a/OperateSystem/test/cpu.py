# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cpu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMessageBox, QAbstractItemView
from PyQt5.QtCore import pyqtSignal, QObject
import sys, time


class Ui_MainWindow(object):
    def __init__(self):
        self.setupUi(MainWindow)
        self.Ready_Model = QStandardItemModel()
        self.Waiting_Model = QStandardItemModel()
        self.Runing_Model = QStandardItemModel()
        self.Locked_Model = QStandardItemModel()
        self.IDS = []
        self.setupFunction()

    def closeEvent(self):
        sys.exit(app.exec_())

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(775, 506)
        MainWindow.setFixedSize(775, 506)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.PCBS_Waiting = QtWidgets.QTableView(self.centralwidget)
        self.PCBS_Waiting.setGeometry(QtCore.QRect(20, 260, 256, 192))
        self.PCBS_Waiting.setObjectName("PCBS_Waiting")
        self.ADDPCB = QtWidgets.QPushButton(self.centralwidget)
        self.ADDPCB.setGeometry(QtCore.QRect(600, 310, 75, 20))
        self.ADDPCB.setObjectName("ADDPCB")
        self.PCBS_Ready = QtWidgets.QTableView(self.centralwidget)
        self.PCBS_Ready.setGeometry(QtCore.QRect(320, 30, 256, 192))
        self.PCBS_Ready.setObjectName("PCBS_Ready")
        self.PCBS_Locked = QtWidgets.QTableView(self.centralwidget)
        self.PCBS_Locked.setGeometry(QtCore.QRect(315, 260, 261, 192))
        self.PCBS_Locked.setObjectName("PCBS_Locked")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 10, 181, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 240, 151, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(320, 240, 141, 16))
        self.label_3.setObjectName("label_3")
        self.ChangeToWait = QtWidgets.QPushButton(self.centralwidget)
        self.ChangeToWait.setGeometry(QtCore.QRect(70, 460, 151, 23))
        self.ChangeToWait.setObjectName("ChangeToWait")
        self.ChangeToReady = QtWidgets.QPushButton(self.centralwidget)
        self.ChangeToReady.setGeometry(QtCore.QRect(400, 460, 75, 23))
        self.ChangeToReady.setObjectName("ChangeToReady")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(600, 290, 151, 16))
        self.label_4.setObjectName("label_4")
        self.PCB_Pid = QtWidgets.QSpinBox(self.centralwidget)
        self.PCB_Pid.setGeometry(QtCore.QRect(600, 130, 71, 22))
        self.PCB_Pid.setMinimum(1)
        self.PCB_Pid.setMaximum(999)
        self.PCB_Pid.setObjectName("PCB_Pid")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(600, 110, 131, 16))
        self.label_5.setObjectName("label_5")
        self.PCB_Level = QtWidgets.QSpinBox(self.centralwidget)
        self.PCB_Level.setGeometry(QtCore.QRect(600, 260, 71, 22))
        self.PCB_Level.setMinimum(1)
        self.PCB_Level.setMaximum(32)
        self.PCB_Level.setObjectName("PCB_Level")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(600, 240, 131, 16))
        self.label_6.setObjectName("label_6")
        self.PCB_Time = QtWidgets.QSpinBox(self.centralwidget)
        self.PCB_Time.setGeometry(QtCore.QRect(600, 190, 71, 22))
        self.PCB_Time.setMinimum(1)
        self.PCB_Time.setMaximum(9999)
        self.PCB_Time.setObjectName("PCB_Time")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(600, 170, 171, 16))
        self.label_7.setObjectName("label_7")
        self.PCBS_Runing = QtWidgets.QTableView(self.centralwidget)
        self.PCBS_Runing.setGeometry(QtCore.QRect(20, 30, 256, 191))
        self.PCBS_Runing.setObjectName("PCBS_Runing")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 10, 111, 16))
        self.label_8.setObjectName("label_8")
        self.PCB_Name = QtWidgets.QLineEdit(self.centralwidget)
        self.PCB_Name.setGeometry(QtCore.QRect(600, 70, 141, 20))
        self.PCB_Name.setObjectName("PCB_Name")
        self.EXIT = QtWidgets.QPushButton(self.centralwidget)
        self.EXIT.setGeometry(QtCore.QRect(600, 380, 111, 51))
        self.EXIT.setObjectName("EXIT")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ADDPCB.setText(_translate("MainWindow", "添加进程"))
        self.label.setText(_translate("MainWindow", "就绪队列，最大为5个进程："))
        self.label_2.setText(_translate("MainWindow", "后备队列，不限数量："))
        self.label_3.setText(_translate("MainWindow", "挂起队列，不限数量："))
        self.ChangeToWait.setText(_translate("MainWindow", "挂起(对后备进程无效)"))
        self.ChangeToReady.setText(_translate("MainWindow", "解挂"))
        self.label_4.setText(_translate("MainWindow", "PS:优先级越小优先权越高"))
        self.label_5.setText(_translate("MainWindow", "请输入进程PID:1--999"))
        self.label_6.setText(_translate("MainWindow", "请输入进程优先级:1--32"))
        self.label_7.setText(_translate("MainWindow", "请输入进程运行时间：1--9999"))
        self.label_8.setText(_translate("MainWindow", "运行中的进程，仅1："))
        self.PCB_Name.setPlaceholderText(_translate("MainWindow", "请输入进程名（可为空）"))
        self.EXIT.setText(_translate("MainWindow", "退出"))

    def setupFunction(self):
        self.EXIT.clicked.connect(self.Exit)
        self.ChangeToReady.clicked.connect(self.changetowaiting)
        self.ChangeToWait.clicked.connect(self.changetolocked)
        self.ADDPCB.clicked.connect(self.addPCB)
        self.setHeader(self.Ready_Model)
        self.setHeader(self.Runing_Model)
        self.setHeader(self.Waiting_Model)
        self.setHeader(self.Locked_Model)
        self.PCBS_Waiting.setModel(self.Waiting_Model)
        self.PCBS_Locked.setModel(self.Locked_Model)
        self.PCBS_Ready.setModel(self.Ready_Model)
        self.PCBS_Runing.setModel(self.Runing_Model)
        self.PCBS_Runing.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.PCBS_Runing.setSelectionMode(QAbstractItemView.SingleSelection)
        self.PCBS_Runing.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.PCBS_Ready.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.PCBS_Ready.setSelectionMode(QAbstractItemView.SingleSelection)
        self.PCBS_Ready.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.PCBS_Waiting.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.PCBS_Waiting.setSelectionMode(QAbstractItemView.SingleSelection)
        self.PCBS_Waiting.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.PCBS_Locked.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.PCBS_Locked.setSelectionMode(QAbstractItemView.SingleSelection)
        self.PCBS_Locked.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.the_thread = myThread()
        self.the_thread.sendmsg.connect(self.AllSchedule)
        self.the_thread.start()

    def Exit(self):
        QApplication.instance().quit()

    def setHeader(self, QStandardItemModels):
        QStandardItemModels.setHorizontalHeaderItem(0, QStandardItem("进程名"))
        QStandardItemModels.setHorizontalHeaderItem(1, QStandardItem("PID"))
        QStandardItemModels.setHorizontalHeaderItem(2, QStandardItem("所需时间"))
        QStandardItemModels.setHorizontalHeaderItem(3, QStandardItem("优先级"))
        QStandardItemModels.setHorizontalHeaderItem(4, QStandardItem("状态"))

    def addItem(self, MODEL1, MODEL2, TABLE):
        row = TABLE.currentIndex().row()
        NAME = MODEL1.item(row, 0).text()
        PID = MODEL1.item(row, 1).text()
        TIME = int(MODEL1.item(row, 2).text())
        LEVEL = int(MODEL1.item(row, 3).text())
        MODEL1.removeRow(row)
        Item_TIME = QStandardItem()
        Item_LEVEL = QStandardItem()
        Item_TIME.setData(TIME, 2)
        Item_LEVEL.setData(LEVEL, 2)
        countRow = MODEL2.rowCount()
        MODEL2.setItem(countRow, 0, QStandardItem(NAME))
        MODEL2.setItem(countRow, 1, QStandardItem(PID))
        MODEL2.setItem(countRow, 2, Item_TIME)
        MODEL2.setItem(countRow, 3, Item_LEVEL)
        if MODEL2 == self.Locked_Model:
            MODEL2.setItem(countRow, 4, QStandardItem("挂起中"))
        elif MODEL2 == self.Ready_Model:
            MODEL2.setItem(countRow, 4, QStandardItem("就绪中"))
        TABLE.clearSelection()

    def MOVE(self, MODEL1, MODEL2):
        countRow = MODEL2.rowCount()
        if MODEL1.rowCount() != 0:
            NAME = MODEL1.item(0, 0).text()
            PID = MODEL1.item(0, 1).text()
            TIME = int(MODEL1.item(0, 2).text())
            LEVEL = int(MODEL1.item(0, 3).text())
            Item_TIME = QStandardItem()
            Item_LEVEL = QStandardItem()
            Item_TIME.setData(TIME, 2)
            Item_LEVEL.setData(LEVEL, 2)
            MODEL1.removeRow(0)
            MODEL2.setItem(countRow, 0, QStandardItem(NAME))
            MODEL2.setItem(countRow, 1, QStandardItem(PID))
            MODEL2.setItem(countRow, 2, Item_TIME)
            MODEL2.setItem(countRow, 3, Item_LEVEL)
            if MODEL2 == self.Runing_Model:
                MODEL2.setItem(countRow, 4, QStandardItem("运行中"))
            elif MODEL2 == self.Ready_Model:
                MODEL2.setItem(countRow, 4, QStandardItem("就绪中"))

    def changetolocked(self):
        if len(self.PCBS_Runing.selectedIndexes()) != 0:
            self.addItem(self.Runing_Model, self.Locked_Model, self.PCBS_Runing)
        elif len(self.PCBS_Ready.selectedIndexes()) != 0:
            self.addItem(self.Ready_Model, self.Locked_Model, self.PCBS_Ready)

    def changetowaiting(self):
        if len(self.PCBS_Locked.selectedIndexes()) != 0:
            self.addItem(self.Locked_Model, self.Ready_Model, self.PCBS_Locked)

    def addPCB(self):
        NAME = self.PCB_Name.text()
        PID = self.PCB_Pid.text()
        TIME = int(self.PCB_Time.text())
        LEVEL = int(self.PCB_Level.text())
        if self.IDS.count(PID) == 0:
            row = self.Waiting_Model.rowCount()
            Item_TIME = QStandardItem()
            Item_LEVEL = QStandardItem()
            Item_TIME.setData(TIME, 2)
            Item_LEVEL.setData(LEVEL, 2)
            self.Waiting_Model.setItem(row, 0, QStandardItem(NAME))
            self.Waiting_Model.setItem(row, 1, QStandardItem(PID))
            self.Waiting_Model.setItem(row, 2, Item_TIME)
            self.Waiting_Model.setItem(row, 3, Item_LEVEL)
            self.Waiting_Model.setItem(row, 4, QStandardItem("等待中"))
            self.IDS.append(PID)
        else:
            QMessageBox.warning(MainWindow, "Error", "该PID已被使用", QMessageBox.Ok)

    def Schedule(self):
        self.Waiting_Model.sort(3)
        if self.Ready_Model.rowCount() < 5:
            self.MOVE(self.Waiting_Model, self.Ready_Model)
            self.Ready_Model.sort(3)
        if self.Runing_Model.rowCount() < 1:
            self.MOVE(self.Ready_Model, self.Runing_Model)
        while self.Ready_Model.rowCount() < 5:
            if self.Waiting_Model.rowCount() == 0:
                break
            self.MOVE(self.Waiting_Model, self.Ready_Model)
        self.Ready_Model.sort(3)

    def AllSchedule(self):
        self.Schedule()
        self.TimeChanging()

    def TimeChanging(self):
        if self.Runing_Model.rowCount() == 1:
            Time = int(self.Runing_Model.item(0, 2).text())
            Time -= 1
            if Time == 0:
                PID = self.Runing_Model.item(0, 1).text()
                self.Runing_Model.removeRow(0)
                self.IDS.remove(PID)
            else:
                Level = int(self.Runing_Model.item(0, 3).text())
                if Level != 1:
                    Level -= 1
                self.Runing_Model.item(0, 2).setData(Time, 2)
                self.Runing_Model.item(0, 3).setData(Level, 2)
        rows = self.Ready_Model.rowCount()
        if rows != 0:
            for num in range(rows):
                Level = int(self.Ready_Model.item(num, 3).text())
                if Level != 1:
                    Level -= 1
                self.Ready_Model.item(num, 3).setData(Level, 2)
        rows = self.Waiting_Model.rowCount()
        if rows != 0:
            for num in range(self.Waiting_Model.rowCount()):
                Level = int(self.Waiting_Model.item(num, 3).text())
                if Level != 1:
                    Level -= 1
                self.Waiting_Model.item(num, 3).setData(Level, 2)
        self.PCBS_Runing.clearSelection()
        self.PCBS_Locked.clearSelection()
        self.PCBS_Waiting.clearSelection()
        self.PCBS_Ready.clearSelection()


class myThread(QtCore.QThread):
    sendmsg = pyqtSignal()

    def __init__(self):
        super(myThread, self).__init__()

    def run(self):
        while True:
            time.sleep(5)
            self.sendmsg.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QMainWindow()  # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = Ui_MainWindow()  # ui是Ui_MainWindow()类的实例化对象
    MainWindow.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())
