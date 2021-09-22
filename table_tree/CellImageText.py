import sys

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QTableWidget, QApplication, QTableWidgetItem


class CellImageText(QWidget):
    def __init__(self):
        super(CellImageText, self).__init__()
        self.setWindowTitle('设置item图文混排')
        self.resize(400, 300)

        tablewidget = QTableWidget(4, 3, self)
        tablewidget.setGeometry(20, 20, 360, 250)

        item = QTableWidgetItem(QIcon('../Image/new_file.jpg'), '张飞')
        tablewidget.setItem(0, 0, item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CellImageText()
    w.show()
    sys.exit(app.exec())
