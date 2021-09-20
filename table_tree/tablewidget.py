import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QApplication, \
                             QTableWidgetItem, QAbstractItemView


class TableWidget(QMainWindow):
    def __init__(self):
        super(TableWidget, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('TableWidget表格扩展控件')
        self.resize(500, 300)

        self.tablewidget = QTableWidget()
        self.tablewidget.setRowCount(4)
        self.tablewidget.setColumnCount(4)
        self.tablewidget.setHorizontalHeaderLabels(['编号', '姓名', '年龄', '性别'])

        item_1 = QTableWidgetItem('0001')
        # 设置表格内容对齐方式为居中对齐
        item_1.setTextAlignment(Qt.AlignCenter)
        self.tablewidget.setItem(0, 0, item_1)

        self.tablewidget.setItem(0, 1, QTableWidgetItem('关羽'))
        self.tablewidget.setItem(0, 2, QTableWidgetItem('23'))
        self.tablewidget.setItem(0, 3, QTableWidgetItem('男'))

        # 禁止编辑
        self.tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 整行选择
        self.tablewidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 根据表格内容调整单元格大小
        self.tablewidget.resizeRowsToContents()
        self.tablewidget.resizeColumnsToContents()

        # 设置表头项目和右侧编号隐藏
        # self.tablewidget.horizontalHeader().setVisible(False)
        # self.tablewidget.verticalHeader().setVisible(False)

        # 设置左侧行数名称
        self.tablewidget.setVerticalHeaderLabels(['a', 'b', 'c', 'd'])

        # 设置是否显示表格网格线
        self.tablewidget.setShowGrid(False)

        self.setCentralWidget(self.tablewidget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = TableWidget()
    w.show()
    sys.exit(app.exec_())