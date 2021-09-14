'''
绘图API:QPainter
绘制内容：文本，图形，图像
使用方法：
1.创建QPainter实例，painter = QPainter()
2.painter.begin(),利用begin()方法开始画笔。
3.painter.DrawText()，等方法进行绘制。
4.painter.end(),利用end()方法，结束画笔。跟打开文件一样，需要开始，结束。

必须在paintEvent事件方法中绘制各类元素。
'''
import sys

from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt


class DrawText(QWidget):
    def __init__(self):
        super(DrawText, self).__init__()
        self.setWindowTitle('drawtext绘制文本')
        self.resize(400, 300)

    def paintEvent(self, event):
        self.painter = QPainter(self)
        self.painter.begin(self)
        self.painter.setPen(QColor(150, 50, 30))
        self.painter.setFont(QFont('SimSun', 25))
        self.painter.drawText(event.rect(), Qt.AlignCenter, '你最近还好吗？')
        self.painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = DrawText()
    w.show()
    sys.exit(app.exec_())