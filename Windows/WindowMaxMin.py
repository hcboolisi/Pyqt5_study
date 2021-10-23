import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QApplication
from PyQt5.QtCore import Qt


class WindowMaxMin(QWidget):
    def __init__(self):
        super(WindowMaxMin, self).__init__()

        self.setWindowTitle('代码控制窗口最大最小化')
        self.resize(400, 300)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.minbtn = QPushButton('最小化')
        self.maxbtn = QPushButton('最大化')
        self.closebtn = QPushButton('关闭窗口')

        vbox = QVBoxLayout()
        vbox.addWidget(self.maxbtn)
        vbox.addWidget(self.minbtn)
        vbox.addWidget(self.closebtn)

        self.setLayout(vbox)

        self.minbtn.clicked.connect(self.showMinimized)
        self.maxbtn.clicked.connect(self.showMaximized)
        self.closebtn.clicked.connect(self.close)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = WindowMaxMin()
    w.show()
    sys.exit(app.exec_())
