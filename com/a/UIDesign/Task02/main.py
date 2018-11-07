# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox
import sys

class Ui_MainWindow(object):
    def __init__(self):
        self.setupUi(MainWindow)
        self.setupFunction()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 444)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_0 = QtWidgets.QLabel(self.centralwidget)
        self.label_0.setGeometry(QtCore.QRect(30, 20, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_0.setFont(font)
        self.label_0.setObjectName("label_0")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 75, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(30, 50, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 125, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 150, 341, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 175, 271, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 200, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 300, 91, 16))
        self.label.setObjectName("label")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 350, 131, 16))
        self.label_8.setObjectName("label_8")
        self.Number = QtWidgets.QLineEdit(self.centralwidget)
        self.Number.setGeometry(QtCore.QRect(170, 300, 113, 20))
        self.Number.setObjectName("Number")
        self.mystring = QtWidgets.QLineEdit(self.centralwidget)
        self.mystring.setGeometry(QtCore.QRect(170, 350, 113, 20))
        self.mystring.setObjectName("mystring")
        self.Display = QtWidgets.QPushButton(self.centralwidget)
        self.Display.setGeometry(QtCore.QRect(300, 300, 75, 23))
        self.Display.setObjectName("Display")
        self.Search = QtWidgets.QPushButton(self.centralwidget)
        self.Search.setGeometry(QtCore.QRect(300, 350, 75, 23))
        self.Search.setObjectName("Search")
        self.First = QtWidgets.QLabel(self.centralwidget)
        self.First.setGeometry(QtCore.QRect(420, 300, 201, 16))
        self.First.setText("")
        self.First.setObjectName("First")
        self.Last = QtWidgets.QLabel(self.centralwidget)
        self.Last.setGeometry(QtCore.QRect(420, 350, 201, 16))
        self.Last.setText("")
        self.Last.setObjectName("Last")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(420, 40, 361, 231))
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit.setObjectName("textEdit")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(420, 280, 54, 12))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(420, 20, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.Exit = QtWidgets.QPushButton(self.centralwidget)
        self.Exit.setGeometry(QtCore.QRect(690, 390, 91, 31))
        self.Exit.setObjectName("Exit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UAR Components"))
        self.label_0.setText(_translate("MainWindow", "UAR components names:"))
        self.label_2.setText(_translate("MainWindow", "2.Succinct Description of the Usability Aspect"))
        self.label_3.setText(_translate("MainWindow", "3.Evidence for the Aspect"))
        self.label_1.setText(_translate("MainWindow", "1.UAR Identifier"))
        self.label_4.setText(_translate("MainWindow", "4.Explanation of the Aspect"))
        self.label_5.setText(_translate("MainWindow", "5.Severity of the Problem or Benefit of the Good Feature"))
        self.label_6.setText(_translate("MainWindow", "6.Possible Solutions and Potential Trade-offs"))
        self.label_7.setText(_translate("MainWindow", "7.Relationship to Other Usability Aspects"))
        self.label.setText(_translate("MainWindow", "Enter a number:"))
        self.label_8.setText(_translate("MainWindow", "Enter a search string:"))
        self.Display.setText(_translate("MainWindow", "Display"))
        self.Search.setText(_translate("MainWindow", "Search"))
        self.Exit.setText(_translate("MainWindow", "Exit"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                       "p, li { white-space: pre-wrap; }\n"
                                                       "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                       "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "Found at:"))
        self.label_10.setText(_translate("MainWindow", "UAR component description:"))

    def setupFunction(self):#将各按键或信号同方法关联
        self.Number.setFocus()
        self.Display.clicked.connect(self.display)
        self.Search.clicked.connect(self.search)
        self.Number.textChanged.connect(self.Num_Change)
        self.mystring.textChanged.connect(self.Mystr_Chang)
        self.Exit.clicked.connect(QApplication.instance().quit)

    def display(self):
        number = self.Number.text()
        if number=='1':
            self.textEdit.setText("This should be a unique identifier for the purposes of filing. If more than one person is working on the project or more than one analysis technique is being used, this identifier could contain letters and numbers. For example, if Chris Smith and Jan Koo are both doing an analysis, the identifier might be CS1 or JK75. If both a heuristic evaluation and a think-aloud usability study were used, the identifiers might be HE6 or TA89. Follow the unique identifier with the word 'Problem,' if the report pertains to a usability problem of the interface, or the words 'Good Feature,' if it describes an aspect of the interface you feel should be preserved in any redesign.")
        elif number=='2':
            self.textEdit.setText("This description will be used as the 'name' of this UAR when you talk about its relation to other UARs. Make the name as short as possible (about three to five words) but still descriptive and distinguishable from other aspects of the system. If this UAR is about a problem (as opposed to a good feature), make sure you have a name that describes the problem, rather than a solution.")
        elif number=='3':
            self.textEdit.setText("This is the objective supporting material that justifies your identifying the aspect as worthy of report. This section needs to contain enough information for a reader of this UAR to understand what triggered the report. For an HE report, for instance, this could be an image of a cluttered screen and the heuristic about aesthetics and minimalist design. In a think-aloud study this is usually what was on the screen (a screen shot or description), what the user did (keystrokes, mouse movements), what the system did in response to any user actions, and what the user said. You need to include enough pertinent information about the identification of an aspect for the reader to understand what the analyst was thinking when the aspect was identified (for HE) or what the user was trying to do when the aspect either hindered or facilitated his or her progress.")
        elif number=='4':
            self.textEdit.setText("This is your interpretation of the evidence. That is, for a think-aloud usability test, why you think what happened happened, or, for an HE, why you think the aspect was designed the way it was. You need to provide enough content in this explanation for the reader to understand the problem-even if they do not know the system or domain as well as you do.")
        elif number=='5':
            self.textEdit.setText("This is your reasoning about how important it is to either fix this problem or preserve this good feature. This includes how frequently the users will experience this aspect, whether they are likely to learn how it works, whether it will affect new users, casual users, experienced users, etc.")
        elif number=='6':
            self.textEdit.setText("If this aspect is a problem (as opposed to a good feature to be preserved in the next version of the software), this is the place to propose a solution. It is not necessary to have a solution as soon as you identify a problem-you might find after analyzing the whole interface that many problems are related and can all be fixed by making a single broad change instead of making several small changes. However, if you do propose a possible solution, report any potential design trade-offs that you see")
        elif number=='7':
            self.textEdit.setText("It is often the case that UARs are related to each other. This is where you record which UARs this one is related to and a statement about how it is related. Make sure that all the related UARs point to each other. It is a common mistake to enter the pointer into a newly created UAR, but neglect to go back to the previous ones that it relates to and update their UARs")
        else:
            QMessageBox(QMessageBox.Warning, "Search String", "Please  enter values between 1 and 7", QMessageBox.Ok).exec()

    def search(self):
        The_str = self.mystring.text().lower()
        The_text = self.textEdit.toPlainText().lower()
        if len(The_text)==0:
           QMB=QMessageBox(QMessageBox.Warning, "Search String", "Please select text",
                        QMessageBox.Ok)
           QMB.button(QMessageBox.Ok).setText('确定')
           QMB.exec()
           self.Number.setFocus()
        elif len(The_str)==0:
            QMB=QMessageBox(QMessageBox.Warning, "Search String", "Please enter a search string",
                        QMessageBox.Ok)
            QMB.button(QMessageBox.Ok).setText('确定')
            QMB.exec()
            self.mystring.setFocus()
        else:
            self.find(The_str,The_text)

    def find(self,str1,str2):
        times=str2.count(str1)
        if times!=0:
            Loca=str2.find(str1)+1
            self.First.setText('Occurrence 1: Position: %d'%Loca)
            if times>1:
                Loca=str2.rfind(str1)+1
                self.Last.setText('Occurrence %d: Position: %d' %(times,Loca))
            QMB = QMessageBox(QMessageBox.Warning, "Search String", "The number of occurences of '%s' is:%d\nSearch same text?"%(str1,times),
                        QMessageBox.Yes|QMessageBox.No)
            QMB.button(QMessageBox.Yes).setText('是(Y)')
            QMB.button(QMessageBox.No).setText('否(N)')
            reply = QMB.exec()
            if reply==QMessageBox.Yes:
                self.The_Yes()
            else:
                self.The_No()
        else:
            QMB = QMessageBox(QMessageBox.Warning, "Search String",
                                "String '%s' not found\nSearch same text again?" %str1,
                                QMessageBox.Yes | QMessageBox.No)
            QMB.button(QMessageBox.Yes).setText('是(Y)')
            QMB.button(QMessageBox.No).setText('否(N)')
            reply = QMB.exec()
            if reply == QMessageBox.Yes:
                self.The_Yes()
            else:
                self.The_No()

    def The_Yes(self):
        self.mystring.setFocus()
        self.mystring.selectAll()

    def The_No(self):
        self.First.clear()
        self.Last.clear()
        self.Number.clear()
        self.mystring.clear()
        self.textEdit.clear()
        self.Number.setFocus()

    def Num_Change(self):#对dispaly对应的文本框修改时
        self.First.clear()
        self.Last.clear()
        self.mystring.clear()
        self.textEdit.clear()

    def Mystr_Chang(self):#对search对应的文本框修改时
        self.First.clear()
        self.Last.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QMainWindow()    # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = Ui_MainWindow()                    # ui是Ui_MainWindow()类的实例化对象
    MainWindow.show()                       # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())                   # 使用exit()或者点击关闭按钮退出QApplication

