import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from com.a.OperateSystem.UI.SystemScheduling_UI import Ui_MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())