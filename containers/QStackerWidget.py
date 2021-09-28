import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class StackedWidget(QWidget):
    def __init__(self):
        super(StackedWidget, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QStackedWidget堆栈窗口')

        self.listbox = QListWidget()
        item1 = QListWidgetItem()
        item1.setText('联系方式')
        item1.setTextAlignment(Qt.AlignCenter)
        item2 = QListWidgetItem()
        item2.setText('个人信息')
        item2.setTextAlignment(Qt.AlignCenter)
        item3 = QListWidgetItem()
        item3.setText('教育程度')
        item3.setTextAlignment(Qt.AlignCenter)
        self.listbox.addItem(item1)
        self.listbox.addItem(item2)
        self.listbox.addItem(item3)
        self.listbox.currentRowChanged.connect(self.change)

        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()

        self.tap1UI()
        self.tap2UI()
        self.tap3UI()

        self.stack = QStackedWidget()
        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)

        Hbox = QHBoxLayout()
        Hbox.addWidget(self.listbox)
        Hbox.addWidget(self.stack)

        self.setLayout(Hbox)

    def tap1UI(self):
        form = QFormLayout()
        form.addRow('姓名', QLineEdit())
        form.addRow('地址', QLineEdit())
        self.stack1.setLayout(form)

    def tap2UI(self):
        form = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton('男'))
        sex.addWidget(QRadioButton('女'))
        form.addRow('性别', sex)
        form.addRow('生日', QLineEdit())
        self.stack2.setLayout(form)

    def tap3UI(self):
        Hbox = QHBoxLayout()
        Hbox.addWidget(QLabel('科目'))
        Hbox.addWidget(QCheckBox('初中'))
        Hbox.addWidget(QCheckBox('高中'))
        Hbox.addWidget(QCheckBox('本科'))
        self.stack3.setLayout(Hbox)

    def change(self, index):
        self.stack.setCurrentIndex(index)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = StackedWidget()
    w.show()
    sys.exit(app.exec_())