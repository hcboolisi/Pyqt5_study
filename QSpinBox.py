import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QSpinBox, QVBoxLayout, QApplication, QLineEdit
from PyQt5.QtCore import Qt


class SpinBox(QWidget):
    def __init__(self):
        super(SpinBox, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('SpinBox计数器控件')

        self.label = QLabel('当前值')
        self.label.setFont(QFont('Arial', 15, 20, True))
        self.label.setAlignment(Qt.AlignCenter)

        self.sb = QSpinBox()
        # self.sb.setMaximum(100)
        # self.sb.setMinimum(0)
        self.sb.setRange(0, 100)
        self.sb.setSingleStep(5)
        self.sb.setValue(15)
        self.sb.setFont(QFont('Arial', 15, 20, True))

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.sb)

        self.sb.valueChanged.connect(self.valuechange)

        self.resize(300, 100)
        self.setLayout(vbox)

    def valuechange(self):
        sender = self.sender()
        # self.label.setText(f'当前值：{sender.value()}')
        self.label.setText('当前值：' + str(sender.value()))
        self.label.setFont(QFont('Arial', 15, 20, True))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = SpinBox()
    w.show()
    sys.exit(app.exec_())