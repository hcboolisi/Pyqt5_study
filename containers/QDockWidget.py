import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class DockWidget(QMainWindow):
    def __init__(self):
        super(DockWidget, self).__init__()

        self.setWindowTitle('QDockWidget停靠控件')
        self.resize(800, 600)

        self.dock = QDockWidget('dockwidget', self)

        self.listbox = QListWidget()
        self.listbox.addItem('项目1')
        self.listbox.addItem('项目2')
        self.listbox.addItem('项目3')

        self.dock.setWidget(self.listbox)  # 将列表窗口绑定再停靠窗口上
        self.setCentralWidget(QTextEdit())  # 设置主窗口的中心窗口为一个多行文本窗口，如果不设置中心窗口，则只能停靠再整个主窗口上

        self.dock.setFloating(True)  # 设置Dock窗口默认漂浮

        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)  # 将Dock窗口绑定到主窗口中，并设置默认停靠位置为靠右停靠


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = DockWidget()
    w.show()
    sys.exit(app.exec_())