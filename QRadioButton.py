import sys

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QRadioButton, QApplication


class RadioButton(QWidget):
    def __init__(self):
        super(RadioButton, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('RadioButton单选框按钮')
        hbox = QHBoxLayout()
        rb_1 = QRadioButton()
        rb_1.setText('单选框1')
        rb_1.setChecked(True)

        rb_2 = QRadioButton('单选框2')

        hbox.addWidget(rb_1)
        hbox.addWidget(rb_2)

        self.setLayout(hbox)
        rb_1.toggled.connect(self.ButtonState)
        rb_2.toggled.connect(self.ButtonState)

    def ButtonState(self):
        radiobutton = self.sender()
        if radiobutton.isChecked() == True:
            print('<'+radiobutton.text()+'> 被选中')
        else:
            print('<'+radiobutton.text()+'> 被取消选中')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = RadioButton()
    w.show()
    sys.exit(app.exec_())
