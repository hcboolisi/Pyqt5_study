import os
import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class PyQtCallJs(QMainWindow):
    def __init__(self):
        super(PyQtCallJs, self).__init__()
        self.setWindowTitle('PyQt5调用JavaScript')
        self.resize(800, 600)

        vbox = QVBoxLayout()
        self.browser = QWebEngineView()
        url = os.getcwd() + '/text.html'
        self.browser.load(QUrl.fromLocalFile(url))

        self.btn = QPushButton('设置全名')
        self.btn.clicked.connect(self.fullname)

        vbox.addWidget(self.browser)
        vbox.addWidget(self.btn)

        center = QWidget()
        center.setLayout(vbox)
        self.setCentralWidget(center)

    def js_callback(self, result):
        print(result)

    def fullname(self):
        self.value = 'Hello World'
        self.browser.page().runJavaScript('fullName("' + self.value + '");', self.js_callback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = PyQtCallJs()
    w.show()
    sys.exit(app.exec_())