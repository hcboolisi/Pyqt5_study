import sys

from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListView, QApplication, QMessageBox


class ListView(QWidget):
    def __init__(self):
        super(ListView, self).__init__()
        self.setWindowTitle('列表视图')

        vbox = QVBoxLayout()

        listmodel = QStringListModel()

        listview = QListView()
        listview.setModel(listmodel)

        self.ls = ['项目1', '项目2', '项目3', '项目4']
        listmodel.setStringList(self.ls)

        vbox.addWidget(listview)
        self.setLayout(vbox)

        listview.clicked.connect(self.clicked)

    def clicked(self, item):
        QMessageBox.information(self, '提示', '你点击的项目是' + self.ls[item.row()])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ListView()
    w.show()
    sys.exit(app.exec_())