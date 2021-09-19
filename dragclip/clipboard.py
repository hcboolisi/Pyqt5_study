import sys

from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QLabel, QApplication


class ClipBoard(QWidget):
    def __init__(self):
        super(ClipBoard, self).__init__()
        self.setWindowTitle('剪贴板')
        self.copytextbtn = QPushButton('复制文本')
        self.pastetextbtn = QPushButton('粘贴文本')

        self.copyHTMLbtn = QPushButton('复制HTML')
        self.pasteHTMLbtn = QPushButton('粘贴HTML')

        self.copyimagebtn = QPushButton('复制图像')
        self.pasteimagebtn = QPushButton('粘贴图像')

        self.textlabel = QLabel('默认文本')
        self.imagelabel = QLabel()
        self.imagelabel.setPixmap(QPixmap('../Image/图标.jpg'))

        layout = QGridLayout()
        layout.addWidget(self.copytextbtn, 0, 0)
        layout.addWidget(self.copyimagebtn, 0, 1)
        layout.addWidget(self.copyHTMLbtn, 0, 2)
        layout.addWidget(self.pastetextbtn, 1, 0)
        layout.addWidget(self.pasteimagebtn, 1, 1)
        layout.addWidget(self.pasteHTMLbtn, 1, 2)

        layout.addWidget(self.textlabel, 2, 0, 1, 2, Qt.AlignCenter)
        layout.addWidget(self.imagelabel, 2, 2)

        self.setLayout(layout)

        self.copytextbtn.clicked.connect(self.copytext)
        self.pastetextbtn.clicked.connect(self.pastetext)
        self.copyHTMLbtn.clicked.connect(self.copyHTML)
        self.pasteHTMLbtn.clicked.connect(self.pasteHTML)
        self.copyimagebtn.clicked.connect(self.copyimage)
        self.pasteimagebtn.clicked.connect(self.pasteimage)

    def copytext(self):
        clipboard = QApplication.clipboard()
        clipboard.setText('hello world')

    def pastetext(self):
        clipboard = QApplication.clipboard()
        self.textlabel.setText(clipboard.text())

    def copyHTML(self):
        mimedata = QMimeData()
        mimedata.setHtml('<b>bold and<font color=red>Red</font></b>')
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mimedata)

    def pasteHTML(self):
        clipboard = QApplication.clipboard()
        mimedata = clipboard.mimeData()
        if mimedata.hasHtml():
            self.textlabel.setText(mimedata.html())

    def copyimage(self):
        clipboard = QApplication.clipboard()
        clipboard.setPixmap(QPixmap('../Image/图标.jpg'))

    def pasteimage(self):
        clipboard = QApplication.clipboard()
        self.imagelabel.setPixmap(clipboard.pixmap())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ClipBoard()
    w.show()
    sys.exit(app.exec_())
