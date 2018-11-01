import time

from PyQt5.QtCore import QThread, pyqtSignal


class timePass(QThread):
    msg = pyqtSignal()

    def __init__(self):
        super(timePass, self).__init__()

    def run(self):
        while True:
            time.sleep(1)
            self.msg.emit()
