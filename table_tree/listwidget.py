import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QMessageBox


class ListWidget(QMainWindow):
    def __init__(self):
        super(ListWidget, self).__init__()
        self.setWindowTitle('ListWidget列表扩展控件')
        self.listwidget = QListWidget()
        self.listwidget.addItems(['项目1', '项目2', '项目3', '项目4'])
        self.listwidget.itemClicked.connect(self.clicked)
        self.setCentralWidget(self.listwidget)

    # 两种方式效果是一样的，感觉第一种绕了一个圈又回来了。先得到索引，再用索引得到item对象，其实点击以后传过来的就是一个item对象。
    def clicked(self, index):
        # QMessageBox.information(self, '提示', '你点击的按钮是:' + self.listwidget.item(self.listwidget.row(index)).text())
        QMessageBox.information(self, '提示', '你点击的按钮是:' + index.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ListWidget()
    w.show()
    sys.exit(app.exec_())