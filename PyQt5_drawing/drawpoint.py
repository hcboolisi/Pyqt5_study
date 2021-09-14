import math
import sys

from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication


class DrawPoint(QWidget):
    def __init__(self):
        super(DrawPoint, self).__init__()
        self.setWindowTitle('DrawPoint绘制正弦曲线')
        self.resize(400, 300)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        painter.setPen(Qt.blue)
        size = self.size()

        #  下面这部分就是绘制正弦曲线的方法，对应的X点和Y点的坐标计算，不过我也看的不太懂，方正是个数学
        #  方法，以后慢慢研究。
        for i in range(1000):
            x = 100 * (-1 + 2 * i/1000) + size.width()/2
            y = -50 * math.sin((x - size.width()/2) * math.pi/50) + size.height()/2
            painter.drawPoint(x, y)
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = DrawPoint()
    w.show()
    sys.exit(app.exec_())