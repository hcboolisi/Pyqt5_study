import sys

from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QApplication, QMessageBox, QWidget


class MessageBox(QMainWindow):
    def __init__(self):
        super(MessageBox, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QMessageBox消息对话框')
        self.btn_1 = QPushButton('显示关于对话框')
        self.btn_2 = QPushButton('显示错误对话框')
        self.btn_3 = QPushButton('显示警告对话框')
        self.btn_4 = QPushButton('显示提问对话框')
        self.btn_5 = QPushButton('显示消息对话框')

        vbox = QVBoxLayout()
        vbox.addWidget(self.btn_1)
        vbox.addWidget(self.btn_2)
        vbox.addWidget(self.btn_3)
        vbox.addWidget(self.btn_4)
        vbox.addWidget(self.btn_5)

        self.btn_1.clicked.connect(self.ShowDialog)
        self.btn_2.clicked.connect(self.ShowDialog)
        self.btn_3.clicked.connect(self.ShowDialog)
        self.btn_4.clicked.connect(self.ShowDialog)
        self.btn_5.clicked.connect(self.ShowDialog)

        centerwidget = QWidget()
        self.setCentralWidget(centerwidget)
        centerwidget.setLayout(vbox)

        self.resize(250, 300)

    def ShowDialog(self):
        sender = self.sender()
        if sender.text() == '显示关于对话框':
            QMessageBox.about(self, '关于', '这是一个关于对话框')  # 关于对话框不可以设置按钮
        elif sender.text() == '显示错误对话框':
            QMessageBox.critical(self, '错误', '这是一个错误对话框', QMessageBox.Yes | QMessageBox.No)
        elif sender.text() == '显示警告对话框':
            QMessageBox.warning(self, '警告', '这是一个警告对话框', QMessageBox.Yes | QMessageBox.No)
        elif sender.text() == '显示提问对话框':
            QMessageBox.question(self, '提问', '这是一个提问对话框', QMessageBox.Yes | QMessageBox.No)
        elif sender.text() == '显示消息对话框':
            QMessageBox.information(self, '消息', '这是一个消息对话框', QMessageBox.Yes | QMessageBox.No)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MessageBox()
    w.show()
    sys.exit(app.exec_())