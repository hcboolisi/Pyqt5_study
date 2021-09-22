import sys

from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout


class Span(QWidget):
    def __init__(self):
        super(Span, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('sort排序')
        self.resize(450, 400)

        self.tablewidget = QTableWidget(4, 3)
        self.tablewidget.setHorizontalHeaderLabels(['姓名', '年级', '分数'])

        self.tablewidget.setItem(0, 0, QTableWidgetItem('关羽'))
        self.tablewidget.setItem(0, 1, QTableWidgetItem('一年级'))
        self.tablewidget.setItem(0, 2, QTableWidgetItem('80'))

        # 合并单元格,前两个参数表示从哪个cell开始合并，后面两个参数表示要合并几行，几列，这里是合并3行，1列
        self.tablewidget.setSpan(0, 0, 3, 1)
        # self.tablewidget.clearSpans()  # 清除，还原合并的单元格

        # 改变行和列的高度和宽度
        self.tablewidget.setRowHeight(3, 100)
        self.tablewidget.setColumnWidth(2, 100)

        vbox = QVBoxLayout(self)
        vbox.addWidget(self.tablewidget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Span()
    w.show()
    sys.exit(app.exec())