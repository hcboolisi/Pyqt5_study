import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication


class WinSignal(QWidget):
    closeSignal = pyqtSignal()

    def __init__(self):
        super(WinSignal, self).__init__()
        self.setWindowTitle('为窗口添加信号')
        self.resize(400, 300)
        btn = QPushButton(self)
        btn.setText('关闭窗口')
        btn.setGeometry(100, 100, 80, 50)

        # 尝试了一下，这里可以不用写下面的btnClicked方法，直接用按钮连接自定义的信号，然后该信号
        # 再连接关闭窗口的方法也能达到效果。可能这只针对没有参数的信号。
        # btn.clicked.connect(self.closeSignal)

        btn.clicked.connect(self.btnClicked)
        self.closeSignal.connect(self.closeWindow)

    def btnClicked(self):
        self.closeSignal.emit()

    def closeWindow(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = WinSignal()
    w.show()
    sys.exit(app.exec_())
