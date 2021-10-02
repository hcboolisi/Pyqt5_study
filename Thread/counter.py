import sys

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import *

sec = 0


# 定义一个工作线程类，继承自QThread
class WorkThread(QThread):
    # 自定义两个信号
    timeout = pyqtSignal()  # 该信号用来每隔一段时间发送一次
    timeShot = pyqtSignal()  # 该信号用来最后时间完成时发送一次

    def run(self):
        # 定义一个死循环
        while True:
            self.sleep(1)  # 设置休眠时间为1秒
            if sec == 5:  # 如果时间等于5秒的时候，触发timeShot信号
                self.timeShot.emit()
                break  # 触发完后，退出循环
            self.timeout.emit()  # 间隔1秒，每循环一次触发一次timeout信号。


class Counter(QMainWindow):
    def __init__(self):
        super(Counter, self).__init__()
        self.setWindowTitle('使用多线程时间计数器功能')
        self.resize(300, 120)

        center = QWidget()
        self.setCentralWidget(center)

        self.lcd = QLCDNumber()
        self.btn = QPushButton('开始计数')

        vbox = QVBoxLayout()
        vbox.addWidget(self.lcd)
        vbox.addWidget(self.btn)

        center.setLayout(vbox)

        self.workThread = WorkThread()
        self.workThread.timeout.connect(self.countTime)
        self.workThread.timeShot.connect(self.end)
        self.btn.clicked.connect(self.start)

    def countTime(self):
        global sec
        sec += 1
        self.lcd.display(sec)

    def end(self):
        QMessageBox.information(None, '消息', '计数结束', QMessageBox.Ok)

    def start(self):
        self.workThread.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Counter()
    w.show()
    sys.exit(app.exec_())