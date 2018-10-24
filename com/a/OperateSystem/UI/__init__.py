def setFunction(self):
    self.acceptBt.clicked.connect(self.accept)
    self.ableTV.setEditTriggers(QAbstractItemView.NoEditTriggers)
    self.ableTV.setSelectionBehavior(QAbstractItemView.SelectRows)


def accept(self):
    if self.lineEdit.text() == "":
        QMessageBox(QMessageBox.Warning, "Error", "Please input the ID").exec()
    elif self.pTimetextEdit.toPlainText() == "":
        QMessageBox(QMessageBox.Warning, "Error", "Please input the time").exec()
    else:
        # if pcount == 4:
        QMessageBox(QMessageBox.Warning, "Error", "Ready is full!").exec()
        # else:

