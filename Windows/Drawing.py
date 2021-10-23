'''
实现绘图应用：

1、在哪里绘图：在白色背景下的QPixmap对象中绘图
2、如何绘图：通过paintEvent方法来绘图，调用update方法来触发paintEvent方法
3、如何通过移动鼠标来绘图:
    (1)鼠标按下：通过mousePressEvent方法来实现
    (2)鼠标移动：mouseMoveEvent
    (3)鼠标抬起：mousePressEvent
'''


import sys

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QWidget, QApplication


class Drawing(QWidget):
    def __init__(self):
        super(Drawing, self).__init__()
        self.pix = QPixmap(800, 600)
        self.lastpoint = QPoint()
        self.endpoint = QPoint()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('绘图板')
        self.resize(800, 600)
        self.pix.fill(Qt.white)

    def paintEvent(self, event):
        painter = QPainter(self.pix)
        # 根据鼠标指针前后两个点绘制直线
        painter.drawLine(self.lastpoint, self.endpoint)
        # 让后一个点一个点得坐标值等前一个点得坐标值，把后一个点作为下一条直线得前一个点，循环返复
        # 就能画出连续得直线
        self.lastpoint = self.endpoint
        painter1 = QPainter(self)
        painter1.drawPixmap(0, 0, self.pix)

    def mousePressEvent(self, event):
        print("鼠标按下事件的button：", event.button())
        print("鼠标按下时的左键：", Qt.LeftButton)
        print("鼠标按下时左键的位置：", event.pos())
        # 如果鼠标按下事件的按键是左键，那么获取该事件的坐标值pos()赋值到self.lastpoint
        if event.button() == Qt.LeftButton:
            self.lastpoint = event.pos()

    def mouseMoveEvent(self, event):
        print("鼠标移动事件的buttons：", event.buttons())
        print("鼠标移动事件的button：", event.button())
        print("鼠标移动时的左键：", Qt.LeftButton)
        print("鼠标移动时左键的位置：", event.pos())
        if event.buttons() and Qt.LeftButton:
            self.endpoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        print("鼠标抬起事件的button：", event.button())
        print("鼠标抬起时的左键：", Qt.LeftButton)
        print("鼠标抬起时左键的位置：", event.pos())
        if event.button() == Qt.LeftButton:
            self.endpoint = event.pos()
            self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Drawing()
    w.show()
    sys.exit(app.exec_())