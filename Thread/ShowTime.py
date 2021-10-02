import sys

from PyQt5.QtCore import QTimer, Qt, QDateTime
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QGridLayout, QApplication, QWidget


class ShowTime(QMainWindow):
    def __init__(self):
        super(ShowTime, self).__init__()

        self.setWindowTitle('显示时间')
        self.resize(300, 200)

        grid = QGridLayout()

        self.label = QLabel('显示时间')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('Arial', 10, 50))

        self.btn1 = QPushButton('开  始')
        self.btn2 = QPushButton('停  止')
        self.btn2.setEnabled(False)

        self.timer = QTimer()
        self.timer.timeout.connect(self.showtime)

        grid.addWidget(self.label, 0, 0, 1, 2)
        grid.addWidget(self.btn1, 1, 0, 1, 1)
        grid.addWidget(self.btn2, 1, 1, 1, 1)

        center = QWidget()
        self.setCentralWidget(center)
        center.setLayout(grid)

        self.btn1.clicked.connect(self.start)
        self.btn2.clicked.connect(self.stop)

    def showtime(self):
        time = QDateTime.currentDateTime()  # 获得当前时间
        self.label.setText(time.toString('yyyy/MM/dd HH:mm:ss dddd'))

    def start(self):
        self.timer.start(1000)  # 开始计时器，间隔时间1秒
        self.btn1.setEnabled(False)
        self.btn2.setEnabled(True)

    def stop(self):
        self.timer.stop()  # 停止计时器
        self.btn1.setEnabled(True)
        self.btn2.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ShowTime()
    w.show()
    sys.exit(app.exec_())