import sys

from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QApplication, QVBoxLayout


class ComboBox(QWidget):
    def __init__(self):
        super(ComboBox, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('ComboxBox下拉选项框')

        self.label = QLabel('请选择你要输入的语言')

        self.cb = QComboBox()
        self.cb.addItem('c')
        self.cb.addItem('c++')
        self.cb.addItems(['python', 'C#', 'php', 'HTML'])

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.cb)

        self.setLayout(vbox)
        self.resize(200, 50)
        self.cb.currentIndexChanged.connect(self.selectionindexitem)

    def selectionindexitem(self):
        self.label.setText(self.cb.currentText())
        self.label.adjustSize()
        for count in range(self.cb.count()):
            print('item ' + str(count) + ' = ' + self.cb.itemText(count))
        print('当前index：', self.cb.currentIndex(), 'selection changed', self.cb.currentText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ComboBox()
    w.show()
    sys.exit(app.exec_())
