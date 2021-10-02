import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWebEngineWidgets import *


class WebEngineView(QMainWindow):
    def __init__(self):
        super(WebEngineView, self).__init__()
        self.setWindowTitle('QWebEngineView打开外部网页')
        self.resize(800, 600)

        self.browser = QWebEngineView()
        self.browser.load(QUrl('https://study.163.com/'))
        self.setCentralWidget(self.browser)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = WebEngineView()
    w.show()
    sys.exit(app.exec_())