import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QTreeWidget, QHBoxLayout, QApplication, QWidget, QTreeWidgetItem


class BasicTreeWidget(QMainWindow):
    def __init__(self):
        super(BasicTreeWidget, self).__init__()
        self.setWindowTitle('树控件')
        self.resize(400, 300)
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        # 创建一个树控件
        tree = QTreeWidget()
        # 设置树控件的列数
        tree.setColumnCount(2)
        # 设置列的标签，跟表格其实是一样的
        tree.setHeaderLabels(['key', 'value'])
        root = QTreeWidgetItem()
        root.setText(0, '根节点')
        root.setIcon(0, QIcon('../Image/new_dir.jpg'))
        tree.addTopLevelItem(root)
        childitem = QTreeWidgetItem(root)
        childitem.setText(0, '子节点')
        childitem.setText(1, '字节的的值')
        childitem.setCheckState(0, Qt.Unchecked)
        root.addChild(childitem)


        hbox = QHBoxLayout()
        hbox.addWidget(tree)

        centralWidget.setLayout(hbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = BasicTreeWidget()
    w.show()
    sys.exit(app.exec_())