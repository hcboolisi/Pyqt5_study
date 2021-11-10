import sys

from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QWidget, QApplication


class AbnormityWindowCartoon(QWidget):
    def __init__(self):
        super(AbnormityWindowCartoon, self).__init__()
        self.setWindowTitle('异形窗口动画')
        self.i = 1
        self.myPix()
        self.timer = QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.timeChange)
        self.timer.start()

    def myPix(self):
        self.update()
        if self.i == 5:
            self.i = 1
        self.myPic = {1: "../Image/上.png", 2: "../Image/左.png", 3: "../Image/下.png", 4: "../Image/右.png"}
        self.pix = QPixmap(self.myPic[self.i])
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_Drag = True
            print(event.globalPos())  # event.globalPos()鼠标点击点在全屏中的全局坐标；
            print(self.pos())  # self.pos()窗口左上角原点的坐标。
            print(event.pos())  # event.Pos()点击点在窗口中的相对坐标。（不包括标题栏）
            # 用鼠标点击点在全屏中的全局坐标减去该点在窗口中的相对坐标，就等于该窗口的原点坐标。
            # 所得到的值是一个QPoint值。
            self.m_DragPosition = event.globalPos() - self.pos()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 设置当前的光标样式为手形样式

        # 如果点击的是右键，则关闭窗口
        if event.button() == Qt.RightButton:
            self.close()

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.m_Drag:
            # 实时计算窗口左上角坐标
            self.move(event.globalPos() - self.m_DragPosition)

    def mouseReleaseEvent(self, event):
        self.m_Drag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def timeChange(self):
        self.i += 1
        self.myPix()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = AbnormityWindowCartoon()
    w.show()
    sys.exit(app.exec_())