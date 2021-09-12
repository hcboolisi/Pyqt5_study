import sys

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QApplication, QFontDialog
from PyQt5.QtCore import Qt

class FontDialog(QWidget):
    def __init__(self):
        super(FontDialog, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QFontDialog字体对话框')

        vbox = QVBoxLayout()
        self.btn = QPushButton('选择字体')
        self.btn.clicked.connect(self.getfont)

        self.label = QLabel('你好Python,你好PyQt5')
        self.label.setAlignment(Qt.AlignCenter)

        vbox.addWidget(self.btn)
        vbox.addWidget(self.label)

        self.setLayout(vbox)
        self.resize(300, 200)

    def getfont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.label.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = FontDialog()
    w.show()
    sys.exit(app.exec_())
