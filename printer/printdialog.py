import sys

from PyQt5.QtPrintSupport import QPrinter, QPageSetupDialog, QPrintDialog
from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QPushButton, QFileDialog,QDialog


class PrintDialog(QWidget):
    def __init__(self):
        super(PrintDialog, self).__init__()
        self.printer = QPrinter()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('打印对话框')
        self.resize(500, 400)

        self.editer = QTextEdit(self)
        self.editer.setGeometry(20, 20, 300, 270)

        self.openbutton = QPushButton('打开文件', self)
        self.openbutton.move(350, 20)
        self.openbutton.clicked.connect(self.openfile)

        self.settingsbutton = QPushButton('打印设置', self)
        self.settingsbutton.move(350, 50)
        self.settingsbutton.clicked.connect(self.printsetting)

        self.printbutton = QPushButton('打印文档', self)
        self.printbutton.move(350, 80)
        self.printbutton.clicked.connect(self.printfile)

    def openfile(self):
        frame = QFileDialog.getOpenFileName(self, '打开文件夹', './')
        if frame[0]:
            with open(frame[0], 'r', encoding='utf-8', errors='ignore') as f:
                self.editer.setText(f.read())

    def printsetting(self):
        printsetting = QPageSetupDialog(self.printer, self)
        printsetting.exec()

    def printfile(self):
        printdialog = QPrintDialog(self.printer, self)
        if QDialog.Accepted == printdialog.exec():
            self.editer.print(self.printer)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = PrintDialog()
    w.show()
    sys.exit(app.exec_())