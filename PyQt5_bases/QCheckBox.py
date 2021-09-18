import sys

from PyQt5.QtWidgets import QWidget, QCheckBox, QHBoxLayout, QApplication
from PyQt5.QtCore import Qt


class CheckBox(QWidget):
    def __init__(self):
        super(CheckBox, self).__init__(parent=None)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('CheckBox复选框')
        self.cb_1 = QCheckBox('复选框1')
        self.cb_1.setChecked(True)  # 设置后，True默认状态为选中状态

        self.cb_2 = QCheckBox('复选框2')

        self.cb_3 = QCheckBox('复选框3（半选中）')
        self.cb_3.setTristate(True)  # 设置复选框为一个三态复选框
        self.cb_3.setCheckState(Qt.PartiallyChecked)  # 设置半选中状态，设置后，默认状态未半选中状态

        hbox = QHBoxLayout()
        hbox.addWidget(self.cb_1)
        hbox.addWidget(self.cb_2)
        hbox.addWidget(self.cb_3)

        self.cb_1.stateChanged.connect(self.checkstate)
        self.cb_2.stateChanged.connect(self.checkstate)
        self.cb_3.stateChanged.connect(self.checkstate)

        self.setLayout(hbox)

    def checkstate(self):  # def checkstate(self, cb):
        # print(cb.text() + '   ischecked = ' + str(cb.isChecked()) + '   checksate = ' + str(cb.checkState()))
        checkstatus_1 = self.cb_1.text() + '  ischecked = ' + str(self.cb_1.isChecked()) + \
                        '  checksate = ' + str(self.cb_1.checkState()) + '\n'
        checkstatus_2 = self.cb_2.text() + '  ischecked = ' + str(self.cb_2.isChecked()) + \
                        '  checksate = ' + str(self.cb_2.checkState()) + '\n'
        checkstatus_3 = self.cb_3.text() + '  ischecked = ' + str(self.cb_3.isChecked()) + \
                        '  checksate = ' + str(self.cb_3.checkState()) + '\n'
        print(checkstatus_1 + checkstatus_2 + checkstatus_3)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CheckBox()
    w.show()
    sys.exit(app.exec_())