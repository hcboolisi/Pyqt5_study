import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class Splitter(QWidget):
    def __init__(self):
        super(Splitter, self).__init__()
        self.setWindowTitle('拖动控件的边界')
        self.resize(400, 300)

        topleft = QFrame()
        topleft.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        # QSplitter 相当于一个边界可以拖动的容器，将控件放入到splitter容器中，这样就能实现控件边界拖动
        # 容器的放置方向，跟布局是一样的，横向放置和纵向放置，取决于splitter的方向。
        splitter1 = QSplitter(Qt.Horizontal)
        textedit = QTextEdit()
        splitter1.addWidget(topleft)
        splitter1.addWidget(textedit)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox = QHBoxLayout()
        hbox.addWidget(splitter2)
        self.setLayout(hbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Splitter()
    w.show()
    sys.exit(app.exec_())