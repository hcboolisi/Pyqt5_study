import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from DateDialog import DateDialog


class MultiWindow(QWidget):
    def __init__(self):
        super(MultiWindow, self).__init__()
        self.setWindowTitle('多窗口交互1，不使用信号槽')

        self.ledit = QLineEdit()
        self.btn1 = QPushButton('弹出对话框1')
        self.btn2 = QPushButton('弹出对话框2')

        self.btn1.clicked.connect(self.onButton1Clicked)
        self.btn2.clicked.connect(self.onButton2Clicked)

        grid = QGridLayout()
        grid.addWidget(self.ledit)
        grid.addWidget(self.btn1)
        grid.addWidget(self.btn2)
        self.setLayout(grid)

    def onButton1Clicked(self):
        dialog = DateDialog()
        result = dialog.exec()
        date = dialog.dateTime()
        self.ledit.setText(date.date().toString())
        dialog.destroy()

    def onButton2Clicked(self):
        date, time, result = DateDialog.getDateTime()
        self.ledit.setText(date.toString())
        if result == DateDialog.Accepted:
            print('点击确定按钮')
        else:
            print('点击取消按钮')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MultiWindow()
    w.show()
    sys.exit(app.exec_())