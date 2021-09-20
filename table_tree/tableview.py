import sys

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTableView, QApplication, QVBoxLayout, QAbstractItemView


class TableView(QWidget):
    def __init__(self):
        super(TableView, self).__init__()
        self.setWindowTitle('QTableView表格视图')
        self.resize(400, 300)
        vbox = QVBoxLayout()

        # TableView使用的是MVC模式来显示数据，M即mode，V即view，C即control

        # 设置mode，4行3列，和每列项目名称
        self.mode = QStandardItemModel(4, 3)
        self.mode.setHorizontalHeaderLabels(['编号', '姓名', '性别'])

        # 创建表视图，TableWidget 不用设置mode，直接在TableWidget上就可以设置行列数和每列项目名称
        self.tabeleview = QTableView()
        # 设置表视图的模式为mode
        self.tabeleview.setModel(self.mode)

        vbox.addWidget(self.tabeleview)
        self.setLayout(vbox)

        # 添加数据,在实际应用中，一般都是用For循环来添加数据。
        item_11 = QStandardItem('0001')
        item_11.setTextAlignment(Qt.AlignCenter)
        item_12 = QStandardItem('关羽')
        item_13 = QStandardItem('男')
        self.mode.setItem(0, 0, item_11)
        self.mode.setItem(0, 1, item_12)
        self.mode.setItem(0, 2, item_13)

        item_21 = QStandardItem('0002')
        item_22 = QStandardItem('张飞')
        item_23 = QStandardItem('男')
        self.mode.setItem(1, 0, item_21)
        self.mode.setItem(1, 1, item_22)
        self.mode.setItem(1, 2, item_23)

        # self.tabeleview.setEditTriggers(QAbstractItemView.NoEditTriggers)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = TableView()
    w.show()
    sys.exit(app.exec_())