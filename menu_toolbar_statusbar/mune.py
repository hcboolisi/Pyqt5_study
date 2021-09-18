import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QMenu


class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('菜单栏设置')
        self.resize(400, 300)

        menubar = self.menuBar()
        file = menubar.addMenu('文件')
        file.addAction('新建')

        opn = file.addMenu('打开')  # 如果要加弹出来的子菜单，那么这个不能用QAction，只能用QMenu。
        n1 = QAction('打开1', self)
        n2 = QAction('打开2', self)
        opn.addAction(n1)
        opn.addSeparator()
        opn.addAction(n2)

        file.addSeparator()

        save = QAction('保存', self)
        save.setShortcut('Ctrl + s')
        file.addAction(save)
        save.triggered.connect(self.process)

        edit = menubar.addMenu('编辑')
        edit.addAction('复制')
        edit.addAction('粘贴')
        quit_1 = QAction('退出', self)
        edit.addAction(quit_1)

        view = menubar.addMenu('视图')
        view.addAction('查看')

    def process(self):
        sender = self.sender()
        print(sender.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Menu()
    w.show()
    sys.exit(app.exec_())