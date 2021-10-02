import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWebEngineWidgets import *


class WebEngineView(QMainWindow):
    def __init__(self):
        super(WebEngineView, self).__init__()
        self.setWindowTitle('加载本地页面')
        self.resize(800, 600)

        self.browser = QWebEngineView()
        # 直接在代码中加载HTML代码
        self.browser.setHtml('''<!DOCTYPE html>
                                <html lang="en">
                                <head>
                                    <meta charset="UTF-8">
                                    <title>自定义的web界面</title>
                                </head>
                                <body>
                                    <h1>Hello PyQt5</h1>
                                    <h2>Hello World</h2>
                                    <h3>Hello Python</h3>
                                </body>
                                </html>''')
        self.setCentralWidget(self.browser)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = WebEngineView()
    w.show()
    sys.exit(app.exec_())