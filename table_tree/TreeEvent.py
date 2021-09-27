import sys

from PyQt5.QtWidgets import QMainWindow, QWidget, QTreeWidget, QTreeWidgetItem, \
                             QApplication, QVBoxLayout


class TreeEvent(QMainWindow):
    def __init__(self):
        super(TreeEvent, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('树控件点击事件')
        self.resize(400, 300)

        self.centerwidget = QWidget()
        self.setCentralWidget(self.centerwidget)

        self.tree = QTreeWidget(self.centerwidget)
        self.tree.setColumnCount(2)
        self.tree.setHeaderLabels(['Key', 'Value'])
        self.tree.setColumnWidth(0, 120)

        item1 = QTreeWidgetItem()
        item1.setText(0, '项目1')
        item1.setText(1, '1')

        item2 = QTreeWidgetItem()
        item2.setText(0, '项目2')
        item2.setText(1, '2')

        item3 = QTreeWidgetItem()
        item3.setText(0, '项目3')
        item3.setText(1, '3')

        self.tree.addTopLevelItems([item1, item2, item3])

        item2_1 = QTreeWidgetItem(item2)
        item2_1.setText(0, '项目2的子项1')
        item2_1.setText(1, '11')

        item2_2 = QTreeWidgetItem(item2)
        item2_2.setText(0, '项目2的子项2')
        item2_2.setText(1, '22')

        item2_3 = QTreeWidgetItem(item2)
        item2_3.setText(0, '项目2的子项3')
        item2_3.setText(1, '33')
        # item2.addChildren([item2_1,item2_2,item2_3])

        self.tree.clicked.connect(self.tree_event)

        vbox = QVBoxLayout()
        vbox.addWidget(self.tree)
        self.centerwidget.setLayout(vbox)

    def tree_event(self, index):
        item = self.tree.currentItem()
        print(index.row())
        print('Key = %s, Vale = %s' % (item.text(0), item.text(1)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = TreeEvent()
    w.show()
    sys.exit(app.exec_())