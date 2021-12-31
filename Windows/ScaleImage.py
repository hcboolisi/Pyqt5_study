import sys

from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QVBoxLayout


class ScaleImage(QWidget):
    def __init__(self):
        super(ScaleImage, self).__init__()
        self.setWindowTitle('设置图片缩放')

        filename = '../Image_1/5.jpg'
        img = QImage(filename)

        label = QLabel(self)
        label.setFixedSize(300, 400)

        result = img.scaled(label.width(), label.height(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        # label.setPixmap(QPixmap.fromImage(result))
        label.setPixmap(QPixmap(result))

        vbx = QVBoxLayout()
        vbx.addWidget(label)
        self.setLayout(vbx)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ScaleImage()
    w.show()
    sys.exit(app.exec_())