import sys

from PyQt5.QtGui import QBitmap, QPainter, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication


class AbnormityWindow(QWidget):
    def __init__(self):
        super(AbnormityWindow, self).__init__()
        self.setWindowTitle('异形窗口')
        self.pix = QBitmap('../Image/333.png')
        self.resize(self.pix.size())
        self.setMask(self.pix)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), QPixmap('../Image_1/6.jpg'))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = AbnormityWindow()
    w.show()
    sys.exit(app.exec_())