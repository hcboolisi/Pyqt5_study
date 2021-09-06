import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

def onclick_button():
    print('1')
    print('widget.x() = %d' % widget.x())
    print('widget.y() = %d' % widget.y())
    print('widget.width() = %d' % widget.width())
    print('widget.height() = %d' % widget.height())

    print('2')
    print('widget.geometry().x() = %d' % widget.geometry().x())
    print('widget.geometry().y() = %d' % widget.geometry().y())
    print('widget.geometry().width() = %d' % widget.geometry().width())
    print('widget.geometry().height() = %d' % widget.geometry().height())

    print('3')
    print(' widget.frameGeometry().x() = %d' % widget.frameGeometry().x())
    print(' widget.frameGeometry().y() = %d' % widget.frameGeometry().y())
    print(' widget.frameGeometry().width() = %d' % widget.frameGeometry().width())
    print(' widget.frameGeometry().height() = %d' % widget.frameGeometry().height())


app = QApplication(sys.argv)
widget = QWidget()

widget.setWindowTitle("屏幕坐标系")
widget.resize(800, 600)
widget.move(250, 200)

btn = QPushButton(widget)
btn.setText('按钮')
btn.move(25, 50)
btn.clicked.connect(onclick_button)

widget.show()

sys.exit(app.exec_())



