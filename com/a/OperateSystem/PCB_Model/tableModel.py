from PyQt5.QtGui import QStandardItem
import logging

from PyQt5.QtWidgets import QHeaderView


class tvmodel:
    def __init__(self, tableView, Model):
        '''表格初始化'''
        try:
            self.HeaderList = ["PID", "RunTime", "Status"]

            '表格初始化'
            self.DataModel = Model
            self.DataModel.setHorizontalHeaderLabels(self.HeaderList)  #

            self.tableView = tableView
            self.tableView.setModel(self.DataModel)
            # 下面代码让表格100填满窗口
            self.tableView.horizontalHeader().setStretchLastSection(True)
            self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            return True
        except Exception as e:
            logging(e)

        def Model_setItem(self, row, column, data):
            '''表格添加数据：第row行，column列数据更改为data'''
            self.DataModel.setItem(row, column, QStandardItem(data))
