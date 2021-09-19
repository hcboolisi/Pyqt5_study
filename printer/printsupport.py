import sys

from PyQt5 import QtPrintSupport
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit


class PrintSupport(QMainWindow):
    def __init__(self):
        super(PrintSupport, self).__init__()
        self.resize(300, 350)
        self.setWindowTitle('打印机的使用')

        button = QPushButton('打印QTextEdit控件中的内容', self)
        button.setGeometry(25, 20, 250, 50)
        button.clicked.connect(self.print)

        self.textedit = QTextEdit('默认文本', self)
        self.textedit.setGeometry(25, 80, 250, 250)

    def print(self):
        printer = QtPrintSupport.QPrinter()
        painter = QPainter()

        painter.begin(printer)
        screen = self.textedit.grab()
        painter.drawPixmap(10, 10, screen)
        painter.end()

        print('print')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = PrintSupport()
    w.show()
    sys.exit(app.exec_())