def setFunction(self):
    self.setGroup()
    self.setTimeZone()
    pass


def setGroup(self):
    self.hourSP.valueChanged.connect(self.changeTime)
    self.minSP.valueChanged.connect(self.changeTime)
    self.secSP.valueChanged.connect(self.changeTime)


def changeTime(self):
    if self.secSP.value() == 60:
        self.secSP.setValue(0)
        self.minSP.setValue(self.minSP.value() + 1)
    if self.minSP.value() == 60:
        self.minSP.setValue(0)
        self.hourSP.setValue(self.hourSP.value() + 1)
    if self.hourSP.value() == 12:
        self.hourSP.setValue(0)
        if self.AMRBT.isChecked():
            self.AMRBT.setChecked(False)
            self.PMRBT.setChecked(True)
        else:
            self.AMRBT.setChecked(True)
            self.PMRBT.setChecked(False)


def setTimeZone(self):
    pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


    def __init__(self, MainWindow):
        self.setupUi(MainWindow)
        self.setFunction()
