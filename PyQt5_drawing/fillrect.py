import sys

from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication


class FillRect(QWidget):
    def __init__(self):
        super(FillRect, self).__init__()
        self.setWindowTitle('用Brush画刷填充区域')
        self.resize(600, 600)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)

        # 实心填充
        brush = QBrush(Qt.SolidPattern)
        painter.setBrush(brush)
        painter.drawRect(10, 10, 100, 100)

        # 密集填充，7种样式,线条越来越细，颜色越来越浅
        brush = QBrush(Qt.Dense1Pattern)
        painter.setBrush(brush)
        painter.drawRect(150, 10, 100, 100)

        brush = QBrush(Qt.Dense2Pattern)
        painter.setBrush(brush)
        painter.drawRect(300, 10, 100, 100)

        brush = QBrush(Qt.Dense3Pattern)
        painter.setBrush(brush)
        painter.drawRect(450, 10, 100, 100)

        brush = QBrush(Qt.Dense4Pattern)
        painter.setBrush(brush)
        painter.drawRect(10, 150, 100, 100)

        brush = QBrush(Qt.Dense5Pattern)
        painter.setBrush(brush)
        painter.drawRect(150, 150, 100, 100)

        brush = QBrush(Qt.Dense6Pattern)
        painter.setBrush(brush)
        painter.drawRect(300, 150, 100, 100)

        brush = QBrush(Qt.Dense7Pattern)
        painter.setBrush(brush)
        painter.drawRect(450, 150, 100, 100)

        # 除以上画刷样式外，还有很多样式，自己学习。

        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = FillRect()
    w.show()
    sys.exit(app.exec_())