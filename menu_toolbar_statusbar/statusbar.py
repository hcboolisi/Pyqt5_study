import sys

from PyQt5.QtWidgets import QMainWindow, QApplication


class StatusBar(QMainWindow):
    def __init__(self):
        super(StatusBar, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('状态栏')
        self.resize(400, 300)

        menubar = self.menuBar()
        file = menubar.addMenu('文件')
        file.addAction('打开')
        file.addAction('新建')

        save = file.addMenu('保存')
        save.addAction('保存1')

        savd2 = save.addMenu('保存2')
        savd2.addAction('123')
        savd2.addAction("456")

        menubar.triggered.connect(self.showstatus)

        self.status = self.statusBar()

    def showstatus(self, menu):
         if menu.text():
             self.status.showMessage('你点击的按钮是：' + menu.text(), 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = StatusBar()
    w.show()
    sys.exit(app.exec_())