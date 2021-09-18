import sys

from PyQt5.QtCore import QDir
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit, QApplication, QFileDialog, QLabel


class FileDialog(QWidget):
    def __init__(self):
        super(FileDialog, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QFileDialog文件对话框')
        vbox = QVBoxLayout()

        self.btn = QPushButton('加载图片')
        self.label = QLabel()

        self.btn_1 = QPushButton('加载文本')
        self.textedit = QTextEdit()
        self.textedit.setReadOnly(True)  # 设置不可以编辑

        self.btn.clicked.connect(self.loadimage)
        self.btn_1.clicked.connect(self.loadtext)

        vbox.addWidget(self.btn)
        vbox.addWidget(self.label)
        vbox.addWidget(self.btn_1)
        vbox.addWidget(self.textedit)

        self.setLayout(vbox)

    def loadimage(self):
        frame, _ = QFileDialog.getOpenFileName(self, '打开文件', '.', '图像文件(*.jpg *.png)')
        self.label.setPixmap(QPixmap(frame))

    def loadtext(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)  # 设置文件模式，任何文件
        dialog.setFilter(QDir.Files)  # 设置文件过滤
        if dialog.exec():
            filenames = dialog.selectedFiles()
            with open(filenames[0], 'r', encoding='UTF-8') as f:  # 编码模式加上去，不然可能会错误，没加编码模式一直闪退
                                                                  # 多次测试后发现，报错illegal multibyte sequence
                date = f.read()
                self.textedit.setText(date)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = FileDialog()
    w.show()
    sys.exit(app.exec_())