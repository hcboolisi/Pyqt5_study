import sys
from PyQt5.QtCore import QPropertyAnimation, QRect
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


class AnimWindow(QMainWindow):
    def __init__(self):
        super(AnimWindow, self).__init__()
        self.OrigHeight = 50
        self.ChangeHeight = 150
        self.setGeometry(500, 400, 150, self.OrigHeight)

        self.btn = QPushButton(self)
        self.btn.setText('展开')
        self.btn.setGeometry(10, 10, 60, 35)
        self.btn.clicked.connect(self.change)

    def change(self):
        currentheight = self.height()
        if currentheight == self.OrigHeight:
            startheight = self.OrigHeight
            endheight = self.ChangeHeight
            self.btn.setText('收缩')
        else:
            startheight = self.ChangeHeight
            endheight = self.OrigHeight
            self.btn.setText('展开')

        self.animation = QPropertyAnimation(self, b'geometry')
        self.animation.setDuration(500)  # 设置间隔时间，多长时间改变一次
        self.animation.setStartValue(QRect(500, 400, 150, startheight))
        self.animation.setEndValue(QRect(500, 400, 150, endheight))
        self.animation.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = AnimWindow()
    win.show()
    sys.exit(app.exec_())

