import os
import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWebEngineWidgets import *


class WebEngineView(QMainWindow):
    def __init__(self):
        super(WebEngineView, self).__init__()
        self.setWindowTitle('加载本地页面')
        self.resize(800, 600)

        url = os.getcwd() + '/LocalHTML.html'  # 获得当前文件路径，加上文件名组成一个本地文件的url地址
        self.browser = QWebEngineView()
        self.browser.load(QUrl.fromLocalFile(url))  # 加载本地网页与加载外部网页的区别
        self.setCentralWidget(self.browser)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = WebEngineView()
    w.show()
    sys.exit(app.exec_())