import sys

from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication


class DrawMultiLine(QWidget):
    def __init__(self):
        super(DrawMultiLine, self).__init__()
        self.setWindowTitle('设置Pen的样式，绘制多种线')
        self.resize(400, 300)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)

        pen = QPen(Qt.red, 3, Qt.SolidLine)  # 设置pen为红色，粗细3，类型为实线
        painter.setPen(pen)
        painter.drawLine(40, 40, 350, 40)

        pen.setStyle(Qt.DashLine)  # 设置pen的类型为虚线
        painter.setPen(pen)
        painter.drawLine(40, 80, 350, 80)

        pen.setStyle(Qt.DashDotLine)  # 设置pen的类型为点划线，一个连接线加一点
        painter.setPen(pen)
        painter.drawLine(40, 120, 350, 120)

        pen.setStyle(Qt.DashDotDotLine)  # 设置pen的类型为DashDotDotLine,一个连接线加两点
        painter.setPen(pen)
        painter.drawLine(40, 160, 350, 160)

        pen.setStyle(Qt.CustomDashLine)  # 设置pen的类型为自定义虚线
        pen.setColor(Qt.blue)  # 设置pen的颜色
        pen.setWidth(10)       # 设置pen的粗细
        pen.setDashPattern([1, 4, 5, 4])  # 1和5是线的长度，4和4是两条线之间的间距长度。
        painter.setPen(pen)
        painter.drawLine(40, 200, 350, 200)

        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = DrawMultiLine()
    w.show()
    sys.exit(app.exec_())
