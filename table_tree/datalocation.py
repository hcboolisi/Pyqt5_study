import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QBrush
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidget, QVBoxLayout, QTableWidgetItem


class DataLocation(QWidget):
    def __init__(self):
        super(DataLocation, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('定位表格中数据位置')
        self.resize(400, 500)

        tablewidget = QTableWidget()
        tablewidget.setColumnCount(4)
        tablewidget.setRowCount(40)
        tablewidget.resizeRowsToContents()

        vbox = QVBoxLayout()
        vbox.addWidget(tablewidget)
        self.setLayout(vbox)

        # for循环向表格中填入数据
        for i in range(40):
            for j in range(4):
                text = f'({i},{j})'  # 设置数据的内容
                item = QTableWidgetItem(text)  # 将数据转换为QTableWidgetItem格式
                item.setTextAlignment(Qt.AlignCenter)  # 设置数据的对齐方式
                tablewidget.setItem(i, j, item)  # 将数据添加到每个cell中

        # 搜索满足条件的单元格
        putdata = input('请输入你要查找的内容int,int：')
        text = f'({putdata})'
        # MatchExactly,匹配模式，精确匹配，也可以换成其他匹配模式，其返回的是一个列表。
        find_items = tablewidget.findItems(text, Qt.MatchExactly)
        if len(find_items) > 0:
            find_item = find_items[0]
            find_item.setBackground(QBrush(QColor(Qt.green)))  # 设置找到的cell背景色为绿色
            find_item.setForeground(QBrush(QColor(Qt.red)))  # 设置找到的cell前景色为红色

            # 定位到找到的cell位置
            row = find_item.row()  # 返回找到的cell所在的行数
            tablewidget.verticalScrollBar().setSliderPosition(row)  # 将滚动条的滑块定位到该行的位置


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = DataLocation()
    w.show()
    sys.exit(app.exec_())