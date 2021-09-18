#! /sur/bin/python3
# _*_ coding: utf-8 _*_

import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


class EXample(QWidget):

    def __init__(self):
        super(EXample, self).__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message box')
        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, '提示信息',
                                     '你确定要退出吗？', QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EXample()
    sys.exit(app.exec_())
