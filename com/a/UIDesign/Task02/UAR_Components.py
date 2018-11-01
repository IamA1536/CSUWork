# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UAR_Components.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox

str = []

str.append(
    "This should be a unique identifier for the purposes of filing. If more than one person is working on the project or more than one analysis technique is being used, this identifier could contain letters and numbers. For example, if Chris Smith and Jan Koo are both doing an analysis, the identifier might be CS1 or JK75. If both a heuristic evaluation and a think-aloud usability study were used, the identifiers might be HE6 or TA89. Follow the unique identifier with the word 'Problem,' if the report pertains to a usability problem of the interface, or the words 'Good Feature,' if it describes an aspect of the interface you feel should be preserved in any redesign.")
str.append(
    "This description will be used as the 'name' of this UAR when you talk about its relation to other UARs. Make the name as short as possible (about three to five words) but still descriptive and distinguishable from other aspects of the system. If this UAR is about a problem (as opposed to a good feature), make sure you have a name that describes the problem, rather than a solution.")
str.append(
    "This is the objective supporting material that justifies your identifying the aspect as worthy of report. This section needs to contain enough information for a reader of this UAR to understand what triggered the report. For an HE report, for instance, this could be an image of a cluttered screen and the heuristic about aesthetics and minimalist design. In a think-aloud study this is usually what was on the screen (a screen shot or description), what the user did (keystrokes, mouse movements), what the system did in response to any user actions, and what the user said. You need to include enough pertinent information about the identification of an aspect for the reader to understand what the analyst was thinking when the aspect was identified (for HE) or what the user was trying to do when the aspect either hindered or facilitated his or her progress.")
str.append(
    "This is your interpretation of the evidence. That is, for a think-aloud usability test, why you think what happened happened, or, for an HE, why you think the aspect was designed the way it was. You need to provide enough content in this explanation for the reader to understand the problem-even if they do not know the system or domain as well as you do.")
str.append(
    "This is your reasoning about how important it is to either fix this problem or preserve this good feature. This includes how frequently the users will experience this aspect, whether they are likely to learn how it works, whether it will affect new users, casual users, experienced users, etc.")
str.append(
    "If this aspect is a problem (as opposed to a good feature to be preserved in the next version of the software), this is the place to propose a solution. It is not necessary to have a solution as soon as you identify a problem-you might find after analyzing the whole interface that many problems are related and can all be fixed by making a single broad change instead of making several small changes. However, if you do propose a possible solution, report any potential design trade-offs that you see")
str.append(
    "It is often the case that UARs are related to each other. This is where you record which UARs this one is related to and a statement about how it is related. Make sure that all the related UARs point to each other. It is a common mistake to enter the pointer into a newly created UAR, but neglect to go back to the previous ones that it relates to and update their UARs.")


class Ui_MainWindow(object):
    def __init__(self):
        self.setupUi(MainWindow)

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(870, 470)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 341, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(440, 10, 401, 361))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_2.addWidget(self.label_15)
        self.DeEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_2)
        self.DeEdit.setObjectName("DeEdit")
        self.verticalLayout_2.addWidget(self.DeEdit)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.FristFoundLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.FristFoundLabel.setText("")
        self.FristFoundLabel.setObjectName("FristFoundLabel")
        self.verticalLayout_2.addWidget(self.FristFoundLabel)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.verticalLayout_2.addWidget(self.label_13)
        self.LastFoundLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.LastFoundLabel.setText("")
        self.LastFoundLabel.setObjectName("LastFoundLabel")
        self.verticalLayout_2.addWidget(self.LastFoundLabel)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.verticalLayout_2.addWidget(self.label_14)
        self.ExitBt = QtWidgets.QPushButton(self.centralwidget)
        self.ExitBt.setGeometry(QtCore.QRect(770, 430, 75, 25))
        self.ExitBt.setObjectName("ExitBt")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 310, 381, 91))
        self.widget.setObjectName("widget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.widget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 10, 371, 74))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)
        self.SreachBt = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.SreachBt.setObjectName("SreachBt")
        self.gridLayout.addWidget(self.SreachBt, 1, 2, 1, 1)

        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)
        self.NameEt = QtWidgets.QTextEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NameEt.sizePolicy().hasHeightForWidth())
        self.NameEt.setSizePolicy(sizePolicy)
        self.NameEt.setMinimumSize(QtCore.QSize(130, 25))
        self.NameEt.setMaximumSize(QtCore.QSize(130, 25))
        self.NameEt.setObjectName("NameEt")
        self.gridLayout.addWidget(self.NameEt, 0, 1, 1, 1)
        self.DisplayBt = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DisplayBt.sizePolicy().hasHeightForWidth())
        self.DisplayBt.setSizePolicy(sizePolicy)
        self.DisplayBt.setObjectName("DisplayBt")

        self.gridLayout.addWidget(self.DisplayBt, 0, 2, 1, 1)

        self.SreachEt = QtWidgets.QTextEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SreachEt.sizePolicy().hasHeightForWidth())
        self.SreachEt.setSizePolicy(sizePolicy)
        self.SreachEt.setMinimumSize(QtCore.QSize(130, 25))
        self.SreachEt.setMaximumSize(QtCore.QSize(130, 25))
        self.SreachEt.setObjectName("SreachEt")
        self.gridLayout.addWidget(self.SreachEt, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.NameEt.setFocus()
        self.retranslateUi(MainWindow)
        self.ExitBt.clicked.connect(MainWindow.close)
        self.SreachBt.clicked.connect(self.sreach)
        self.DisplayBt.clicked.connect(self.display)
        self.changName = self.NameEt.document()
        self.changName.contentsChanged.connect(self.ClearDetail)
        self.changSreach = self.SreachEt.document()
        self.changSreach.contentsChanged.connect(self.FoundDetail)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UAR Components"))
        self.label.setText(_translate("MainWindow", "UAR Components names:"))
        self.label_2.setText(_translate("MainWindow", "1. UAR Identifier"))
        self.label_3.setText(_translate("MainWindow", "2. Succinct Description of the Usability Aspect"))
        self.label_4.setText(_translate("MainWindow", "3. Evidence for the Aspect"))
        self.label_5.setText(_translate("MainWindow", "4. Explanation of the Aspect"))
        self.label_6.setText(_translate("MainWindow", "5. Severity of the Problem or Benefit of the Good Feature"))
        self.label_7.setText(_translate("MainWindow", "6. Possible Solutions and Potential Trade-offs"))
        self.label_8.setText(_translate("MainWindow", "7. Relationship to Other Usability Aspects"))
        self.label_15.setText(_translate("MainWindow", "UAR Components description:"))
        self.label_12.setText(_translate("MainWindow", "Found at:"))
        self.ExitBt.setText(_translate("MainWindow", "Exit"))
        self.label_9.setText(_translate("MainWindow", "Enter a number:"))
        self.SreachBt.setText(_translate("MainWindow", "Search"))
        self.label_10.setText(_translate("MainWindow", "Enter a search string:"))
        self.DisplayBt.setText(_translate("MainWindow", "Display"))

    def ClearDetail(self):
        self.SreachEt.setPlainText("")
        self.DeEdit.setPlainText("")
        self.FristFoundLabel.setText("")
        self.LastFoundLabel.setText("")

    def FoundDetail(self):
        self.FristFoundLabel.setText("")
        self.LastFoundLabel.setText("")

    def display(self):

        num = int(self.NameEt.toPlainText())
        if num > 0 and num < 8:
            self.DeEdit.setPlainText(str[num - 1])
        else:
            Msg = QMessageBox(QMessageBox.Warning, "Search String", "Please enter values between 1 and 7")
            Msg.setWindowFlag(QtCore.Qt.WindowCloseButtonHint)
            Msg.exec()

    def sreach(self):
        str = self.SreachEt.toPlainText()
        if str == "":
            Msg = QMessageBox(QMessageBox.Warning, "Search String", "Please select text")
            Msg.setWindowFlag(QtCore.Qt.WindowCloseButtonHint)
            Msg.exec()
        else:
            str = str.lower()
            detext = self.DeEdit.toPlainText()
            detext = detext.lower()

            fristPos = detext.find(str) + 1
            lastPos = detext.rfind(str) + 1
            totalNum = detext.count(str)
            if totalNum != 0:
                self.FristFoundLabel.setText("Occurences 1: Position: {0}".format(fristPos))
                if totalNum != 1:
                    self.LastFoundLabel.setText("Occurences {0}: Position: {1}".format(totalNum, lastPos))
                str = "The number of occurences of " + str + "is: {0} \n Sreach same text?".format(totalNum)
                cbox = QMessageBox(QMessageBox.Information, "Search String", str, QMessageBox.NoButton)
                cbox.addButton("是(&Y)", QMessageBox.AcceptRole)
                IsNo = cbox.addButton("否(&N)", QMessageBox.RejectRole)


            else:
                str = "String {0} not found \n Search same text again?".format(str)
                cbox = QMessageBox(QMessageBox.Information, "Search String", str, QMessageBox.NoButton)
                cbox.addButton("确认", QMessageBox.YesRole)
                self.NameEt.setFocus()

            cbox.exec()
            if totalNum != 0:
                if cbox.clickedButton() == IsNo:
                    self.SreachEt.setPlainText("")
                    self.DeEdit.setPlainText("")
                    self.NameEt.setPlainText("")
                    self.FristFoundLabel.setText("")
                    self.LastFoundLabel.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QMainWindow()  # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = Ui_MainWindow()  # ui是Ui_MainWindow()类的实例化对象
    MainWindow.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出QApplication
