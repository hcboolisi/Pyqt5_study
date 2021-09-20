import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication, QComboBox, QTableWidget, QTableWidgetItem, QPushButton


class PlaceControlInCell(QWidget):
    def __init__(self):
        super(PlaceControlInCell, self).__init__()
        self.setWindowTitle('在表格中放置控件')
        self.resize(500, 300)
        vbox = QVBoxLayout()

        self.tablewidget = QTableWidget(4, 3)
        self.tablewidget.setHorizontalHeaderLabels(['姓名', '年龄', '性别'])

        item_name = QTableWidgetItem('姓名')
        item_name.setTextAlignment(Qt.AlignCenter)
        self.tablewidget.setItem(0, 0, item_name)

        btn = QPushButton('修改')
        # 利用QSS来设置控件边界与单元格边界之间的距离
        btn.setStyleSheet('QPushButton{margin:10px};')
        btn.clicked.connect(self.clicked)
        self.tablewidget.setCellWidget(0, 1, btn)

        combobox = QComboBox()
        combobox.addItems(['男', '女'])
        combobox.setStyleSheet('QComboBox{margin:3px};')
        self.tablewidget.setCellWidget(0, 2, combobox)

        vbox.addWidget(self.tablewidget)
        self.setLayout(vbox)

    def clicked(self):
        self.tablewidget.setCellWidget(0, 1, None)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = PlaceControlInCell()
    w.show()
    sys.exit(app.exec_())