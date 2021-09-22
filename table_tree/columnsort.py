import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QPushButton, \
    QVBoxLayout, QApplication, QHBoxLayout, QComboBox


class ColumnSort(QWidget):
    def __init__(self):
        super(ColumnSort, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('sort排序')
        self.resize(450, 400)

        self.tablewidget = QTableWidget(4, 3)
        self.tablewidget.setHorizontalHeaderLabels(['姓名', '年级', '分数'])

        self.tablewidget.setItem(0, 0, QTableWidgetItem('关羽'))
        self.tablewidget.setItem(0, 1, QTableWidgetItem('一年级'))
        self.tablewidget.setItem(0, 2, QTableWidgetItem('80'))

        self.tablewidget.setItem(1, 0, QTableWidgetItem('张飞'))
        self.tablewidget.setItem(1, 1, QTableWidgetItem('二年级'))
        self.tablewidget.setItem(1, 2, QTableWidgetItem('70'))

        self.tablewidget.setItem(2, 0, QTableWidgetItem('赵云'))
        self.tablewidget.setItem(2, 1, QTableWidgetItem('三年级'))
        self.tablewidget.setItem(2, 2, QTableWidgetItem('88'))

        self.tablewidget.setItem(3, 0, QTableWidgetItem('马超'))
        self.tablewidget.setItem(3, 1, QTableWidgetItem('一年级'))
        self.tablewidget.setItem(3, 2, QTableWidgetItem('75'))


        # 利用for循环设置每个cell中item的对齐方式
        for i in range(4):
            for j in range(3):
                self.tablewidget.item(i, j).setTextAlignment(Qt.AlignCenter)

        # 新增一个窗口，用来布局嵌套，将水平布局放在该窗口中，再将该窗口放在主窗口的垂直布局中。
        widget_1 = QWidget()
        self.btn_sort_Up = QPushButton('排序（升）')
        self.btn_sort_down = QPushButton('排序（降）')
        self.combobox = QComboBox()
        self.combobox.addItems(['姓名', '年级', '分数'])

        # 新增一个水平布局，用来存放两个按钮，该布局放在新增的widget_1中
        Hbox = QHBoxLayout(widget_1)
        Hbox.addWidget(self.combobox)
        Hbox.addWidget(self.btn_sort_Up)
        Hbox.addWidget(self.btn_sort_down)

        vbox = QVBoxLayout(self)  # 感觉self可以代替self.setLayout()
        vbox.addWidget(self.tablewidget)
        vbox.addWidget(widget_1)

        self.btn_sort_Up.clicked.connect(lambda: self.sort(self.btn_sort_Up))
        self.btn_sort_down.clicked.connect(lambda: self.sort(self.btn_sort_down))

    def sort(self, btn):
        global col
        if self.combobox.currentText() == '姓名':
            col = 0
        elif self.combobox.currentText() == '年级':
            col = 1
        elif self.combobox.currentText() == '分数':
            col = 2
        text = btn.text()
        if text == '排序（升）':
            self.tablewidget.sortItems(col, Qt.AscendingOrder)  # 设置以分数来升序排列，也可以改变列索引，来改变排列对象
        elif text == '排序（降）':
            self.tablewidget.sortItems(col, Qt.DescendingOrder)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ColumnSort()
    w.show()
    sys.exit(app.exec())