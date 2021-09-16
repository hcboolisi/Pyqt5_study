import sys

from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtWidgets import QWidget, QCalendarWidget, QLabel, QVBoxLayout, QApplication, QStyle


class Calendar(QWidget):
    def __init__(self):
        super(Calendar, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('日历控件')
        self.cal = QCalendarWidget()
        self.cal.setMaximumDate(QDate(2086, 12, 31))
        self.cal.setMinimumDate(QDate(1986, 1, 1))
        self.cal.setGridVisible(True)
        self.cal.clicked.connect(self.showdate)

        self.label = QLabel()
        self.label.setFont(QFont('SimSun', 15, 10, True))
        palette = QPalette()
        palette.setColor(QPalette.WindowText,  QColor(120, 33, 200, 233))
        self.label.setPalette(palette)

        vbox = QVBoxLayout()
        vbox.addWidget(self.cal)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def showdate(self, date):    # 三种方式来实现该功能
        # sender = self.sender()
        # self.label.setText(sender.selectedDate().toString('yyyy-MM-dd dddd'))
        self.label.setText(date.toString('yyyy-MM-dd dddd'))
        # self.label.setText(self.cal.selectedDate().toString('yyyy-MM-dd dddd'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Calendar()
    w.show()
    sys.exit(app.exec_())