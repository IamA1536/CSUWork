import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from com.a.OperateSystem.UI.SystemScheduling_UI import Ui_MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QMainWindow()  # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = Ui_MainWindow(MainWindow)  # ui是Ui_MainWindow()类的实例化对象
    MainWindow.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出QApplication
