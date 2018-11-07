# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Date_Time.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtWidgets import QApplication, QMessageBox


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        self.setupUi(MainWindow)
        self.setFunction()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 30, 761, 451))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 331, 361))
        self.groupBox.setObjectName("groupBox")
        self.calendar = QtWidgets.QCalendarWidget(self.groupBox)
        self.calendar.setGeometry(QtCore.QRect(40, 40, 271, 241))
        self.calendar.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.calendar.setGridVisible(False)
        self.calendar.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        self.calendar.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendar.setNavigationBarVisible(True)
        self.calendar.setDateEditEnabled(False)
        self.calendar.setObjectName("calendar")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(390, 20, 341, 361))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(80, 310, 160, 31))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.hourSP = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hourSP.sizePolicy().hasHeightForWidth())
        self.hourSP.setSizePolicy(sizePolicy)
        self.hourSP.setMaximumSize(QtCore.QSize(30, 20))
        self.hourSP.setObjectName("hourSP")
        self.gridLayout_2.addWidget(self.hourSP, 0, 0, 1, 1)
        self.minSP = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minSP.sizePolicy().hasHeightForWidth())
        self.minSP.setSizePolicy(sizePolicy)
        self.minSP.setMaximumSize(QtCore.QSize(30, 20))
        self.minSP.setObjectName("minSP")
        self.gridLayout_2.addWidget(self.minSP, 0, 1, 1, 1)
        self.secSP = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.secSP.sizePolicy().hasHeightForWidth())
        self.secSP.setSizePolicy(sizePolicy)
        self.secSP.setMaximumSize(QtCore.QSize(30, 20))
        self.secSP.setObjectName("secSP")
        self.gridLayout_2.addWidget(self.secSP, 0, 2, 1, 1)
        self.AMRBT = QtWidgets.QRadioButton(self.groupBox_2)
        self.AMRBT.setGeometry(QtCore.QRect(270, 310, 41, 16))
        self.AMRBT.setObjectName("AMRBT")
        self.PMRBT = QtWidgets.QRadioButton(self.groupBox_2)
        self.PMRBT.setGeometry(QtCore.QRect(270, 330, 41, 16))
        self.PMRBT.setObjectName("PMRBT")
        self.infoLabel = QtWidgets.QLabel(self.tab)
        self.infoLabel.setGeometry(QtCore.QRect(20, 400, 411, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.infoLabel.setFont(font)
        self.infoLabel.setObjectName("infoLabel")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.timeZoneCB = QtWidgets.QComboBox(self.tab_2)
        self.timeZoneCB.setGeometry(QtCore.QRect(250, 30, 300, 25))
        self.timeZoneCB.setMaxVisibleItems(11)
        self.timeZoneCB.setObjectName("timeZoneCB")
        self.timeZoneCB.addItem("")
        self.timeZoneCB.addItem("")
        self.timeZoneCB.addItem("")
        self.timeZoneCB.addItem("")
        self.timeZoneCB.addItem("")
        self.timeZoneCB.addItem("")
        self.timeZoneCB.addItem("")
        self.timeZoneCB.addItem("")
        self.timeZoneCB.addItem("")
        self.timeZoneCB.addItem("")
        self.timeZoneCB.addItem("")
        self.timeZoneCB.addItem("")
        self.timeZoneCB.addItem("")
        self.timeZoneCB.addItem("")
        self.timeZoneCB.addItem("")
        self.timeZoneCB.addItem("")
        self.timeZoneCB.addItem("")
        self.timeZoneCB.addItem("")
        self.timeZoneCB.addItem("")
        self.timeZoneCB.addItem("")
        self.timeZoneCB.addItem("")
        self.timeZoneCB.addItem("")
        self.timeZoneCB.addItem("")
        self.timeZoneCB.addItem("")
        self.adjustBT = QtWidgets.QCheckBox(self.tab_2)
        self.adjustBT.setGeometry(QtCore.QRect(210, 370, 16, 16))
        self.adjustBT.setText("")
        self.adjustBT.setCheckable(True)
        self.adjustBT.setChecked(False)
        self.adjustBT.setAutoRepeat(False)
        self.adjustBT.setAutoExclusive(False)
        self.adjustBT.setTristate(False)
        self.adjustBT.setObjectName("adjustBT")
        self.adjustLabel = QtWidgets.QLabel(self.tab_2)
        self.adjustLabel.setGeometry(QtCore.QRect(230, 370, 371, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.adjustLabel.setFont(font)
        self.adjustLabel.setObjectName("adjustLabel")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(460, 510, 321, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.CancelBT = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CancelBT.sizePolicy().hasHeightForWidth())
        self.CancelBT.setSizePolicy(sizePolicy)
        self.CancelBT.setMinimumSize(QtCore.QSize(80, 40))
        self.CancelBT.setMaximumSize(QtCore.QSize(80, 40))
        self.CancelBT.setObjectName("CancelBT")
        self.gridLayout.addWidget(self.CancelBT, 0, 1, 1, 1)
        self.okBT = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okBT.sizePolicy().hasHeightForWidth())
        self.okBT.setSizePolicy(sizePolicy)
        self.okBT.setMinimumSize(QtCore.QSize(80, 40))
        self.okBT.setMaximumSize(QtCore.QSize(80, 40))
        self.okBT.setObjectName("okBT")
        self.gridLayout.addWidget(self.okBT, 0, 0, 1, 1)
        self.ApplyBT = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ApplyBT.sizePolicy().hasHeightForWidth())
        self.ApplyBT.setSizePolicy(sizePolicy)
        self.ApplyBT.setMinimumSize(QtCore.QSize(80, 40))
        self.ApplyBT.setMaximumSize(QtCore.QSize(80, 40))
        self.ApplyBT.setObjectName("ApplyBT")
        self.gridLayout.addWidget(self.ApplyBT, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Date/Time"))
        self.groupBox.setTitle(_translate("MainWindow", "&Date"))
        self.groupBox_2.setTitle(_translate("MainWindow", "&Time"))
        self.AMRBT.setText(_translate("MainWindow", "AM"))
        self.PMRBT.setText(_translate("MainWindow", "PM"))
        self.infoLabel.setText(_translate("MainWindow", "Current Time Zone: "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Date && Time"))
        self.timeZoneCB.setCurrentText(_translate("MainWindow", "IDL 12:00"))
        self.timeZoneCB.setItemText(0, _translate("MainWindow", "AESST +11:00"))
        self.timeZoneCB.setItemText(1, _translate("MainWindow", "EAST +10:00"))
        self.timeZoneCB.setItemText(2, _translate("MainWindow", "JST +09:00"))
        self.timeZoneCB.setItemText(3, _translate("MainWindow", "CCT +08:00"))
        self.timeZoneCB.setItemText(4, _translate("MainWindow", "CXT +07:00"))
        self.timeZoneCB.setItemText(5, _translate("MainWindow", "ALMT +06:00"))
        self.timeZoneCB.setItemText(6, _translate("MainWindow", "MVT +05:00"))
        self.timeZoneCB.setItemText(7, _translate("MainWindow", "EAST +04:00"))
        self.timeZoneCB.setItemText(8, _translate("MainWindow", "EAT +03:00"))
        self.timeZoneCB.setItemText(9, _translate("MainWindow", "EET +02:00"))
        self.timeZoneCB.setItemText(10, _translate("MainWindow", "DNT +01:00"))
        self.timeZoneCB.setItemText(11, _translate("MainWindow", "GMT 0:00"))
        self.timeZoneCB.setItemText(12, _translate("MainWindow", "WAT -01:00"))
        self.timeZoneCB.setItemText(13, _translate("MainWindow", "FNT -02:00"))
        self.timeZoneCB.setItemText(14, _translate("MainWindow", "ADT -03:00"))
        self.timeZoneCB.setItemText(15, _translate("MainWindow", "AST -04:00"))
        self.timeZoneCB.setItemText(16, _translate("MainWindow", "EST -05:00"))
        self.timeZoneCB.setItemText(17, _translate("MainWindow", "CST -06:00"))
        self.timeZoneCB.setItemText(18, _translate("MainWindow", "MST -07:00"))
        self.timeZoneCB.setItemText(19, _translate("MainWindow", "PST -08:00"))
        self.timeZoneCB.setItemText(20, _translate("MainWindow", "AKST -09:00"))
        self.timeZoneCB.setItemText(21, _translate("MainWindow", "HST -10:00"))
        self.timeZoneCB.setItemText(22, _translate("MainWindow", "NT -11:00"))
        self.timeZoneCB.setItemText(23, _translate("MainWindow", "IDL 12:00"))
        self.adjustLabel.setText(_translate("MainWindow", "Automatically adjust clock for daylight saving changes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Time Zone"))
        self.CancelBT.setText(_translate("MainWindow", "Cancel"))
        self.okBT.setText(_translate("MainWindow", "OK"))
        self.ApplyBT.setText(_translate("MainWindow", "Apply"))

    def setFunction(self):

        self.setGroup()
        self.setTimeZone()
        pass

    def setGroup(self):
        self.hourSP.setMinimum(-1)
        self.minSP.setMinimum(-1)
        self.secSP.setMinimum(-1)
        self.hourSP.valueChanged.connect(self.changeTime)
        self.minSP.valueChanged.connect(self.changeTime)
        self.secSP.valueChanged.connect(self.changeTime)
        self.AMRBT.setChecked(True)
        self.adjustBT.setEnabled(False)
        self.adjustLabel.setEnabled(False)
        self.okBT.clicked.connect(lambda: self.showMsg(1))
        self.CancelBT.clicked.connect(lambda: self.showMsg(2))
        self.ApplyBT.clicked.connect(lambda: self.showMsg(3))

    def showMsg(self, n):
        date = self.calendar.selectedDate()
        time = str(date.toPyDate()).split("-")
        if self.AMRBT.isChecked():
            hour = self.hourSP.text()
        else:
            hour = (int(self.hourSP.text()) + 12) % 24
        if self.adjustBT.isChecked():
            autoDl = "True"
        else:
            autoDl = "False"
        if n == 1:
            str1 = "OK...\n"
            str3 = "(Time saved)"
        elif n == 2:
            str1 = "Cancelled..."
            str3 = "(Time not saved)"
        else:
            str1 = "Apply..."
            str3 = "Time saved"
            self.adjustBT.setEnabled(False)
            self.adjustLabel.setEnabled(False)
        str2 = "====================\n" \
               "Year = {0}\n" \
               "Month = {1}\n" \
               "Day = {2}\n" \
               "Hour = {3}\n" \
               "Minute = {4}\n" \
               "Second = {5}\n" \
               "TimeZone = {6}\n" \
               "Auto Daylight = {7}\n" \
               "===================\n".format(time[0], time[1], time[2], hour, self.minSP.text(),
                                              self.secSP.text(), self.timeZoneCB.currentText(), autoDl)

        QMessageBox.about(MainWindow, "Date_and_Time", str1 + str2 + str3)
        if n == 1 or n == 2:
            MainWindow.close()
        pass

    def changeTime(self):

        if self.secSP.value() == 60:
            self.secSP.setValue(0)
            self.minSP.setValue(self.minSP.value() + 1)
        if self.secSP.value() == -1:
            self.secSP.setValue(59)
            self.minSP.setValue(self.minSP.value() - 1)
        if self.minSP.value() == 60:
            self.minSP.setValue(0)
            self.hourSP.setValue(self.hourSP.value() + 1)
        if self.minSP.value() == -1:
            self.minSP.setValue(59)
            self.hourSP.setValue(self.hourSP.value() - 1)
        if self.hourSP.value() == 12 or self.hourSP.value() == -1:
            if self.hourSP.value() == 12:
                self.hourSP.setValue(0)
            else:
                self.hourSP.setValue(11)
            if self.AMRBT.isChecked():
                self.AMRBT.setChecked(False)
                self.PMRBT.setChecked(True)
            else:
                self.AMRBT.setChecked(True)
                self.PMRBT.setChecked(False)

    def creatBt(self, i, x):
        y = 110
        bl = btlabel(self.tab_2)
        bl.setPixmap(QPixmap("img/timezone ({0}).gif".format(i + 1)))
        bl.setGeometry(QtCore.QRect(x, y, 15, 184))
        bl.clicked.connect(lambda: self.changeTimeZone(i))
        return bl

    def setTimeZone(self):
        x = 230
        self.btList = []
        for i in range(24):
            self.btList.append(self.creatBt(i, x))
            x += 15
        self.timeZoneCB.currentIndexChanged.connect(self.changeMap)

    def changeMap(self):
        self.changeTimeZone(self.timeZoneCB.currentIndex())

    def changeTimeZone(self, n):
        x = 230 + 11 * 15
        y = 110
        for i in range(n, 24):
            if x + (i - n) * 15 < 590:
                ex = x + (i - n) * 15
            else:
                ex = x + (i - n) * 15
                ex = ex - 360
            self.btList[i].setGeometry(QtCore.QRect(ex, y, 15, 184))
        for i in range(n):
            if x + (i - n) * 15 >= 230:
                ex = x + (i - n) * 15
            else:
                ex = x + (i - n) * 15
                ex = 360 + ex

            self.btList[i].setGeometry(QtCore.QRect(ex, y, 15, 184))
        self.timeZoneCB.setCurrentIndex(n)
        self.infoLabel.setText("Current Time Zone: {0}".format(self.timeZoneCB.currentText()))
        self.adjustBT.setEnabled(True)
        self.adjustLabel.setEnabled(True)
    #调整时区图位置

class btlabel(QtWidgets.QLabel):
    clicked = pyqtSignal()

    def __init__(self, parnet=None):
        super(btlabel, self).__init__(parnet)

    def mousePressEvent(self, ev: QtGui.QMouseEvent):
        self.clicked.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QMainWindow()  # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = Ui_MainWindow(MainWindow)  # ui是Ui_MainWindow()类的实例化对象
    MainWindow.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出QApplication
