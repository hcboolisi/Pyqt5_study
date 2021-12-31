import sys

from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QWidget, QLabel, QApplication
from PyQt5.QtCore import Qt


class LodingGif(QWidget):
    def __init__(self):
        super(LodingGif, self).__init__()
        self.label = QLabel("", self)  # 创建一个label对象
        self.setFixedSize(640, 640)   # 设置窗口的填充尺寸为640*640
        self.setWindowFlags(Qt.Dialog | Qt.CustomizeWindowHint)  # 设置窗口标记为对话框和无边框
        self.movie = QMovie('../Image/加载.gif')  # 创建一个movie对象，后面跟路径
        self.label.setMovie(self.movie)  # 设置label的movie为movie对象。
        self.movie.start()  # 调用movie对象的start方法开启电影


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = LodingGif()
    w.show()
    sys.exit(app.exec_())