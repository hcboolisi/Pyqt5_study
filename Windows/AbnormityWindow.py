import sys

from PyQt5.QtGui import QBitmap, QPainter, QPixmap, QCursor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication


class AbnormityWindow(QWidget):
    def __init__(self):
        super(AbnormityWindow, self).__init__()
        self.setWindowTitle('异形窗口')
        self.pix = QBitmap('../Image/透明图1.png')
        self.resize(self.pix.size())
        self.setMask(self.pix)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), QPixmap('../Image_1/6.jpg'))

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = AbnormityWindow()
    w.show()
    sys.exit(app.exec_())