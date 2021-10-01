import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class ScrollBar(QMainWindow):
    def __init__(self):
        super(ScrollBar, self).__init__()

        self.setWindowTitle('QScrollBar滚动条')
        self.resize(300, 400)

        hbox = QHBoxLayout()

        self.label = QLabel('拖动滚动条控制文本的颜色')

        self.scroll1 = QScrollBar()
        # self.scroll1.setOrientation(Qt.Horizontal)  # 设置为水平方向
        self.scroll1.setMaximum(255)
        self.scroll1.sliderMoved.connect(self.slider)

        self.scroll2 = QScrollBar()
        self.scroll2.setMaximum(255)
        self.scroll2.sliderMoved.connect(self.slider)

        self.scroll3 = QScrollBar()
        self.scroll3.setMaximum(255)
        self.scroll3.sliderMoved.connect(self.slider)

        self.scroll4 = QScrollBar()
        self.scroll4.setMaximum(255)
        self.scroll4.sliderMoved.connect(self.slider_pos)

        hbox.addWidget(self.label)
        hbox.addWidget(self.scroll1)
        hbox.addWidget(self.scroll2)
        hbox.addWidget(self.scroll3)
        hbox.addWidget(self.scroll4)

        centerwidget = QWidget()
        self.setCentralWidget(centerwidget)
        centerwidget.setLayout(hbox)

        self.y = self.label.pos().y()

    def slider(self):
        print(self.scroll1.value(), self.scroll2.value(), self.scroll3.value())
        palette = QPalette()
        color = QColor(self.scroll1.value(), self.scroll2.value(), self.scroll3.value(), 255)
        palette.setColor(QPalette.Foreground, color)
        self.label.setPalette(palette)

    def slider_pos(self):
        self.label.move(self.label.x(), self.y + self.scroll4.value())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ScrollBar()
    w.show()
    sys.exit(app.exec_())