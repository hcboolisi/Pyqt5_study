import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QVBoxLayout, QWidget
from CommonHelper import CommonHelper


class LoadQSS(QMainWindow):
    def __init__(self, parent=None):
        super(LoadQSS, self).__init__(parent)
        self.resize(477, 258)
        self.setWindowTitle('加载QSS文件')

        btn = QPushButton()
        btn.setText('加载QSS文件')
        btn.setToolTip('点击加载QSS文件')
        btn.clicked.connect(self.onClick)

        vbx = QVBoxLayout()
        vbx.addWidget(btn)

        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(vbx)

        self.setLayout(vbx)

    def onClick(self):
        styleFile = './style.qss'
        qssFile = CommonHelper.readQSS(styleFile)
        win.setStyleSheet(qssFile)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LoadQSS()
    win.show()
    sys.exit(app.exec_())