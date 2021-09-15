import sys

from PyQt5.QtGui import QPainter, QPolygon, QImage
from PyQt5.QtCore import Qt, QRect, QPoint
from PyQt5.QtWidgets import QWidget, QApplication


class DrawPatterning(QWidget):
    def __init__(self):
        super(DrawPatterning, self).__init__()
        self.setWindowTitle('绘制各种图形')
        self.resize(400, 800)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(Qt.red)

        # 绘制弧线。
        # 1 alen = 1/16 度， 所有要绘制50度的弧线，就要用50*16
        rect = QRect(0, 10, 100, 100)  # 创建绘制区域，也可以不要直接写成painter.drawArc(0, 10, 100, 100, 0, 50*16)
        # painter.drawArc(0, 10, 100, 100, 0, 50 * 16)
        painter.drawArc(rect, 0, 130*16)  # 后面两个参数，为开始角度和结束角度。

        # 通过弧线绘制圆，
        # 设置一个正方形的绘制区域，然后360度
        painter.setPen(Qt.blue)
        painter.drawArc(120, 10, 150, 150, 0, 360*16)
        # 也可以绘制椭圆，通过改变绘制区域的长宽值
        # painter.drawArc(120, 10, 150, 50, 0, 360*16)

        # 绘制带弦的弧形
        painter.drawChord(10, 120, 100, 100, 12, 150*16)

        # 绘制扇形
        painter.drawPie(10, 240, 200, 200, 12, 140*16)

        # 绘制椭圆
        # 可以改变区域大小来绘制圆形，设置宽和高一样，就可以绘制圆形
        painter.drawEllipse(180, 180, 200, 100)

        # 绘制多边形
        p1 = QPoint(140, 380)
        p2 = QPoint(270, 420)
        p3 = QPoint(290, 512)
        p4 = QPoint(290, 588)
        p5 = QPoint(200, 530)
        polygon = QPolygon([p1, p2, p3, p4, p5])
        painter.drawPolygon(polygon)
        # 也可以直接把点放进去去绘制
        # painter.drawPolygon(p1, p2, p3, p4, p5)

        # 绘制图像
        image = QImage('../图标.jpg')
        rect = QRect(10, 600, int(image.width()/2), int(image.height()/2))  # 这里图像的宽高，除以2后可能会得到一个浮点数，运行是会出错
                                                                            # 所有转换一下，直接转换成整数。
        # rect = QRect(10, 600, 200, 200)
        painter.drawImage(rect, image)

        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = DrawPatterning()
    w.show()
    sys.exit(app.exec_())