import sys

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QApplication


class PushButton(QDialog):
    def __init__(self):
        super(PushButton, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QPushButton按钮')
        vbox = QVBoxLayout()

        self.btn1 = QPushButton('第一个按钮')
        self.btn1.toggle()   # 设置按钮开关，标记状态
        self.btn1.setCheckable(True)   # 设置按钮可核对，可复选，选中或不选中

        self.btn2 = QPushButton()
        self.btn2.setText('图像按钮')  # 设置按钮文本（名字）

        # 两种设置按钮图标的方法
        # self.btn2.setIcon(QIcon('图标_1.jpg'))
        self.btn2.setIcon(QIcon(QPixmap('../Image/图标_1.jpg')))

        self.btn3 = QPushButton('不可用的按钮')  # 另一种设置按钮文本（名字）的方法
        self.btn3.setEnabled(False)   # 设置按钮不可以用

        self.btn4 = QPushButton()
        self.btn4.setText('默认的按钮(M)')
        self.btn4.setShortcut('alt+M')  # 设置按钮快捷键，注意“+”两边不能有空格，
                                        # 也可以用self.btn4.setText('&M默认的按钮')来设置
        self.btn4.setDefault(True)

        # 一个clicked信号对应多个槽
        self.btn1.clicked.connect(self.whichbutton)
        self.btn1.clicked.connect(lambda: self.whichbutton_1(self.btn1))  # 利用lambda表达式来来来进行一个参数的传递，
                                                                          # 其实我感觉就是利用lambda来重新创建了一个新的函数
        self.btn1.clicked.connect(self.buttonstate)

        self.btn2.clicked.connect(self.whichbutton)
        self.btn4.clicked.connect(lambda: self.whichbutton_1(self.btn4))

        vbox.addWidget(self.btn1)
        vbox.addWidget(self.btn2)
        vbox.addWidget(self.btn3)
        vbox.addWidget(self.btn4)

        self.setLayout(vbox)
        self.resize(400, 300)

    # 利用sender来传递一个参数
    def whichbutton(self):
        print('=' * 50)
        sender = self.sender()
        print('以下是whichbutton槽函数输出的内容')
        print('被单机的按钮是<'+sender.text()+'>')   # 复习一下三种格式化字符串的输出
        print(f'被单机的按钮是<{sender.text()}>')
        print('被单机的按钮是<{}>'.format(sender.text()))

    # 自己创建一个参数来传递，相当于点击了按钮以后，按钮自己把自己当作参数传递到这个函数中，作为函数的参数
    def whichbutton_1(self, btn):
        print('='*50)
        print('以下是whichbutton_1槽函数输出的内容')
        print(f'被单机的按钮是<{btn.text()}>')

    def buttonstate(self):
        print('='*50)
        print('以下是buttonstate槽函数输出的内容')
        if self.btn1.isChecked():
            print('按钮1已经被选中')
        else:
            print('按钮1未被选中')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = PushButton()
    w.show()
    sys.exit(app.exec_())