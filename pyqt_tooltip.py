import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton,
                             QApplication)
from PyQt5.QtGui import QFont, QIcon

# 创建一个提示窗口类继承自QWidget
class tooltip_w(QWidget):
    def __init__(self):  # 初始化类属性
        super().__init__()  # 调用父类的初始化方法

        self.initUI()  # 在初始化方法中调用自己的initUI方法

    # 创建一个initUI方法
    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))  # 设置提示信息的字体（SansSerif）和字号为 10
        self.setToolTip('这是一个<b>窗口</b>')  # 设置窗口自己的提示信息

        btn = QPushButton('这是一个按钮', self)  # 实例化一个按钮，并设置按钮上的信息
        btn.setToolTip('这是一个<b>按钮</b>，他的功能是...')  # 设置按钮的提示信息
        btn.resize(btn.sizeHint())  # 设施按钮的大小，sizeHint（）返回一个推荐值，这个我也不太懂，以后再说
        btn.move(50, 50)  # 设置按钮的位置

        self.setGeometry(300, 300, 800, 600)  # 设置窗口的位置大小
        self.setWindowTitle('主窗口')  # 设置窗口的标题
        self.setWindowIcon(QIcon('图标.jpg'))  # 设置窗口的图标
        self.show()  # 在屏幕中展示窗口

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 实例化一个app应用

    w = tooltip_w()  # 实例化一个窗口
    sys.exit(app.exec_())
