import sys
import time

from PyQt5.QtCore import QThread, pyqtSignal, QDateTime, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog, QLineEdit, QApplication


class BackThread(QThread):
    update_date = pyqtSignal(str)

    def run(self):
        while True:
            date = QDateTime.currentDateTime()
            currenttime = date.toString('yyyy-MM-dd hh:mm:ss')
            self.update_date.emit(currenttime)
            time.sleep(1)


class UpdateUI(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle('利用子线程更新显示时间')
        self.resize(400, 100)

        self.ledit = QLineEdit(self)
        self.ledit.resize(400, 100)
        self.ledit.setFont(QFont('Arial', 15))
        self.ledit.setAlignment(Qt.AlignCenter)
        self.ledit.setEnabled(False)  # 设置启用，激活模式，False，不可激活，不可进行任何操作
        # self.ledit.setReadOnly(True)  # 设置只读模式，可选取，可复制，不可以编辑
        self.initUI()

    def initUI(self):
        self.backed = BackThread()
        self.backed.update_date.connect(self.displaytime)
        self.backed.start()

    def displaytime(self, date):
        self.ledit.setText(date)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = UpdateUI()
    w.show()
    sys.exit(app.exec_())