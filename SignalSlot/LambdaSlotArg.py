import sys
from functools import partial

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication, QMessageBox


class LambdaSlot(QWidget):
    def __init__(self):
        super(LambdaSlot, self).__init__()
        self.setWindowTitle('利用Lambda表达式向槽函数传递参数')
        self.resize(400, 300)

        vbox = QVBoxLayout()
        self.btn1 = QPushButton('按钮1')
        self.btn1.setObjectName('button1')
        self.btn2 = QPushButton('按钮2')
        self.btn2.setObjectName('button2')

        vbox.addWidget(self.btn1)
        vbox.addWidget(self.btn2)
        self.setLayout(vbox)

        k = 30
        i = 30

        # 利用Lambda表达式，来向槽函数传递参数
        # self.btn1.clicked.connect(lambda: self.on_button1_clicked(20, 30))
        # self.btn2.clicked.connect(lambda: self.on_button1_clicked(k, i))
        # self.btn1.clicked.connect(lambda: QMessageBox.information(self, '提示', '单击了按钮1'))

        # 利用partial来来向槽函数传递参数
        self.btn1.clicked.connect(partial(self.on_button1_clicked, 20, 30))
        self.btn2.clicked.connect(partial(self.on_button1_clicked, k, i))

    def on_button1_clicked(self, a, b):
        print('a + b =', a + b)
        QMessageBox.information(self, '结果', str(a + b))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = LambdaSlot()
    w.show()
    sys.exit(app.exec_())
