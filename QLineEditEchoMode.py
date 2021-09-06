import sys

from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QApplication


class LineEditEchoMode(QWidget):
    def __init__(self):
        super(LineEditEchoMode, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('LineEdit的回显模式')

        form_layout = QFormLayout()

        normallineedit = QLineEdit()
        noecholineedit = QLineEdit()
        passwordlineedit = QLineEdit()
        passwordechooneditlineedit = QLineEdit()

        form_layout.addRow('normal', normallineedit)
        form_layout.addRow('noecho', noecholineedit)
        form_layout.addRow('password', passwordlineedit)
        form_layout.addRow('passwordechoonedit', passwordechooneditlineedit)

        normallineedit.setPlaceholderText('normal模式的输入')
        noecholineedit.setPlaceholderText('NoEcho模式的输入')
        passwordlineedit.setPlaceholderText('正常的密码输入')
        passwordechooneditlineedit.setPlaceholderText('PasswordEchoOnEdit模式的输入')

        normallineedit.setEchoMode(QLineEdit.Normal)
        noecholineedit.setEchoMode(QLineEdit.NoEcho)
        passwordlineedit.setEchoMode(QLineEdit.Password)
        passwordechooneditlineedit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(form_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = LineEditEchoMode()
    w.show()
    sys.exit(app.exec_())