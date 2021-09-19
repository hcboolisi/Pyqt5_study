import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

'''
面向对象编程最重要的三个部分是类(class)、数据和方法。
我们创建了一个类的调用，这个类继承自QWidget。这就意味着，
我们调用了两个构造器，一个是这个类本身的，一个是这个类继承的。
super()构造器方法返回父级的对象。
__init__()方法是构造器的一个方法。
'''

class IconWindow(QWidget):

    def __init__(self):
        super().__init__()  # 调用父类QWidget的初始化方法

        self.initUI()  # 在初始化方法中调用自己的initUI方法，此方法是自己创建的，主要功能是初始化窗口基本属性。

    # 创建一个用于初始化窗口的方法，名叫initUI，然后在类的初始化方法中调用。
    def initUI(self):
        self.setGeometry(300, 300, 800, 600)  # 设置窗口的位置和大小，等同于resize和move两个方法
        self.setWindowTitle('带有图标的窗口')  # 设置窗口的图标
        self.setWindowIcon(QIcon('../Image/图标.jpg'))  # 设置窗口的图标，图标可以使用绝对路径和相对路径，此为相对路径

        self.show()  # show方法用于在屏幕上展示窗口


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建一个app运用实例
    w = IconWindow()  # 利用自己创建的类来实例化一个窗口
    sys.exit(app.exec_())  # 固定写法
