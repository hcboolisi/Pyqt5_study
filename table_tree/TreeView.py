import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QTreeView, QWidget, QVBoxLayout, QDirModel


class TreeView(QMainWindow):
    def __init__(self):
        super(TreeView, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('树视图控件')
        self.resize(800, 600)
        centerwidget = QWidget()
        self.setCentralWidget(centerwidget)

        Vbox = QVBoxLayout()

        model = QDirModel()

        self.treeview = QTreeView()
        self.treeview.setModel(model)

        Vbox.addWidget(self.treeview)
        centerwidget.setLayout(Vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = TreeView()
    w.show()
    sys.exit(app.exec_())
