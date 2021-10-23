import sys

from PyQt5.QtWidgets import QWidget, QComboBox, QApplication


class QSSSubContral(QWidget):
    def __init__(self):
        super(QSSSubContral, self).__init__()
        self.setWindowTitle('QSS子控件选择器')

        combox = QComboBox(self)
        combox.addItems(['', 'Windows', 'Linux', 'MacOS'])
        combox.setObjectName('myComboBox')

        combox.move(50, 50)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QSSSubContral()
    qssStyle = '''
        QComboBox#myComboBox::drop-down{
            image:url(../Image/图标.jpg)
        }
    '''
    w.setStyleSheet(qssStyle)
    w.show()
    sys.exit(app.exec_())