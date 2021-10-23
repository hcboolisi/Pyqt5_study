import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication


class WindowPattern(QWidget):
    def __init__(self):
        super(WindowPattern, self).__init__()
        self.setWindowTitle('设置窗口得样式')
        self.resize(400, 300)
        # self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = WindowPattern()
    w.show()
    sys.exit(app.exec_())
