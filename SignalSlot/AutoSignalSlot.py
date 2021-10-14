import sys

from PyQt5.QtCore import pyqtSlot, QMetaObject
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QHBoxLayout


class AutoSignalSlot(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle('信号自动连接槽')

        hbox = QHBoxLayout(self)
        self.btn = QPushButton('ok')
        self.btn.setObjectName('okButton')  # 设置按钮1的对象名称为‘okButton’,用来自动连接槽函数。

        self.btn1 = QPushButton('cancel')
        self.btn1.setObjectName('cancelButton')  # 设置按钮2的对象名称为‘cancelButton’,用来自动连接槽函数。

        # 传统的，手动连接槽函数方式
        # self.btn.clicked.connect(self.on_okButton_clicked)

        hbox.addWidget(self.btn)
        hbox.addWidget(self.btn1)

        # 通过这个功能自动找固定格式的槽函数连接。在定义槽函数的时候，就要用固定的格式“on_对象名称_信号名称”
        # 该语句最好写在布局之后，因为写在之前，不能自动连接槽函数。
        QMetaObject.connectSlotsByName(self)

    # 利用装饰器的方式，声明一下此函数为一个槽函数，装饰器，这个东西，还需要再研究。
    @pyqtSlot()
    def on_okButton_clicked(self):
        print('点击了OK按钮')

    @pyqtSlot()
    def on_cancelButton_clicked(self):
        print('点击了cancel按钮')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = AutoSignalSlot()
    w.show()
    sys.exit(app.exec_())