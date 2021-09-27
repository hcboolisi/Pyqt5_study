import sys

from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, \
    QHBoxLayout, QTreeWidget, QApplication, QTreeWidgetItem, QInputDialog, QMessageBox


class ModifyTree(QMainWindow):
    def __init__(self):
        super(ModifyTree, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('树控件的增，删，改')
        self.resize(400, 300)
        centerwidget = QWidget()
        self.setCentralWidget(centerwidget)

        hbox = QHBoxLayout()
        self.btn1 = QPushButton('增加节点')
        self.btn2 = QPushButton('删除节点')
        self.btn3 = QPushButton('修改节点')
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)
        hbox.addWidget(self.btn3)

        self.tree = QTreeWidget()
        self.tree.setColumnCount(2)
        self.tree.setHeaderLabels(['Key', 'Value'])

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.tree)

        centerwidget.setLayout(vbox)

        self.btn1.clicked.connect(self.addTreeItem)
        self.btn2.clicked.connect(self.deleteTreeItem)
        self.btn3.clicked.connect(self.updateTreeItem)

    def addTreeItem(self):
        print('添加节点')
        if self.tree.selectedItems():
            currentitem = self.tree.currentItem()
            NewItem = QTreeWidgetItem(currentitem)
            NewItem.setText(0, '新节点')
            NewItem.setText(1, '新值')
        else:
            NewItem = QTreeWidgetItem(self.tree)
            NewItem.setText(0, '新节点')
            NewItem.setText(1, '新值')

    def deleteTreeItem(self):
        currentitem = self.tree.currentItem()
        root = self.tree.invisibleRootItem()  # 实列化最底层隐形的root根节点（删除顶级节点的时候用，是所有顶级节点的根节点）
        if currentitem:
            for currentitem in self.tree.selectedItems():
                (currentitem.parent() or root).removeChild(currentitem)  # 通过自己的父节点来删除自己

    def updateTreeItem(self):
        currentitem = self.tree.currentItem()
        try:
            if currentitem:
                text1, ok = QInputDialog.getText(self, '请按要求输入内容', 'Key')
                if text1 and ok:   # 存在一个BUG，如果选cancel的话，程序会出错，自动退出.但是用Try可以解决问题
                    Key = text1
                text2, ok = QInputDialog.getText(self, '请按要求输入内容', 'Value')
                if text1 and ok:
                    Value = text2
                currentitem.setText(0, str(Key))
                currentitem.setText(1, str(Value))
            else:
                QMessageBox.warning(None, '警告', '请选择需要修改的项目', QMessageBox.Ok)
        except:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ModifyTree()
    w.show()
    sys.exit(app.exec_())
