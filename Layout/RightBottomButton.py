import sys

from PyQt5.QtWidgets import *


class RightBottomButton(QMainWindow):
    def __init__(self):
        super(RightBottomButton, self).__init__()
        self.setWindowTitle('通过布局的伸缩量来设置控件位置')
        self.resize(800, 600)

        vbox = QVBoxLayout()
        btn1 = QPushButton('按钮1')
        btn2 = QPushButton('按钮2')
        btn3 = QPushButton('按钮3')
        btn4 = QPushButton('按钮4')

        hbox = QHBoxLayout()
        btnOK = QPushButton('确定')
        btncancell = QPushButton('取消')

        hbox.addStretch(1)
        hbox.addWidget(btnOK)
        # hbox.addStretch(1)
        hbox.addWidget(btncancell)

        vbox.addStretch(0)
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)

        vbox.addStretch(1)
        vbox.addLayout(hbox)

        center = QWidget()
        self.setCentralWidget(center)
        center.setLayout(vbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = RightBottomButton()
    w.show()
    sys.exit(app.exec_())