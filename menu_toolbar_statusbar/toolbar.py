import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction


class ToolBar(QMainWindow):
    def __init__(self):
        super(ToolBar, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('工具栏')
        self.resize(400, 300)

        # 创建工具栏要使用addtoolbar。
        toolbar = self.addToolBar('第一个工具栏')
        btn1 = toolbar.addAction(QIcon('../Image/new_file.jpg'), '新建')

        # 注意如果要用QAction的话，一定要加一个放置位置，self代表toolbar自己，也可以直接使用toolbar
        new_dir = QAction(QIcon('../Image/new_dir.jpg'), '新建文件夹', self)
        toolbar.addAction(new_dir)

        # 设置toolbar按钮图标文本的显示方式，在图标下面或者在图标侧面，默认不显示，作为提示语显示
        toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        toolbar_1 = self.addToolBar('第二个工具栏')
        toolbar_1.addAction(QIcon('../Image/save.jpg'), '保存')

        # 三种方式设置工具栏按钮点击事件
        # btn1.triggered.connect(self.clickevent)
        # new_dir.triggered.connect(lambda: self.click(new_dir))  # lambda 里面的函数传的参数是按钮自己
        toolbar.actionTriggered.connect(self.action)
        toolbar_1.actionTriggered.connect(self.action)

    def action(self, btn):
        print('单击的工具栏按钮是:' + btn.text())

    def clickevent(self):
        sender = self.sender()
        print('点击:' + sender.text())

    def click(self, e):
        print('点击：' + e.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ToolBar()
    w.show()
    sys.exit(app.exec_())