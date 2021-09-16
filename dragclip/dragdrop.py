import sys

from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QComboBox, QFormLayout, QApplication


class DragDrop(QWidget):
    def __init__(self):
        super(DragDrop, self).__init__()
        self.setWindowTitle('控件拖拽')
        label = QLabel('请将左边的内容拖到右边的下拉列表框中')

        self.lineedit = QLineEdit()
        self.lineedit.setDragEnabled(True)  # 设置LineEdit可拖动

        self.combox = ComBox()
        self.combox.setAcceptDrops(True)  # 设置下拉列表框可接受拖动放下的东西。

        form = QFormLayout()
        form.addRow(label)
        form.addRow(self.lineedit, self.combox)

        self.setLayout(form)


class ComBox(QComboBox):
    def __init__(self):
        super(ComBox, self).__init__()

    def dragEnterEvent(self, event):    # 当其他控件拖拽到下拉列表框drag事件侦测领域，范围内且鼠标还未放开的时候，
        if event.mimeData().hasText():  # 下来列表框的drag事件就会判断事件的扩展数据是否有文本内容，如果有
            event.accept()              # 那么下拉列表框的drag事件就调用接收方法接收内容
        else:
            event.ignore()              # 否则的话，drag事件就不管，不做任何操作。

    def dropEvent(self, event):
        self.addItem(event.mimeData().text())  # 当鼠标放开的时候，利用addItem方法将drop事件接受的扩展数据文本添加到下拉列表框中


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = DragDrop()
    w.show()
    sys.exit(app.exec_())