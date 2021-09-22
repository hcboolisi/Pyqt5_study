import sys

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QTableWidget, QVBoxLayout, QApplication, QTableWidgetItem


class CellImageSize(QWidget):
    def __init__(self):
        super(CellImageSize, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('设置表格图像尺寸')
        self.resize(1024, 768)

        tw = QTableWidget(4, 3)
        tw.setIconSize(QSize(400, 300))

        for i in range(3):
            tw.setColumnWidth(i, 400)

        for i in range(4):
            tw.setRowHeight(i, 300)

        for k in range(12):  # 总的单元格数量是12个
            i = int(k / 3)   # 横向排列，用每个单元格的“编号数”除以表格的列数，就可以得到该单元格的行索引
            j = int(k % 3)   # 横向排列，用每个单元格的“编号数”除以表格的列数取余，就可以得到该单元格的列索引
            item = QTableWidgetItem()
            item.setIcon(QIcon('../Image_1/%d.jpg' % (k+1)))
            tw.setItem(i, j, item)

        vbox = QVBoxLayout()
        vbox.addWidget(tw)
        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CellImageSize()
    w.show()
    sys.exit(app.exec())
