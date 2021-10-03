import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

text = ''


class Calc(QWidget):
    def __init__(self):
        super(Calc, self).__init__()
        self.setWindowTitle('利用循环和栅格布局设计计算器界面')

        vbox = QVBoxLayout()
        self.ledit = QLineEdit()
        self.ledit.setReadOnly(True)
        self.ledit.setFont(QFont('Arial', 25))

        grid = QGridLayout()
        vbox.addWidget(self.ledit)
        vbox.addLayout(grid)
        self.setLayout(vbox)

        names = ['Cls', 'Back', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        # 利用列表生成式，从两个循环中列出计算器每个按钮的位置,poss是一个列表，列表中的每个元素是一个元组
        poss = [(i, j) for i in range(5) for j in range(4)]

        # zip函数将names列表中的元素和poss列表中的元素一一对应打包在一起，就跟字典中键值对一样的，
        # 然后在利用for循环，将打包后的每对数据提出来,赋值到两个变量中，就像拆包一样，这样就可以得到
        # 计算器中每个按钮的名称和栅格布局中的位置，最后再将每个按钮的名称和位置，添加到栅格布局中。
        for pos, name in zip(poss, names):
            if name == '':  # 设置如果按钮名称为空，则不添加按钮，直接略过
                continue
            else:
                self.btn = QPushButton(name)
                self.btn.setFont(QFont('Arial', 15))
                self.btn.clicked.connect(self.display)
                grid.addWidget(self.btn, *pos)
                # 将一一对应的按钮和位置添加到栅格布局中，因为pos是一个元组，添加的时候，无法直接添加，要将里面的每个元素都提取出来，
                # 所以利用python的一个特殊语法，在前面加个“ * ”号，就可以将pos元组中的元素单独提取出来。功能其实跟
                # pos[0],pos[1],是一样的，所以上面的代码也可以写成：
                # grid.addWidget(QPushButton(name), pos[0], pos[1])
                # 其实也可以写成：
                # i, j = pos  # 利用元组的拆包将每个值提取出来赋值到i，j变量中
                # grid.addWidget(QPushButton(name), i, j)

    def display(self):
        global text
        sender = self.sender()
        if sender.text() == 'Back':
            a = len(text) - 1
            text = text[0:a]
        elif sender.text() == 'Close':
            app.quit()
        elif sender.text() == 'Cls':
            text = ''
        else:
            text += sender.text()
        self.ledit.setText(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Calc()
    w.show()
    sys.exit(app.exec_())