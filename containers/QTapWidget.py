import sys

from PyQt5.QtWidgets import QTabWidget, QWidget, QApplication, QFormLayout, QLineEdit, QHBoxLayout, QRadioButton, \
    QLabel, QCheckBox


class TapWidget(QTabWidget):
    def __init__(self):
        super(TapWidget, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('选项卡控件')

        self.tap1 = QWidget()
        self.tap2 = QWidget()
        self.tap3 = QWidget()

        self.addTab(self.tap1, '选项卡1')
        self.addTab(self.tap2, '个人信息')
        self.addTab(self.tap3, '选项卡3')

        self.tap1UI()
        self.tap2UI()
        self.tap3UI()

    def tap1UI(self):
        form = QFormLayout()
        form.addRow('姓名', QLineEdit())
        form.addRow('地址', QLineEdit())
        self.setTabText(0, '联系方式')
        self.tap1.setLayout(form)

    def tap2UI(self):
        form = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton('男'))
        sex.addWidget(QRadioButton('女'))
        form.addRow('性别', sex)
        form.addRow('生日', QLineEdit())
        self.tap2.setLayout(form)

    def tap3UI(self):
        Hbox = QHBoxLayout()
        Hbox.addWidget(QLabel('科目'))
        Hbox.addWidget(QCheckBox('初中'))
        Hbox.addWidget(QCheckBox('高中'))
        Hbox.addWidget(QCheckBox('本科'))
        self.setTabText(2, '教育程度')
        self.tap3.setLayout(Hbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = TapWidget()
    w.show()
    sys.exit(app.exec_())