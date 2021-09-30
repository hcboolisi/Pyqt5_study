import sys

from PyQt5.QtWidgets import *


class MdiWindow(QMainWindow):
    count = 0

    def __init__(self):
        super(MdiWindow, self).__init__()

        self.setWindowTitle('多文档窗口QMidWindow')

        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        bar = self.menuBar()
        file = bar.addMenu('file')
        file.addAction("New")
        file.addAction("cascade")
        file.addAction('Tiled')

        file.triggered.connect(self.windowaction)

    def windowaction(self, e):
        if e.text() == "New":
            MdiWindow.count += 1
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle('子窗口 ' + str(MdiWindow.count))
            self.mdi.addSubWindow(sub)
            sub.show()
        elif e.text() == "cascade":
            self.mdi.cascadeSubWindows()  # 设置层叠子窗口
        elif e.text() == "Tiled":
            self.mdi.tileSubWindows()  # 设置平铺子窗口


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MdiWindow()
    w.show()
    sys.exit(app.exec_())