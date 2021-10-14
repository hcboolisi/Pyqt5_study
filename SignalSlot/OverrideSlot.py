import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt


class OverRideSlot(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Override 覆盖槽函数')
        self.resize(400, 300)

    # 覆盖槽函数就是将已有的槽函数，重新写一边，写成自己的需要的功能。
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Alt:
            self.close()
        elif e.key() == Qt.Key_Space:
            self.setWindowTitle('按下空格键')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = OverRideSlot()
    w.show()
    sys.exit(app.exec_())
