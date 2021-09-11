import sys

from PyQt5.QtWidgets import QMainWindow, QPushButton, QDialog, QApplication
from PyQt5.QtCore import Qt

class Dialog(QMainWindow):
    def __init__(self):
        super(Dialog, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('对话框')
        self.resize(300, 200)
        self.btn = QPushButton(self)
        self.btn.setText('打开对话框')
        self.btn.move(50, 50)
        self.btn.clicked.connect(self.showdialog)

    def showdialog(self):
        dialog = QDialog()
        dialog.setWindowTitle("对话框")
        btn = QPushButton('确定', dialog)
        btn.move(50, 50)
        btn.clicked.connect(dialog.close)
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Dialog()
    w.show()
    sys.exit(app.exec_())