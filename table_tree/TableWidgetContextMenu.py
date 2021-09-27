import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QTableWidget, QApplication, QVBoxLayout, QMenu


class TableWidgetContextMenu(QWidget):
    def __init__(self):
        super(TableWidgetContextMenu, self).__init__()
        self.setWindowTitle('显示上下文菜单')
        self.resize(450, 400)

        self.tablewidget = QTableWidget(4, 3)
        self.tablewidget.setHorizontalHeaderLabels(['姓名', '年级', '分数'])

        self.tablewidget.setItem(0, 0, QTableWidgetItem('关羽'))
        self.tablewidget.setItem(0, 1, QTableWidgetItem('一年级'))
        self.tablewidget.setItem(0, 2, QTableWidgetItem('80'))

        self.tablewidget.setItem(1, 0, QTableWidgetItem('张飞'))
        self.tablewidget.setItem(1, 1, QTableWidgetItem('二年级'))
        self.tablewidget.setItem(1, 2, QTableWidgetItem('70'))

        self.tablewidget.setItem(2, 0, QTableWidgetItem('赵云'))
        self.tablewidget.setItem(2, 1, QTableWidgetItem('三年级'))
        self.tablewidget.setItem(2, 2, QTableWidgetItem('88'))

        self.tablewidget.setItem(3, 0, QTableWidgetItem('马超'))
        self.tablewidget.setItem(3, 1, QTableWidgetItem('一年级'))
        self.tablewidget.setItem(3, 2, QTableWidgetItem('75'))

        vbox = QVBoxLayout(self)
        vbox.addWidget(self.tablewidget)

        self.tablewidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tablewidget.customContextMenuRequested.connect(self.generateMune)

    def generateMune(self, pos):
        print(pos)

        for i in self.tablewidget.selectionModel().selection().indexes():
            rowNum = i.row()
            if rowNum < 2:
                menu = QMenu()
                item1 = menu.addAction('第一个功能')
                item2 = menu.addAction('第二个功能')
                item3 = menu.addAction('第三个功能')

                # pos是窗口内坐标，通过下面的功能将点击的坐标转换为全屏坐标
                screenpos = self.tablewidget.mapToGlobal(pos)
                print(screenpos)
                action = menu.exec(screenpos)
                if action == item1:
                    print('你选择了：' + item1.text())
                elif action == item2:
                    print('你选择了：' + item2.text())
                elif action == item3:
                    print('你选择了：' + item3.text())
                return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = TableWidgetContextMenu()
    w.show()
    sys.exit(app.exec())