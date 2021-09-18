import sys

from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QGridLayout, QApplication


class LabelBuddy(QDialog):
    def __init__(self):
        super(LabelBuddy, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Label伙伴关系')

        name_label = QLabel('&Name')
        name_line_edit = QLineEdit()
        name_label.setBuddy(name_line_edit)

        pwd_label = QLabel('&PassWord', self)   # self 可要可不要，都可以运行
        pwd_line_edit = QLineEdit(self)
        pwd_label.setBuddy(pwd_line_edit)

        btnOK = QPushButton('&Ok')
        btnCancel = QPushButton('&Cancel')

        main_layout = QGridLayout()

        main_layout.addWidget(name_label, 0, 0)
        main_layout.addWidget(name_line_edit, 0, 1, 1, 2)
        main_layout.addWidget(pwd_label, 1, 0)
        main_layout.addWidget(pwd_line_edit, 1, 1, 1, 2)
        main_layout.addWidget(btnOK, 2, 1)
        main_layout.addWidget(btnCancel, 2, 2)

        self.setLayout(main_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = LabelBuddy()
    w.show()
    sys.exit(app.exec_())