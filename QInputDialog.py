import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QFormLayout, QApplication, QInputDialog


class InputDialog(QWidget):
    def __init__(self):
        super(InputDialog, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QInputDailog输入对话框')
        formlayout = QFormLayout()

        self.btn_1 = QPushButton('获取列表中的选项')
        self.lineedit_1 = QLineEdit()
        self.btn_1.clicked.connect(self.getitem)
        formlayout.addRow(self.btn_1, self.lineedit_1)

        self.btn_2 = QPushButton('获取字符串')
        self.lineedit_2 = QLineEdit()
        self.btn_2.clicked.connect(self.gettext)
        formlayout.addRow(self.btn_2, self.lineedit_2)

        self.btn_3 = QPushButton('获取整数')
        self.lineedit_3 = QLineEdit()
        self.btn_3.clicked.connect(self.getint)
        formlayout.addRow(self.btn_3, self.lineedit_3)

        self.setLayout(formlayout)

    def getitem(self):
        items = ['c', 'c++', 'python', 'java', 'ruby']
        item, ok = QInputDialog.getItem(self, '请选择编程语言', '语言列表', items)
        if item and ok:
            self.lineedit_1.setText(item)

    def gettext(self):
        text, ok = QInputDialog.getText(self, '请按要求输入内容', '姓名')
        if text and ok:
            self.lineedit_2.setText(text)

    def getint(self):
        num, ok = QInputDialog.getInt(self, '请按要求输入内容', '整数')
        if num and ok:
            self.lineedit_3.setText(str(num))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = InputDialog()
    w.show()
    sys.exit(app.exec_())