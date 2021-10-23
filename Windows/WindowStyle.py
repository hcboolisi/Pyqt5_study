import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QHBoxLayout, QApplication, QStyleFactory


class WindowStyle(QWidget):
    def __init__(self):
        super(WindowStyle, self).__init__()
        self.setWindowTitle('设置窗口控件风格')
        self.resize(250, 150)

        self.label = QLabel("设置窗口控件风格")
        self.label.setFont(QFont('Arial', 15))
        self.combobox = QComboBox()
        self.combobox.addItems(QStyleFactory.keys())
        self.combobox.setFont(QFont('Arial', 15))

        # 获取当前窗口风格
        index = self.combobox.findText(QApplication.style().objectName(), QtCore.Qt.MatchFixedString)

        # 设置当前下拉框显示当前得窗口风格类型
        self.combobox.setCurrentIndex(index)

        hbox = QHBoxLayout()
        hbox.addWidget(self.label)
        hbox.addWidget(self.combobox)

        self.setLayout(hbox)

        self.combobox.activated[str].connect(self.setStyle)

    def setStyle(self, style):
        print(style)
        QApplication.setStyle(style)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = WindowStyle()
    w.show()
    sys.exit(app.exec_())
