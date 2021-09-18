import sys

from PyQt5.QtGui import QFont, QPalette
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QApplication, QColorDialog
from PyQt5.QtCore import Qt

class ColorDialog(QWidget):
    def __init__(self):
        super(ColorDialog, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QColorDialog颜色对话框')

        vbox = QVBoxLayout()
        self.btn = QPushButton('设置字体颜色')
        self.btn.clicked.connect(self.getcolor)

        self.btn_1 = QPushButton('设置背景颜色')
        self.btn_1.clicked.connect(self.getcolor)

        self.label = QLabel('你还好吗？')
        self.label.setAlignment(Qt.AlignCenter)

        vbox.addWidget(self.btn)
        vbox.addWidget(self.btn_1)
        vbox.addWidget(self.label)


        self.setLayout(vbox)
        self.resize(300, 100)

    def getcolor(self):
        sender = self.sender()
        color = QColorDialog.getColor()
        p = QPalette()
        if sender.text() == '设置字体颜色':
            p.setColor(QPalette.WindowText, color)
            self.label.setPalette(p)
        if sender.text() == '设置背景颜色':
            p.setColor(QPalette.Window, color)
            self.label.setAutoFillBackground(True)
            self.label.setPalette(p)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ColorDialog()
    w.show()
    sys.exit(app.exec_())