import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QApplication


class BasicQSS(QWidget):
    def __init__(self):
        super(BasicQSS, self).__init__()
        self.setWindowTitle("QSS样式表")

        self.btn1 = QPushButton('按钮1')
        self.btn2 = QPushButton('按钮2')
        # 设置按钮2的name属性
        self.btn2.setProperty('name', 'btn2')
        self.btn3 = QPushButton('按钮3')

        # 直接在按钮3种设置自己的QSS样式
        self.btn3.setStyleSheet('''
            background-color:black;
            color:red;
            font-size:30px;
            height: 55
        ''')

        vbox = QVBoxLayout()
        vbox.addWidget(self.btn1)
        vbox.addWidget(self.btn2)
        vbox.addWidget(self.btn3)

        self.setLayout(vbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = BasicQSS()

    # 设置全部QPushButton的QSS样式
    # qssstyle ='''
    #     QPushButton{
    #         background-color : red
    #     }
    # '''

    # 单独设置属性名为btn2的按钮的QSS样式
    qssstyle = '''
          QPushButton[name = btn2]{
              background-color : red;
              color : white;
              height : 80;
              font-size:30px;
          }
      '''
    w.setStyleSheet(qssstyle)
    w.show()
    sys.exit(app.exec_())