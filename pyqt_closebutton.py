#!/usr/bin/python3
# _*_ coding : utf_8 _*_


import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QToolTip
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont, QIcon


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))  # 设置提示的字体和大小，注意写法和需要导入的相关库

        qbtn = QPushButton('退出', self)  # 实例化一个退出按钮，注意写法
        qbtn.clicked.connect(QCoreApplication.instance().quit)  # 关联按钮点击之后的事件即退出操作，信号与槽机制
        qbtn.setToolTip('这是一个<b>退出按钮</b>，它的功能使退出程序')  # 设置按钮的提示信息
        qbtn.resize(qbtn.sizeHint())  # 设置按钮的大小
        qbtn.move(50, 50)   # 设置按钮的位置

        self.setGeometry(300, 300, 800, 600)    # 设置窗口的大小，位置
        self.setWindowIcon(QIcon('图标.jpg'))    # 设置窗口图标，注意写法和需要导入的相关库
        self.setWindowTitle('退出按钮')     # 设置窗口标题
        self.setToolTip('这是一个窗口')   # 设置窗口提示信息
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
